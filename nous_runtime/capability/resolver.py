# -*- coding: utf-8 -*-
"""
Capability Resolver -enforces Capability->Provider->Execution separation.

The resolver ensures that:
  1. Capabilities declare WHAT (not WHO)
  2. Providers declare WHO/HOW (not WHAT)
  3. Execution always goes: request ->resolve ->select ->execute ->audit
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

from nous_runtime.planner.observation import Observation

log = logging.getLogger("nous.capability.resolver")


@dataclass
class ResolutionResult:
    """Result of resolving a capability request to a provider."""
    capability_id: str
    provider_id: str = ""
    provider_name: str = ""
    resolved: bool = False
    error: str = ""
    params: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExecutionResult:
    """Result of executing a capability via a provider."""
    ok: bool
    capability_id: str
    provider_id: str
    result: Any = None
    error: str = ""
    error_code: str = ""
    duration_ms: float = 0.0

    @classmethod
    def from_observation(cls, observation: Observation) -> "ExecutionResult":
        """Build the legacy execution result from an Observation.

        This keeps existing SDK/CLI callers stable while making
        Observation the canonical execution output inside the Runtime.
        """
        data = observation.data or {}
        metadata = observation.metadata or {}
        ok = observation.status == "success"
        return cls(
            ok=ok,
            capability_id=observation.capability or observation.tool,
            provider_id=str(metadata.get("provider_id", "")),
            result=data.get("result", data),
            error="; ".join(observation.errors) if observation.errors else "",
            error_code=str(metadata.get("error_code", "")),
            duration_ms=observation.duration_ms,
        )


def resolve_capability(capability_id: str) -> ResolutionResult:
    """
    Resolve a capability to an available provider.

    Steps:
      1. Look up capability in registry
      2. Find providers that serve this capability
      3. Select best provider (health, latency, cost)
      4. Return resolution

    Args:
        capability_id: Dotted capability name (e.g., "model.reason").

    Returns:
        ResolutionResult with selected provider or error.
    """
    result = ResolutionResult(capability_id=capability_id)

    # 1. Check capability exists
    try:
        from nous_runtime.compat.capability import get_capability, list_capabilities
        cap = get_capability(capability_id)
        if not cap:
            # Try listing all to give helpful error
            all_caps = list_capabilities()
            names = [c.get("name", "?") if isinstance(c, dict) else str(c) for c in all_caps[:10]]
            result.error = (
                f"Capability '{capability_id}' not found. "
                f"Available: {', '.join(names)}..."
            )
            return result
    except Exception as e:
        result.error = f"Capability lookup failed: {e}"
        return result

    # 2. Find providers
    try:
        from nous_runtime.compat.provider import list_providers, get_provider
        providers = list_providers()
        candidates = []
        for entry in providers:
            pid = entry.get("provider_id", entry.get("name", ""))
            caps = entry.get("capabilities", [])
            if capability_id in caps or any(
                capability_id.startswith(c.replace("*", "")) for c in caps
            ):
                candidates.append((pid, get_provider(pid)))

        if not candidates:
            result.error = f"No provider found for capability '{capability_id}'"
            return result

        # 3. Select best provider (prefer healthy, then first match)
        for pid, p in candidates:
            if p is None:
                continue
            try:
                h = p.health()
                if h.get("status") == "ok":
                    result.provider_id = pid
                    result.provider_name = getattr(p, "provider_name", pid)
                    result.resolved = True
                    return result
            except Exception:
                continue

        # Fallback: use first candidate even if health unknown
        if candidates:
            pid, p = candidates[0]
            if p is not None:
                result.provider_id = pid
                result.provider_name = getattr(p, "provider_name", pid)
                result.resolved = True
            else:
                result.error = (
                    f"No healthy provider for '{capability_id}'. "
                    f"Run: nous provider setup"
                )
        else:
            result.error = (
                f"No provider configured for '{capability_id}'. "
                f"Run: nous provider setup"
            )

    except Exception as e:
        result.error = f"Provider selection failed: {e}"

    return result


def execute_capability_observation(
    capability_id: str,
    *,
    _authorization_context=None,
    _governance_surface: str = "local_cli",
    **params,
) -> Observation:
    """
    Execute a capability through the resolver pipeline and return Observation.

    Args:
        capability_id: Dotted capability name.
        **params: Parameters for the capability.

    Returns:
        Observation with structured data, errors, duration, and provider metadata.
    """
    import time
    start = time.time()

    # 1. Resolve
    resolution = resolve_capability(capability_id)
    if not resolution.resolved:
        return Observation.failure(
            "capability.execute",
            [resolution.error],
            capability=capability_id,
            duration_ms=(time.time() - start) * 1000,
            metadata={
                "provider_id": "",
                "provider_name": "",
                "error_code": "NOUS_CAPABILITY_NOT_FOUND",
                "stage": "resolve",
            },
        )

    # 1.5 Authorization Gate (B1)
    try:
        from nous_runtime.governance import (
            ActionProposal,
            AuthorizationContext,
            get_gate,
        )
        from nous_runtime.governance.runtime_mode import should_fail_closed
        import os as _os
        import getpass as _getpass

        workspace = _os.getcwd()
        try:
            from nous_runtime.project.workspace import find_workspace
            ws = find_workspace()
            if ws:
                workspace = str(ws)
        except Exception:
            pass

        proposal = ActionProposal(
            action_type="capability.execute",
            capability_id=capability_id,
            target_workspace=workspace,
            side_effect_class=_infer_side_effect(capability_id),
            reversibility=_infer_reversibility(capability_id),
            parameter_summary=str(params)[:200],
            params=dict(params),
        )

        context = _authorization_context or AuthorizationContext(
            subject_type="user",
            subject_id=f"{_getpass.getuser()}@{_os.environ.get('COMPUTERNAME', 'localhost')}",
            authn_method="cli_os_user",
            authn_confidence=0.8,
            session_locality="local",
        )

        gate = get_gate()
        decision = gate.evaluate(proposal, context)

        fail_closed = should_fail_closed(surface=_governance_surface)
        if decision.action_mode == "DENY":
            if fail_closed or decision.rule_class == "NON_OVERRIDABLE":
                return Observation.failure(
                    "capability.execute",
                    [f"Authorization denied: {decision.reason_message}"],
                    capability=capability_id,
                    duration_ms=(time.time() - start) * 1000,
                    metadata={
                        "provider_id": "",
                        "error_code": "NOUS_UNAUTHORIZED",
                        "stage": "authorization",
                        "gate_decision_id": decision.decision_id,
                        "gate_reason": decision.reason_code,
                    },
                )
            log.warning(
                "Governance DENY recorded but compatibility execution continues: %s",
                decision.reason_code,
            )
        elif decision.action_mode == "ASK_APPROVAL":
            if fail_closed:
                return Observation.failure(
                    "capability.execute",
                    [f"Approval required: {decision.reason_message}"],
                    capability=capability_id,
                    duration_ms=(time.time() - start) * 1000,
                    metadata={
                        "provider_id": "",
                        "error_code": "NOUS_APPROVAL_REQUIRED",
                        "stage": "authorization",
                        "gate_decision_id": decision.decision_id,
                        "approval_required": True,
                    },
                )
            log.warning("Governance approval required but compatibility execution continues")
        elif decision.action_mode == "ESCALATE":
            if fail_closed:
                return Observation.failure(
                    "capability.execute",
                    [f"Escalated: {decision.reason_message}"],
                    capability=capability_id,
                    duration_ms=(time.time() - start) * 1000,
                    metadata={
                        "provider_id": "",
                        "error_code": "NOUS_ESCALATED",
                        "stage": "authorization",
                        "gate_decision_id": decision.decision_id,
                    },
                )
            log.warning("Governance escalation recorded but compatibility execution continues")
        # EXECUTE, RECOMMEND, or compatibility continuation: proceed
    except Exception as e:
        import logging
        from nous_runtime.governance.runtime_mode import should_fail_closed
        _log = logging.getLogger("nous.capability.resolver")
        if should_fail_closed(surface=_governance_surface):
            _log.error("Gate evaluation failed; strict governance blocks execution: %s", e)
            return Observation.failure(
                "capability.execute",
                [f"Governance gate unavailable: {e}"],
                capability=capability_id,
                duration_ms=(time.time() - start) * 1000,
                metadata={
                    "provider_id": "",
                    "error_code": "NOUS_GOVERNANCE_UNAVAILABLE",
                    "stage": "authorization",
                    "gate_bypass_blocked": True,
                },
            )
        _log.warning("Gate evaluation failed (compatibility execution): %s", e)

    # 2. Execute via provider
    try:
        from nous_runtime.intelligence.reliability.executor import execute_provider_observation
        provider_obs = execute_provider_observation(
            resolution.provider_id,
            capability_id,
            payload=params,
        )
        ok = provider_obs.status == "success"
        duration_ms = (time.time() - start) * 1000
        metadata = {
            "provider_id": resolution.provider_id,
            "provider_name": resolution.provider_name,
            "error_code": "" if ok else "NOUS_EXECUTION_FAILED",
            "stage": "execute",
            "provider_observation_id": provider_obs.observation_id,
        }
        provider_metadata = provider_obs.metadata or {}
        for key in ("reliability_wrapped", "execution_id", "model_id"):
            if key in provider_metadata:
                metadata[key] = provider_metadata[key]
        if provider_metadata.get("error_code"):
            metadata["error_code"] = provider_metadata["error_code"]

        if ok:
            return Observation.success(
                "capability.execute",
                {
                    "result": provider_obs.data.get("result", provider_obs.data),
                    "provider_observation": provider_obs.summary(),
                },
                capability=capability_id,
                duration_ms=duration_ms,
                metadata=metadata,
            )
        return Observation.failure(
            "capability.execute",
            provider_obs.errors or ["execution failed"],
            capability=capability_id,
            duration_ms=duration_ms,
            metadata=metadata,
        )
    except Exception as e:
        return Observation.failure(
            "capability.execute",
            [str(e)],
            capability=capability_id,
            duration_ms=(time.time() - start) * 1000,
            metadata={
                "provider_id": resolution.provider_id,
                "provider_name": resolution.provider_name,
                "error_code": "NOUS_PROVIDER_UNAVAILABLE",
                "stage": "provider",
            },
        )


def _infer_side_effect(capability_id: str) -> str:
    """Infer side-effect class from capability name."""
    if capability_id in ("system.echo", "system.status"):
        return "read_only"
    if "file_write" in capability_id or "write" in capability_id:
        return "local_write"
    if "file_read" in capability_id or "read" in capability_id or "search" in capability_id:
        return "read_only"
    if "shell" in capability_id or "exec" in capability_id:
        return "destructive"
    if capability_id.startswith("model."):
        return "external_write"
    return "unknown"


def _infer_reversibility(capability_id: str) -> str:
    """Infer reversibility from capability name."""
    if capability_id in ("system.echo", "system.status"):
        return "reversible"
    if "file_write" in capability_id:
        return "partially_reversible"
    if "shell" in capability_id or "exec" in capability_id or "delete" in capability_id:
        return "irreversible"
    if capability_id.startswith("model."):
        return "reversible"
    return "unknown"


def execute_capability(capability_id: str, **params) -> ExecutionResult:
    """
    Execute a capability through the resolver pipeline.

    This is the legacy public API. Internally the Runtime now produces
    Observation first, then adapts it to ExecutionResult for existing callers.
    New Runtime code should prefer execute_capability_observation().
    """
    observation = execute_capability_observation(capability_id, **params)
    return ExecutionResult.from_observation(observation)
