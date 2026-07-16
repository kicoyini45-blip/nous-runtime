# -*- coding: utf-8 -*-
"""Agent budget helpers."""

from __future__ import annotations

from nous_runtime.agent.models import AgentBudget


class AgentBudgetError(RuntimeError):
    """Raised when an Agent execution would exceed its budget."""


def require_budget(
    budget: AgentBudget,
    *,
    cost_usd: float = 0.0,
    tokens: int = 0,
    runtime_ms: int = 0,
    invocations: int = 1,
) -> None:
    if not budget.allows(
        cost_usd=cost_usd,
        tokens=tokens,
        runtime_ms=runtime_ms,
        invocations=invocations,
    ):
        raise AgentBudgetError("agent budget exceeded")
