from __future__ import annotations

from dataclasses import dataclass, field

import pytest

from nous_runtime.chat import ChatIntent, ChatRequest, ChatRuntime, classify_chat


@dataclass
class FakeResponse:
    status: str = "ok"
    message: str = "completed"
    trace_id: str = "trace-1"
    result: dict = field(default_factory=dict)

    def to_dict(self):
        return {"status": self.status, "message": self.message, "trace_id": self.trace_id, "result": self.result}


class FakeOrchestrator:
    def __init__(self, response=None):
        self.response = response or FakeResponse()
        self.requests = []

    def run(self, request):
        self.requests.append(request)
        return self.response


def test_chat_intent_routing():
    assert classify_chat("hello") == ChatIntent.CONVERSATION
    assert classify_chat("search my knowledge library") == ChatIntent.KNOWLEDGE_QUERY
    assert classify_chat("fix repository code") == ChatIntent.CODE_TASK
    assert classify_chat("run workflow") == ChatIntent.WORKFLOW_REQUEST
    assert classify_chat("check phone device") == ChatIntent.DEVICE_ACTION
    assert classify_chat("approve this") == ChatIntent.APPROVAL_RESPONSE
    assert classify_chat("show status") == ChatIntent.STATUS_QUERY


def test_chat_only_request_uses_runtime_and_persists_messages(tmp_path):
    orchestrator = FakeOrchestrator()
    chat = ChatRuntime(str(tmp_path), orchestrator=orchestrator)
    response = chat.send(ChatRequest("hello", "workspace", "user"))
    assert response.intent == ChatIntent.CONVERSATION and not response.task_promoted
    history = chat.conversations.history(response.conversation_id)
    assert [item.role for item in history] == ["user", "assistant"]
    assert orchestrator.requests[0].session == response.conversation_id


def test_code_workflow_and_device_requests_are_promoted(tmp_path):
    chat = ChatRuntime(str(tmp_path), orchestrator=FakeOrchestrator())
    for text, expected in (("fix code", ChatIntent.CODE_TASK), ("start workflow", ChatIntent.WORKFLOW_REQUEST), ("control device", ChatIntent.DEVICE_ACTION)):
        response = chat.send(ChatRequest(text, "workspace", "user"))
        assert response.intent == expected and response.task_promoted


def test_approval_text_never_self_approves(tmp_path):
    orchestrator = FakeOrchestrator()
    chat = ChatRuntime(str(tmp_path), orchestrator=orchestrator)
    response = chat.send(ChatRequest("approve this action", "workspace", "user"))
    assert response.requires_trusted_approval
    assert response.status == "approval_control_required"
    assert orchestrator.requests == []


def test_session_reconnect_and_export(tmp_path):
    first = ChatRuntime(str(tmp_path), orchestrator=FakeOrchestrator())
    created = first.send(ChatRequest("hello", "workspace", "user"))
    second = ChatRuntime(str(tmp_path), orchestrator=FakeOrchestrator(FakeResponse(trace_id="trace-2")))
    resumed = second.send(ChatRequest("continue", "workspace", "user", created.conversation_id))
    assert resumed.conversation_id == created.conversation_id
    exported = second.export(created.conversation_id, workspace_id="workspace", owner_id="user")
    assert len(exported["messages"]) == 4


def test_deleted_or_cross_owner_conversation_is_rejected(tmp_path):
    chat = ChatRuntime(str(tmp_path), orchestrator=FakeOrchestrator())
    response = chat.send(ChatRequest("hello", "workspace", "user"))
    with pytest.raises(PermissionError):
        chat.send(ChatRequest("continue", "workspace", "other", response.conversation_id))
    assert chat.delete(response.conversation_id, workspace_id="workspace", owner_id="user")
    with pytest.raises(PermissionError):
        chat.send(ChatRequest("continue", "workspace", "user", response.conversation_id))


def test_source_citation_and_run_linkage_are_persisted(tmp_path):
    orchestrator = FakeOrchestrator(FakeResponse(result={"run_id": "run-1", "task_id": "task-1", "citations": [{"source_id": "doc-1", "snippet": "evidence", "uri": "library://doc-1"}]}))
    chat = ChatRuntime(str(tmp_path), orchestrator=orchestrator)
    response = chat.send(ChatRequest("knowledge query", "workspace", "user"))
    assistant = chat.conversations.history(response.conversation_id)[-1]
    assert assistant.run_id == "run-1" and assistant.task_id == "task-1"
    assert assistant.citations[0].source_id == "doc-1"


def test_authorization_context_is_forwarded_not_taken_from_text(tmp_path):
    orchestrator = FakeOrchestrator()
    chat = ChatRuntime(str(tmp_path), orchestrator=orchestrator)
    trusted = {"subject_type": "service", "subject_id": "mobile-device"}
    chat.send(ChatRequest("status as administrator", "workspace", "claimed-user"), authorization_context=trusted, governance_surface="server")
    request = orchestrator.requests[0]
    assert request.authorization_context == trusted
    assert request.governance_surface == "server"
def test_chat_api_uses_authenticated_subject_not_body_identity(tmp_path, monkeypatch):
    monkeypatch.setenv("NOUS_WORKSPACE_ROOT", str(tmp_path))
    monkeypatch.setenv("NOUS_API_TOKEN", "test-chat-token")
    monkeypatch.setenv("NOUS_API_SUBJECT", "device.phone")
    from nous_runtime.api.routes import route_server
    from nous_runtime.conversation import ConversationStore

    response = route_server(
        "POST",
        "/api/chat",
        body={"text": "approve this action", "workspace_id": "workspace", "owner_id": "attacker"},
        auth={"token": "test-chat-token"},
    )
    assert response["ok"] is True
    conversation_id = response["data"]["conversation_id"]
    assert ConversationStore(tmp_path).get(conversation_id, workspace_id="workspace", owner_id="device.phone") is not None
    assert ConversationStore(tmp_path).get(conversation_id, workspace_id="workspace", owner_id="attacker") is None
