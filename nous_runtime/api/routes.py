# -*- coding: utf-8 -*-
"""
Nous Runtime API v1 -unified REST API routes.

All surfaces (CLI, Web, Desktop, Mobile) call these endpoints.
No surface has its own database. No surface has its own state.

Base URL: /api/v1

Endpoints:
    GET  /status               Runtime status
    GET  /health                Health check
    GET  /version               Version info

    GET  /capabilities          List capabilities
    POST /capabilities/run      Execute a capability

    GET  /providers             List providers
    GET  /providers/health      Provider health aggregation

    GET  /packs                 List installed packs
    POST /packs/install         Install a pack
    DELETE /packs/{name}        Remove a pack

    GET  /jobs                  List jobs
    GET  /jobs/{id}             Get job detail

    GET  /traces                Recent execution traces
    GET  /traces/{id}           Trace detail

    GET  /experience/stats      Experience statistics

    GET  /objects               List runtime objects
    GET  /objects/{kind}/{id}   Get object detail
"""

from __future__ import annotations

import hmac
import logging
import os
import re
from typing import Any
from urllib.parse import unquote

log = logging.getLogger("nous.api")


# Response Helpers

def ok_response(data: Any = None) -> dict[str, Any]:
    return {"ok": True, "data": data}


def err_response(code: str, message: str, details: dict | None = None) -> dict[str, Any]:
    return {
        "ok": False,
        "error": {"code": code, "message": message, "details": details or {}},
    }


PUBLIC_ROUTES = {
    ("GET", "/api/v1/health"),
    ("GET", "/api/v1/version"),
}
MUTATION_METHODS = {"POST", "PUT", "PATCH", "DELETE"}


def _extract_bearer(value: str) -> str:
    value = value.strip()
    if value.lower().startswith("bearer "):
        return value[7:].strip()
    return value


def _authentication_context(auth: dict[str, Any] | None, *, surface: str):
    if not auth or auth.get("query_token"):
        return None
    token = str(auth.get("token") or "")
    headers = auth.get("headers") or {}
    if not token and isinstance(headers, dict):
        token = str(headers.get("x-auth-token") or headers.get("X-Auth-Token") or "")
        if not token:
            token = _extract_bearer(str(headers.get("authorization") or headers.get("Authorization") or ""))
    configured = os.environ.get("NOUS_API_TOKEN") or os.environ.get("NOUS_AUTH_TOKEN")
    if not configured or not token or not hmac.compare_digest(token, configured):
        return None

    from nous_runtime.governance.contracts import AuthorizationContext

    return AuthorizationContext(
        subject_type="service",
        subject_id=os.environ.get("NOUS_API_SUBJECT", "api-service"),
        authn_method="api_bearer_token",
        authn_confidence=0.9,
        session_locality="remote" if surface in {"server", "api", "control_plane"} else "local",
    )


def _is_authenticated(auth: dict[str, Any] | None, *, surface: str = "local_cli") -> bool:
    return _authentication_context(auth, surface=surface) is not None


def _auth_required(method: str, path: str, *, surface: str = "local_cli") -> bool:
    method = method.upper()
    if (method, path) in PUBLIC_ROUTES:
        return False
    if method in MUTATION_METHODS:
        return True
    from nous_runtime.governance.runtime_mode import should_fail_closed

    return should_fail_closed(surface=surface)


def _authorize_api_request(
    method: str,
    path: str,
    auth: dict[str, Any] | None,
    *,
    surface: str = "local_cli",
) -> dict[str, Any] | None:
    if not _auth_required(method, path, surface=surface):
        return None
    if _is_authenticated(auth, surface=surface):
        return None
    return err_response(
        "NOUS_UNAUTHENTICATED",
        "Authentication required",
        {"path": path, "method": method.upper()},
    )


# Status

def handle_status() -> dict[str, Any]:
    try:
        from nous_runtime.kernel.runtime import Runtime
        from nous_runtime.services.packs import count_packs
        r = Runtime()
        s = r.status()
        return ok_response({
            "version": s.version,
            "running": s.running,
            "providers": s.providers,
            "capabilities": s.capabilities,
            "packs": count_packs(),
            "devices": s.devices,
            "events": s.events_total,
            "jobs_pending": s.jobs_pending,
            "demo_mode": s.demo_mode,
        })
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


def handle_health() -> dict[str, Any]:
    try:
        from nous_runtime.services.providers import provider_health_summary
        return ok_response(provider_health_summary())
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


def handle_version() -> dict[str, Any]:
    from nous_runtime import __version__
    return ok_response({"version": __version__})


# Capabilities

def handle_list_capabilities() -> dict[str, Any]:
    try:
        from nous_runtime.services.capabilities import list_capabilities
        return ok_response(list_capabilities())
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


