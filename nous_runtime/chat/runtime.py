"""Chat entry point over Conversation Store and the unified Runtime Pipeline."""

from __future__ import annotations

from typing import Any

from nous_runtime.chat.models import ChatIntent, ChatRequest, ChatResponse
from nous_runtime.chat.router import classify_chat
from nous_runtime.conversation import Citation, ConversationMessage, ConversationStore
from nous_runtime.runtime.orchestrator import RuntimeOrchestrator
from nous_runtime.runtime.request import RuntimeRequest


class ChatRuntime:
    def __init__(self, root: str = ".", *, orchestrator: RuntimeOrchestrator | None = None):
        self.root = root
        self.conversations = ConversationStore(root)
        self.orchestrator = orchestrator or RuntimeOrchestrator(workspace_root=root)

    def send(self, request: ChatRequest, *, authorization_context: dict[str, Any] | None = None, governance_surface: str = "local_cli") -> ChatResponse:
        if not request.text.strip():
            raise ValueError("chat text is required")
        conversation_id = request.conversation_id
        if conversation_id:
            conversation = self.conversations.get(conversation_id, workspace_id=request.workspace_id, owner_id=request.owner_id)
            if conversation is None:
                raise PermissionError("conversation is unavailable in this workspace and owner scope")
        else:
            conversation = self.conversations.create(request.workspace_id, request.owner_id, title=request.text[:80])
            conversation_id = conversation.conversation_id
        intent = classify_chat(request.text)
        self.conversations.append(ConversationMessage(conversation_id, "user", request.text, attachment_ids=request.attachment_ids))
        if intent == ChatIntent.APPROVAL_RESPONSE:
            message = "Approval responses require an authenticated approval control path."
            self.conversations.append(ConversationMessage(conversation_id, "assistant", message, metadata={"intent": intent.value, "requires_trusted_approval": True}))
            return ChatResponse(conversation_id, intent, "approval_control_required", message, requires_trusted_approval=True)
        context = self.conversations.context_window(conversation_id)
        response = self.orchestrator.run(RuntimeRequest(request.text, workspace=request.workspace_id, session=conversation_id, user_id=request.owner_id, constraints={"product_capability": "chat", "chat_intent": intent.value, "conversation_summary": context["summary"], "conversation_message_ids": [item["message_id"] for item in context["messages"]]}, authorization_context=dict(authorization_context or {}), governance_surface=governance_surface))
        promoted = intent in {ChatIntent.CODE_TASK, ChatIntent.WORKFLOW_REQUEST, ChatIntent.DEVICE_ACTION}
        message = response.message
        citations = tuple(Citation(str(item.get("source_id") or ""), str(item.get("snippet") or ""), str(item.get("uri") or "")) for item in response.result.get("citations") or () if item.get("source_id"))
        self.conversations.append(ConversationMessage(conversation_id, "assistant", message, event_id=response.trace_id, run_id=str(response.result.get("run_id") or ""), task_id=str(response.result.get("task_id") or ""), citations=citations, metadata={"intent": intent.value, "trace_id": response.trace_id, "runtime_status": response.status, "task_promoted": promoted}))
        return ChatResponse(conversation_id, intent, response.status, message, response.trace_id, promoted, False, response.to_dict())

    def export(self, conversation_id: str, *, workspace_id: str, owner_id: str) -> dict[str, Any]:
        if self.conversations.get(conversation_id, workspace_id=workspace_id, owner_id=owner_id) is None:
            raise PermissionError("conversation is unavailable")
        return self.conversations.export(conversation_id)

    def delete(self, conversation_id: str, *, workspace_id: str, owner_id: str) -> bool:
        if self.conversations.get(conversation_id, workspace_id=workspace_id, owner_id=owner_id) is None:
            raise PermissionError("conversation is unavailable")
        return self.conversations.delete(conversation_id)
