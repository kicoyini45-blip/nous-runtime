from __future__ import annotations

from types import SimpleNamespace

import pytest

from nous_runtime.runtime.orchestrator import RuntimeOrchestrator
from nous_runtime.runtime.pipeline import PRODUCT_CAPABILITIES, RuntimePipeline
from nous_runtime.runtime.request import RuntimeRequest


class ExecuteGate:
    def __init__(self):
        self.proposals = []

    def evaluate(self, proposal, context):
        self.proposals.append((proposal, context))
        return SimpleNamespace(
            action_mode="EXECUTE", reason_message="allowed", reason_code="TEST", decision_id="decision-1"
        )


def test_all_products_use_one_governed_runtime_path(tmp_path, monkeypatch):
    observed: list[tuple[str, dict[str, str]]] = []
    gate = ExecuteGate()
    monkeypatch.setattr(RuntimePipeline, "_build_context", lambda self, request, intent, workspace: {})
    monkeypatch.setattr(RuntimePipeline, "_plan", lambda self, request, intent, workspace: {"status": "planned", "reason": ""})
    monkeypatch.setattr(RuntimePipeline, "_decide", lambda self, request, workspace, intent: {"selected": "bound", "reason": ""})
    monkeypatch.setattr(RuntimePipeline, "_evaluate", lambda self, request, workspace, trace, execution: {"status": "evaluated"})
    monkeypatch.setattr(RuntimePipeline, "_collect_experience", lambda self, workspace, execution, evaluation: {"status": "collected"})

    def binding(name):
        def execute(request, context):
            observed.append((name, context))
            return {"ok": True, "status": "success", "product": name, "owner": request.user_id}

        return execute

    runtime = RuntimeOrchestrator(
        workspace_root=str(tmp_path),
        product_handlers={name: binding(name) for name in PRODUCT_CAPABILITIES},
        gate=gate,
    )

    for product in sorted(PRODUCT_CAPABILITIES):
        request = RuntimeRequest(
            "status",
            user_id="owner-a",
            session=f"session-{product}",
            constraints={"product_capability": product},
        )
        response = runtime.run(request)
        assert response.status == "ok"
        assert response.result["execution"]["capability"] == product
        assert response.result["execution"]["builtin_fallback"] is False
        assert response.result["execution"]["result"]["owner"] == "owner-a"
        event_types = [event.event_type for event in runtime.pipeline.events.load_events(request.request_id)]
        assert event_types == ["runtime.request.received", "runtime.response.ready"]

    assert {name for name, _ in observed} == set(PRODUCT_CAPABILITIES)
    assert all(context["user_id"] == "owner-a" for _, context in observed)
    assert {proposal.capability_id for proposal, _ in gate.proposals} == {
        f"product.{name}" for name in PRODUCT_CAPABILITIES
    }


def test_product_bindings_are_explicit_and_fail_closed(tmp_path, monkeypatch):
    with pytest.raises(ValueError, match="unknown product"):
        RuntimeOrchestrator(
            workspace_root=str(tmp_path),
            product_handlers={"not_a_product": lambda request, context: {}},
        )

    monkeypatch.setattr(RuntimePipeline, "_build_context", lambda self, request, intent, workspace: {})
    monkeypatch.setattr(RuntimePipeline, "_plan", lambda self, request, intent, workspace: {"status": "planned", "reason": ""})
    monkeypatch.setattr(RuntimePipeline, "_decide", lambda self, request, workspace, intent: {"selected": "bound", "reason": ""})
    monkeypatch.setattr(RuntimePipeline, "_evaluate", lambda self, request, workspace, trace, execution: {"status": "evaluated"})
    monkeypatch.setattr(RuntimePipeline, "_collect_experience", lambda self, workspace, execution, evaluation: {"status": "collected"})
    runtime = RuntimeOrchestrator(workspace_root=str(tmp_path), gate=ExecuteGate())
    response = runtime.run(
        RuntimeRequest("status", constraints={"product_capability": "not_a_product"})
    )
    assert response.status == "failed"
    assert response.result["execution"]["builtin_fallback"] is False