def handle_run_capability(
    body: dict,
    *,
    authorization_context=None,
    governance_surface: str = "local_cli",
) -> dict[str, Any]:
    capability_id = body.get("capability_id", "")
    params = body.get("params", {})
    if not capability_id:
        return err_response("NOUS_INVALID_REQUEST", "capability_id is required")
    if not isinstance(params, dict):
        return err_response("NOUS_INVALID_REQUEST", "params must be an object")
    reserved = {"_authorization_context", "_governance_surface"} & set(params)
    if reserved:
        return err_response("NOUS_INVALID_REQUEST", "reserved execution parameters are not allowed")

    from nous_runtime.capability.resolver import execute_capability
    result = execute_capability(
        capability_id,
        _authorization_context=authorization_context,
        _governance_surface=governance_surface,
        **params,
    )
    return ok_response({
        "ok": result.ok,
        "capability_id": result.capability_id,
        "provider_id": result.provider_id,
        "result": result.result,
        "error": result.error,
        "error_code": result.error_code,
        "duration_ms": result.duration_ms,
    })


# Providers

def handle_list_providers() -> dict[str, Any]:
    try:
        from nous_runtime.services.providers import list_provider_summaries
        return ok_response(list_provider_summaries())
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


def handle_provider_health() -> dict[str, Any]:
    try:
        from nous_runtime.services.providers import provider_health_summary
        return ok_response(provider_health_summary())
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


# Packs

def handle_list_packs() -> dict[str, Any]:
    try:
        from nous_runtime.services.packs import list_packs
        return ok_response(list_packs())
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


def handle_install_pack(body: dict) -> dict[str, Any]:
    path = body.get("path", "")
    if not path:
        return err_response("NOUS_INVALID_REQUEST", "path is required")
    try:
        from nous_runtime.services.packs import install_pack
        return ok_response(install_pack(path))
    except Exception as e:
        return err_response("NOUS_EXECUTION_FAILED", str(e))


def handle_remove_pack(name: str) -> dict[str, Any]:
    try:
        from nous_runtime.services.packs import remove_pack
        remove_pack(name)
        return ok_response({"removed": name})
    except Exception as e:
        return err_response("NOUS_EXECUTION_FAILED", str(e))


# Jobs

def handle_list_jobs(status_filter: str = "") -> dict[str, Any]:
    try:
        from nous_runtime.services.jobs import list_jobs
        if status_filter:
            return ok_response(list_jobs(status=status_filter))
        return ok_response(list_jobs())
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


def handle_get_job(job_id: str) -> dict[str, Any]:
    try:
        from nous_runtime.services.jobs import get_job
        job = get_job(job_id)
        if job:
            return ok_response(job)
        return err_response("NOUS_CAPABILITY_NOT_FOUND", f"Job {job_id} not found")
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


# Traces

def handle_list_traces(limit: int = 20, session_id: str = "") -> dict[str, Any]:
    try:
        from nous_runtime.services.traces import get_recent_traces, get_session_traces
        if session_id:
            return ok_response(get_session_traces(session_id))
        return ok_response(get_recent_traces(limit))
    except Exception as e:
        return err_response("NOUS_INTERNAL_ERROR", str(e))


# Experience

def handle_experience_stats(provider_id: str = "", capability_id: str = "") -> dict[str, Any]:
    from nous_runtime.learning.experience import stats
    return ok_response(stats(provider_id=provider_id, capability_id=capability_id))


def _inspector_snapshot_dict() -> dict[str, Any]:
    from nous_runtime.inspector import diagnose, snapshot

    snap = snapshot()
    snap.findings = diagnose(snap)
    return snap.to_dict()


def handle_inspector_runtime() -> dict[str, Any]:
    return ok_response(_inspector_snapshot_dict()["runtime"])


def handle_inspector_capabilities() -> dict[str, Any]:
    return ok_response(_inspector_snapshot_dict()["capabilities"])


def handle_inspector_tasks() -> dict[str, Any]:
    return ok_response(_inspector_snapshot_dict()["tasks"])


def handle_inspector_observations() -> dict[str, Any]:
    return ok_response(_inspector_snapshot_dict()["observations"])


def handle_inspector_memory() -> dict[str, Any]:
    return ok_response(_inspector_snapshot_dict()["memory"])


def handle_inspector_diagnostics() -> dict[str, Any]:
    return ok_response(_inspector_snapshot_dict()["findings"])


def handle_inspector_decisions(limit: int = 20) -> dict[str, Any]:
    from nous_runtime.intelligence import DecisionHistory
    from nous_runtime.project.workspace import find_workspace

    workspace = find_workspace()
    if workspace is None:
        return ok_response([])
    return ok_response([decision.to_dict() for decision in DecisionHistory(workspace).list(limit=limit)])


def _inspector_decision(decision_id: str):
    from nous_runtime.intelligence import DecisionHistory
    from nous_runtime.project.workspace import find_workspace

    workspace = find_workspace()
    if workspace is None:
        return None
    return DecisionHistory(workspace).get(decision_id)


def handle_inspector_decision_candidates(decision_id: str) -> dict[str, Any]:
    decision = _inspector_decision(decision_id)
    if decision is None:
        return ok_response([])
    return ok_response([candidate.to_dict() for candidate in decision.candidates])


def handle_inspector_decision_ranking(decision_id: str) -> dict[str, Any]:
    decision = _inspector_decision(decision_id)
    if decision is None:
        return ok_response([])
    return ok_response(
        [
            {"candidate_id": candidate.candidate_id, "score": candidate.score, "rank": idx + 1}
            for idx, candidate in enumerate(sorted(decision.candidates, key=lambda item: (-item.score, item.candidate_id)))
        ]
    )


def handle_inspector_decision_constraints(decision_id: str) -> dict[str, Any]:
    decision = _inspector_decision(decision_id)
    if decision is None:
        return ok_response([])
    return ok_response([item.__dict__ for item in decision.rejected_candidates])


def handle_inspector_decision_score(decision_id: str) -> dict[str, Any]:
    decision = _inspector_decision(decision_id)
    if decision is None:
        return ok_response([])
    return ok_response([item.__dict__ for item in decision.score_breakdown])


def handle_inspector_outcomes(limit: int = 20, decision_id: str = "") -> dict[str, Any]:
    from nous_runtime.intelligence import JsonlDecisionStore
    from nous_runtime.project.workspace import find_workspace

    workspace = find_workspace()
    if workspace is None:
        return ok_response([])
    return ok_response([outcome.to_dict() for outcome in JsonlDecisionStore(workspace).list_outcomes(limit=limit, decision_id=decision_id)])


def handle_inspector_incomplete_decisions() -> dict[str, Any]:
    from nous_runtime.intelligence import lifecycle_for_workspace
    from nous_runtime.project.workspace import find_workspace

    workspace = find_workspace()
    if workspace is None:
        return ok_response([])
    return ok_response([decision.to_dict() for decision in lifecycle_for_workspace(str(workspace)).incomplete_decisions()])


def handle_inspector_provider_reliability(provider_id: str = "") -> dict[str, Any]:
    from nous_runtime.intelligence.reliability import JsonlReliabilityStore
    from nous_runtime.intelligence.profiles import JsonlProfileStore
    from nous_runtime.intelligence.replay import frozen_replay_summary
    from nous_runtime.intelligence import JsonlDecisionStore
    from nous_runtime.project.workspace import find_workspace

    workspace = find_workspace()
    if workspace is None:
        return ok_response([])
    store = JsonlReliabilityStore(workspace)
    profiles = JsonlProfileStore(workspace)
    if provider_id:
        health = store.get_current_health(provider_id, "")
        circuit = store.get_circuit_state(f"{provider_id}:*")
        observations = [
            item.to_dict()
            for item in profiles.list_performance_observations(limit=50)
            if item.provider_id == provider_id
        ]
        return ok_response(
            {
                "provider_id": provider_id,
                "health": health.to_dict() if health else None,
                "circuit": circuit.to_dict() if circuit else None,
                "recent_failures": [item.to_dict() for item in store.list_signals(provider_id=provider_id, limit=20)],
                "recent_retries": [item.to_dict() for item in store.list_retries(provider_id=provider_id, limit=20)],
                "fallback_chains": [item.to_dict() for item in store.list_fallbacks(limit=20)],
                "profile_observations": observations[-20:],
            }
        )
    decisions = JsonlDecisionStore(workspace).list_decisions(limit=20)
    return ok_response(
        {
            "integrity": store.verify_integrity(),
            "recent_failures": [item.to_dict() for item in store.list_signals(limit=20)],
            "recent_retries": [item.to_dict() for item in store.list_retries(limit=20)],
            "fallback_chains": [item.to_dict() for item in store.list_fallbacks(limit=20)],
            "profile_observation_count": len(profiles.list_performance_observations(limit=10000)),
            "frozen_replay": [frozen_replay_summary(decision) for decision in decisions],
            "deprecated_path_diagnostics": [
                {
                    "path": "nous_runtime.compat.provider.invoke_via_provider_observation",
                    "status": "compatibility_routed",
                    "canonical": "nous_runtime.intelligence.reliability.executor.execute_provider_observation",
                }
            ],
        }
    )


def handle_inspector_consistency() -> dict[str, Any]:
    from nous_runtime.intelligence.consistency import verify_cross_store_consistency
    from nous_runtime.project.workspace import find_workspace

    workspace = find_workspace()
    if workspace is None:
        return ok_response({"ok": True, "findings": [], "counts": {}})
    return ok_response(verify_cross_store_consistency(workspace))


# ---------------------------------------------------------------------------
# Context Runtime handlers (Phase 3)
# ---------------------------------------------------------------------------

def _get_context_workspace() -> str:
    try:
        from nous_runtime.project.workspace import find_workspace
        return find_workspace() or ""
    except Exception:
        return ""


def handle_context_current() -> dict[str, Any]:
    """Build and return current context snapshot."""
    try:
        from nous_runtime.context.builder import BuildRequest, build_context
        ws = _get_context_workspace()
        request = BuildRequest(intent="api_request", max_items=100)
        snapshot = build_context(request, workspace=ws)
        return ok_response(snapshot.to_dict())
    except Exception as e:
        return err_response("CONTEXT_BUILD_ERROR", str(e))


def handle_context_history() -> dict[str, Any]:
    """List context snapshot history."""
    try:
        from nous_runtime.context.snapshot import list_snapshots
        ws = _get_context_workspace()
        snapshots = list_snapshots(workspace=ws, limit=50)
        return ok_response(snapshots)
    except Exception as e:
        return err_response("CONTEXT_HISTORY_ERROR", str(e))


def handle_context_explain() -> dict[str, Any]:
    """Explain the current context snapshot."""
    try:
        from nous_runtime.context.explain import explain_snapshot
        from nous_runtime.context.store import ContextStore
        ws = _get_context_workspace()
        store = ContextStore(ws)
        active = store.list(status="active", limit=1)
        if not active:
            return err_response("CONTEXT_NOT_FOUND", "No active context snapshot found.")
        exp = explain_snapshot(active[0])
        return ok_response(exp.to_dict())
    except Exception as e:
        return err_response("CONTEXT_EXPLAIN_ERROR", str(e))


def handle_context_timeline() -> dict[str, Any]:
    """Show context timeline."""
    try:
        from nous_runtime.context.store import ContextStore
        ws = _get_context_workspace()
        store = ContextStore(ws)
        snapshots = store.list(limit=50, order="ASC")
        timeline = [
            {
                "id": s.id,
                "timestamp": s.timestamp,
                "status": s.status,
                "item_count": s.item_count,
                "confidence": s.confidence,
                "intent": s.metadata.get("intent", ""),
            }
            for s in snapshots
        ]
        return ok_response(timeline)
    except Exception as e:
        return err_response("CONTEXT_TIMELINE_ERROR", str(e))


def handle_context_snapshot(body: dict | None = None) -> dict[str, Any]:
    """Create a new context snapshot."""
    try:
        from nous_runtime.context.snapshot import create_snapshot
        ws = _get_context_workspace()
        intent = (body or {}).get("intent", "api_snapshot")
        snapshot = create_snapshot(workspace=ws, intent=intent)
        return ok_response(snapshot.to_dict())
    except Exception as e:
        return err_response("CONTEXT_SNAPSHOT_ERROR", str(e))


def handle_context_restore(body: dict | None = None) -> dict[str, Any]:
    """Restore context from a snapshot."""
    try:
        from nous_runtime.context.snapshot import restore_snapshot
        ws = _get_context_workspace()
        snapshot_id = (body or {}).get("snapshot_id", "")
        result = restore_snapshot(snapshot_id=snapshot_id, workspace=ws)
        return ok_response(result.to_dict())
    except Exception as e:
        return err_response("CONTEXT_RESTORE_ERROR", str(e))


# ---------------------------------------------------------------------------
# Evaluation Runtime handlers (Phase 4)
# ---------------------------------------------------------------------------

def _get_eval_workspace() -> str:
    try:
        from nous_runtime.project.workspace import find_workspace
        return find_workspace() or ""
    except Exception:
        return ""


def handle_evaluation_current() -> dict[str, Any]:
    """Get the most recent evaluation record."""
    try:
        from nous_runtime.evaluation.history import EvaluationHistory
        ws = _get_eval_workspace()
        history = EvaluationHistory(ws)
        records = history.list(limit=1)
        if not records:
            return err_response("EVAL_NOT_FOUND", "No evaluation records found.")
        return ok_response(records[0].to_dict())
    except Exception as e:
        return err_response("EVAL_CURRENT_ERROR", str(e))


def handle_evaluation_history() -> dict[str, Any]:
    """List evaluation history."""
    try:
        from nous_runtime.evaluation.history import EvaluationHistory
        ws = _get_eval_workspace()
        history = EvaluationHistory(ws)
        records = history.list(limit=50)
        return ok_response([r.to_dict() for r in records])
    except Exception as e:
        return err_response("EVAL_HISTORY_ERROR", str(e))


def handle_evaluation_report() -> dict[str, Any]:
    """Get the current evaluation report."""
    try:
        from nous_runtime.evaluation.history import EvaluationHistory
        from nous_runtime.evaluation.report import generate_json_report
        ws = _get_eval_workspace()
        history = EvaluationHistory(ws)
        records = history.list(limit=1)
        if not records:
            return err_response("EVAL_NOT_FOUND", "No evaluation records found.")
        return ok_response(generate_json_report(records[0]))
    except Exception as e:
        return err_response("EVAL_REPORT_ERROR", str(e))


def handle_evaluation_run(body: dict | None = None) -> dict[str, Any]:
    """Run a new evaluation."""
    try:
        from nous_runtime.evaluation.evaluator import EvaluationEngine
        ws = _get_eval_workspace()
        body = body or {}
        target_type = body.get("target_type", "project")
        target_id = body.get("target_id", "current")
        engine = EvaluationEngine(workspace=ws)
        record = engine.evaluate(
            target_type=target_type,
            target_id=target_id,
            input_summary=body.get("input_summary", "API evaluation"),
        )
        return ok_response(record.to_dict())
    except Exception as e:
        return err_response("EVAL_RUN_ERROR", str(e))


# ---------------------------------------------------------------------------
# Experience Runtime handlers (Phase 5)
# ---------------------------------------------------------------------------

def _get_exp_workspace() -> str:
    try:
        from nous_runtime.project.workspace import find_workspace
        return find_workspace() or ""
    except Exception:
        return ""


def handle_experience_list() -> dict[str, Any]:
    try:
        from nous_runtime.experience.store import ExperienceStore
        ws = _get_exp_workspace()
        store = ExperienceStore(ws)
        records = store.list(limit=50)
        return ok_response([r.to_dict() for r in records])
    except Exception as e:
        return err_response("EXP_LIST_ERROR", str(e))


def handle_experience_search() -> dict[str, Any]:
    try:
        from nous_runtime.experience.similarity import SimilarityEngine
        engine = SimilarityEngine()
        results = engine.find_similar_tasks("", limit=20)
        return ok_response([{"record": r.to_dict(), "score": s} for r, s in results])
    except Exception as e:
        return err_response("EXP_SEARCH_ERROR", str(e))


def handle_experience_recommend() -> dict[str, Any]:
    try:
        from nous_runtime.experience.recommendation import RecommendationEngine
        engine = RecommendationEngine()
        recs = engine.recommend("general task")
        return ok_response([r.to_dict() for r in recs])
    except Exception as e:
        return err_response("EXP_RECOMMEND_ERROR", str(e))


def handle_phase5_experience_stats() -> dict[str, Any]:
    try:
        from nous_runtime.experience.analyzer import ExperienceAnalyzer
        from nous_runtime.experience.store import ExperienceStore
        ws = _get_exp_workspace()
        analyzer = ExperienceAnalyzer(ExperienceStore(ws))
        return ok_response(analyzer.summary())
    except Exception as e:
        return err_response("EXP_STATS_ERROR", str(e))



# ---------------------------------------------------------------------------
# Phase 8 Runtime Closure handlers
# ---------------------------------------------------------------------------

def handle_runtime_run(
    body: dict,
    *,
    authorization_context=None,
    governance_surface: str = "local_cli",
) -> dict[str, Any]:
    try:
        from nous_runtime.runtime.orchestrator import RuntimeOrchestrator
        from nous_runtime.runtime.request import RuntimeRequest

        text = str(body.get("user_input") or body.get("text") or "")
        if not text.strip():
            return err_response("NOUS_INVALID_REQUEST", "user_input is required")
        response = RuntimeOrchestrator().run(RuntimeRequest(
            text,
            workspace=str(body.get("workspace") or ""),
            session=str(body.get("session") or ""),
            user_id=authorization_context.subject_id if authorization_context else "api",
            constraints=dict(body.get("constraints") or {}),
            authorization_context=authorization_context.to_dict() if authorization_context else {},
            governance_surface=governance_surface,
        ))
        return ok_response(response.to_dict())
    except Exception as e:
        return err_response("RUNTIME_RUN_ERROR", str(e))


def handle_runtime_sessions() -> dict[str, Any]:
    try:
        from nous_runtime.runtime.session import RuntimeSessionStore
        return ok_response(RuntimeSessionStore().list())
    except Exception as e:
        return err_response("RUNTIME_SESSION_ERROR", str(e))


def handle_runtime_dashboard() -> dict[str, Any]:
    try:
        from nous_runtime.control_center.snapshot import control_center_snapshot

        return ok_response(control_center_snapshot(os.environ.get("NOUS_WORKSPACE_ROOT", ".")))
    except Exception as exc:
        return err_response("RUNTIME_DASHBOARD_ERROR", str(exc))


def handle_runtime_runs(limit: int = 20) -> dict[str, Any]:
    """List canonical runs from the existing EventStream."""
    from nous_runtime.events import EventStream

    root = os.environ.get("NOUS_WORKSPACE_ROOT", ".")
    return ok_response([item.to_dict() for item in EventStream(root).list_runs(limit=max(1, min(int(limit), 200)))])


def handle_run_events(
    run_id: str,
    after_sequence: int = 0,
    limit: int = 200,
) -> dict[str, Any]:
    """Replay canonical persisted events for one Runtime run."""
    from nous_runtime.events import EventStream

    stream = EventStream(os.environ.get("NOUS_WORKSPACE_ROOT", "."))
    if stream.get_run(run_id) is None:
        return err_response("NOUS_NOT_FOUND", f"Run not found: {run_id}")
    events = list(
        stream.iter_persisted_events(
            run_id,
            after_sequence=max(0, int(after_sequence)),
            limit=max(1, min(int(limit), 1000)),
        )
    )
    return ok_response({
        "run_id": run_id,
        "events": [event.to_dict() for event in events],
        "next_after_sequence": events[-1].sequence if events else max(0, int(after_sequence)),
    })

def handle_workspace() -> dict[str, Any]:
    """Describe the active workspace through the existing Workspace Registry."""
    from nous_runtime.workspace.registry import WorkspaceRegistry

    registry = WorkspaceRegistry(os.environ.get("NOUS_WORKSPACE_ROOT", "."))
    active = registry.active()
    return ok_response({
        "active": active.to_dict() if active else None,
        "workspaces": [item.to_dict() for item in registry.list()],
    })


def handle_approvals() -> dict[str, Any]:
    """List pending approvals from the authoritative ApprovalBroker."""
    from nous_runtime.governance.broker import get_broker

    return ok_response({"approvals": get_broker().get_pending()})


def handle_workflow_run(body: dict[str, Any]) -> dict[str, Any]:
    """Start a registered workflow through the existing Workflow Runtime."""
    try:
        from nous_runtime.workflow import WorkflowRuntime

        runtime = WorkflowRuntime(os.environ.get("NOUS_WORKSPACE_ROOT", "."))
        run = runtime.start(
            str(body.get("workflow_id") or ""),
            str(body.get("version") or "1.0.0"),
            dict(body.get("inputs") or {}),
            idempotency_key=str(body.get("idempotency_key") or ""),
        )
        return ok_response({
            "run_id": run.run_id,
            "workflow_id": run.workflow_id,
            "state": run.state.value,
            "step_states": dict(run.step_states),
            "outputs": dict(run.outputs),
            "error": run.error,
        })
    except (KeyError, ValueError) as exc:
        return err_response("NOUS_INVALID_REQUEST", str(exc))

def handle_model_select(body: dict) -> dict[str, Any]:
    try:
        from nous_runtime.model.runtime import ModelRuntime
        from nous_runtime.model.types import ModelRequest

        task_type = str(body.get("task_type") or "general")
        request = ModelRequest(
            task_type=task_type,
            context=str(body.get("context") or ""),
            privacy=str(body.get("privacy") or "standard"),
            cost=float(body.get("cost") or 0.0),
            latency=int(body.get("latency") or 0),
            quality=float(body.get("quality") or 0.0),
            metadata=dict(body.get("metadata") or {}),
        )
        return ok_response(ModelRuntime().select(request).to_dict())
    except Exception as e:
        return err_response("MODEL_SELECT_ERROR", str(e))

def handle_chat_runtime(
    body: dict[str, Any],
    *,
    authorization_context=None,
    governance_surface: str = "local_cli",
) -> dict[str, Any]:
    try:
        from nous_runtime.chat import ChatRequest, ChatRuntime

        subject_id = getattr(authorization_context, "subject_id", "") or "local"
        response = ChatRuntime(os.environ.get("NOUS_WORKSPACE_ROOT", ".")).send(
            ChatRequest(
                text=str(body.get("text") or ""),
                workspace_id=str(body.get("workspace_id") or "default"),
                owner_id=subject_id,
                conversation_id=str(body.get("conversation_id") or ""),
                attachment_ids=tuple(str(item) for item in body.get("attachment_ids") or ()),
            ),
            authorization_context=authorization_context.to_dict() if authorization_context else {},
            governance_surface=governance_surface,
        )
        return ok_response({
            "conversation_id": response.conversation_id,
            "intent": response.intent.value,
            "status": response.status,
            "message": response.message,
            "trace_id": response.trace_id,
            "task_promoted": response.task_promoted,
            "requires_trusted_approval": response.requires_trusted_approval,
            "data": response.data,
        })
    except (PermissionError, ValueError) as exc:
        return err_response("NOUS_INVALID_REQUEST", str(exc))
    except Exception as exc:
        return err_response("NOUS_CHAT_ERROR", str(exc))


def handle_ide_runtime(
    body: dict[str, Any],
    *,
    authorization_context=None,
    governance_surface: str = "server",
) -> dict[str, Any]:
    """Dispatch editor-neutral IDE requests without creating IDE-owned state."""
    del governance_surface
    from nous_runtime.ide import IDERequest, IDERuntimeProtocol

    response = IDERuntimeProtocol(os.environ.get("NOUS_WORKSPACE_ROOT", ".")).handle(
        IDERequest(
            action=str(body.get("action") or ""),
            params=dict(body.get("params") or {}),
            subject_id=getattr(authorization_context, "subject_id", "") or "",
        )
    )
    if response.ok:
        return ok_response(response.data)
    return err_response("NOUS_IDE_REQUEST_ERROR", response.error)

# Route Table

ROUTES = {
    ("GET", "/api/v1/status"): handle_status,
    ("GET", "/api/v1/health"): handle_health,
    ("GET", "/api/v1/version"): handle_version,
    ("GET", "/api/v1/capabilities"): handle_list_capabilities,
    ("POST", "/api/v1/capabilities/run"): handle_run_capability,
    ("GET", "/api/v1/providers"): handle_list_providers,
    ("GET", "/api/v1/providers/health"): handle_provider_health,
    ("GET", "/api/v1/packs"): handle_list_packs,
    ("POST", "/api/v1/packs/install"): handle_install_pack,
    ("DELETE", "/api/v1/packs/{name}"): handle_remove_pack,
    ("GET", "/api/v1/jobs"): handle_list_jobs,
    ("GET", "/api/v1/jobs/{job_id}"): handle_get_job,
    ("GET", "/api/v1/traces"): handle_list_traces,
    ("GET", "/api/v1/experience/stats"): handle_experience_stats,
    ("POST", "/api/runtime/run"): handle_runtime_run,
    ("POST", "/api/chat"): handle_chat_runtime,
    ("POST", "/api/ide/runtime"): handle_ide_runtime,
    ("GET", "/api/runtime/sessions"): handle_runtime_sessions,
    ("GET", "/api/runtime/dashboard"): handle_runtime_dashboard,
    ("GET", "/api/runtime/runs"): handle_runtime_runs,
    ("GET", "/api/runtime/runs/{run_id}/events"): handle_run_events,
    ("GET", "/api/workspace"): handle_workspace,
    ("GET", "/api/control/approvals"): handle_approvals,
    ("POST", "/api/workflow/run"): handle_workflow_run,
    ("POST", "/api/model/select"): handle_model_select,
    ("GET", "/api/inspector/runtime"): handle_inspector_runtime,
    ("GET", "/api/inspector/capabilities"): handle_inspector_capabilities,
    ("GET", "/api/inspector/tasks"): handle_inspector_tasks,
    ("GET", "/api/inspector/observations"): handle_inspector_observations,
    ("GET", "/api/inspector/memory"): handle_inspector_memory,
    ("GET", "/api/inspector/decisions"): handle_inspector_decisions,
    ("GET", "/api/inspector/decision/candidates"): handle_inspector_decision_candidates,
    ("GET", "/api/inspector/decision/ranking"): handle_inspector_decision_ranking,
    ("GET", "/api/inspector/decision/constraints"): handle_inspector_decision_constraints,
    ("GET", "/api/inspector/decision/score"): handle_inspector_decision_score,
    ("GET", "/api/inspector/outcomes"): handle_inspector_outcomes,
    ("GET", "/api/inspector/decisions/incomplete"): handle_inspector_incomplete_decisions,
    ("GET", "/api/inspector/providers/reliability"): handle_inspector_provider_reliability,
    ("GET", "/api/inspector/consistency"): handle_inspector_consistency,
    ("GET", "/api/inspector/diagnostics"): handle_inspector_diagnostics,
    # Context Runtime (Phase 3)
    ("GET", "/api/context/current"): handle_context_current,
    ("GET", "/api/context/history"): handle_context_history,
    ("GET", "/api/context/explain"): handle_context_explain,
    ("GET", "/api/context/timeline"): handle_context_timeline,
    ("POST", "/api/context/snapshot"): handle_context_snapshot,
    ("POST", "/api/context/restore"): handle_context_restore,
    # Evaluation Runtime (Phase 4)
    ("GET", "/api/evaluation/current"): handle_evaluation_current,
    ("GET", "/api/evaluation/history"): handle_evaluation_history,
    ("GET", "/api/evaluation/report"): handle_evaluation_report,
    ("POST", "/api/evaluation/run"): handle_evaluation_run,
    # Experience Runtime (Phase 5)
    ("GET", "/api/experience/list"): handle_experience_list,
    ("GET", "/api/experience/search"): handle_experience_search,
    ("GET", "/api/experience/recommend"): handle_experience_recommend,
    ("GET", "/api/experience/stats"): handle_phase5_experience_stats,
}


GOVERNED_MUTATION_ROUTES = {
    ("POST", "/api/v1/packs/install"): ("pack.install", "external_write", "partially_reversible"),
    ("DELETE", "/api/v1/packs/{name}"): ("pack.remove", "destructive", "partially_reversible"),
    ("POST", "/api/context/snapshot"): ("context.snapshot", "local_write", "reversible"),
    ("POST", "/api/context/restore"): ("context.restore", "local_write", "reversible"),
    ("POST", "/api/evaluation/run"): ("evaluation.run", "local_write", "reversible"),
    ("POST", "/api/workflow/run"): ("workflow.run", "local_write", "partially_reversible"),
}
_PATH_PARAMETER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$")


def _match_route(method: str, path: str):
    exact = ROUTES.get((method, path))
    if exact is not None:
        return exact, path, {}
    actual_parts = path.strip("/").split("/")
    for (route_method, pattern), handler in ROUTES.items():
        if route_method != method or "{" not in pattern:
            continue
        pattern_parts = pattern.strip("/").split("/")
        if len(actual_parts) != len(pattern_parts):
            continue
        captured: dict[str, str] = {}
        matched = True
        for expected, actual in zip(pattern_parts, actual_parts):
            if expected.startswith("{") and expected.endswith("}"):
                value = unquote(actual)
                if not _PATH_PARAMETER.fullmatch(value):
                    matched = False
                    break
                captured[expected[1:-1]] = value
            elif expected != actual:
                matched = False
                break
        if matched:
            return handler, pattern, captured
    return None, "", {}


def _authorize_mutation_route(
    method: str,
    route_path: str,
    body: dict | None,
    params: dict[str, Any],
    authorization_context,
    *,
    surface: str,
) -> dict[str, Any] | None:
    governance = GOVERNED_MUTATION_ROUTES.get((method, route_path))
    if governance is None:
        return None
    if authorization_context is None:
        return err_response("NOUS_UNAUTHENTICATED", "Authentication required")
    capability_id, side_effect_class, reversibility = governance
    try:
        from nous_runtime.governance import ActionProposal, get_gate
        from nous_runtime.governance.runtime_mode import should_fail_closed

        proposal_params = {"body": dict(body or {}), "path_params": dict(params)}
        proposal = ActionProposal(
            action_type="api.mutation",
            capability_id=capability_id,
            params=proposal_params,
            parameter_summary=f"{method} {route_path}",
            target_workspace=str((body or {}).get("workspace") or ""),
            affected_resources=tuple(str(value) for value in params.values()),
            side_effect_class=side_effect_class,
            reversibility=reversibility,
            deployment_channel="api",
            locality="remote" if surface in {"server", "api", "control_plane"} else "local",
        )
        decision = get_gate().evaluate(proposal, authorization_context)
        if decision.action_mode == "EXECUTE":
            return None
        if not should_fail_closed(surface=surface) and decision.rule_class != "NON_OVERRIDABLE":
            log.warning("Compatibility API mutation after governance decision: %s", decision.reason_code)
            return None
        code = "NOUS_APPROVAL_REQUIRED" if decision.action_mode == "ASK_APPROVAL" else "NOUS_UNAUTHORIZED"
        return err_response(
            code,
            decision.reason_message or decision.reason_code,
            {"decision_id": decision.decision_id, "action_mode": decision.action_mode},
        )
    except Exception as exc:
        from nous_runtime.governance.runtime_mode import should_fail_closed

        if should_fail_closed(surface=surface):
            log.exception("API governance evaluation failed: %s %s", method, route_path)
            return err_response("NOUS_GOVERNANCE_UNAVAILABLE", "Governance evaluation unavailable")
        log.warning("Compatibility API mutation without Gate: %s", exc)
        return None
def route(
    method: str,
    path: str,
    body: dict | None = None,
    params: dict | None = None,
    auth: dict[str, Any] | None = None,
    surface: str = "local_cli",
) -> dict[str, Any]:
    """Route an API request to the appropriate handler."""
    method_upper = method.upper()
    handler, route_path, path_params = _match_route(method_upper, path)
    if not handler:
        return err_response("NOUS_INVALID_REQUEST", f"No route: {method} {path}")

    auth_error = _authorize_api_request(method_upper, path, auth, surface=surface)
    if auth_error:
        return auth_error

    try:
        authorization_context = _authentication_context(auth, surface=surface)
        request_params = dict(path_params)
        for name, value in (params or {}).items():
            if name in request_params and request_params[name] != value:
                return err_response("NOUS_INVALID_REQUEST", f"Conflicting route parameter: {name}")
            request_params[name] = value
        governance_error = _authorize_mutation_route(
            method_upper,
            route_path,
            body,
            request_params,
            authorization_context,
            surface=surface,
        )
        if governance_error:
            return governance_error
        if body is not None and handler in {handle_run_capability, handle_runtime_run, handle_chat_runtime, handle_ide_runtime}:
            return handler(
                body,
                authorization_context=authorization_context,
                governance_surface=surface,
            )
        if body is not None:
            return handler(body)
        elif request_params:
            return handler(**request_params)
        else:
            return handler()
    except Exception as e:
        log.exception("API route error: %s %s", method, path)
        return err_response("NOUS_INTERNAL_ERROR", str(e))

def route_server(
    method: str,
    path: str,
    body: dict | None = None,
    params: dict | None = None,
    auth: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Route a request through the fail-closed server API surface."""
    return route(method, path, body=body, params=params, auth=auth, surface="server")
