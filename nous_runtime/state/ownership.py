"""Canonical state ownership registry.

This module is metadata, not a persistence layer. It records which runtime
component is authoritative for each durable state type so public surfaces and
future services can keep dependency direction explicit.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StateOwnership:
    state: str
    owner: str
    service: str
    persistence: str
    status: str = "active"


STATE_OWNERSHIP: tuple[StateOwnership, ...] = (
    StateOwnership("runtime", "kernel", "nous_runtime.kernel.runtime", "process status"),
    StateOwnership("workspace", "project", "nous_runtime.project.workspace", ".nous directory"),
    StateOwnership("project_memory", "project", "nous_runtime.project.memory", ".nous/memory/*.jsonl"),
    StateOwnership("capability", "capability", "nous_runtime.services.capabilities", "capability registry"),
    StateOwnership("provider", "provider", "nous_runtime.services.providers", "provider registry"),
    StateOwnership("pack", "pack", "nous_runtime.services.packs", "pack registry"),
    StateOwnership("job", "job", "nous_runtime.services.jobs", "legacy jobs table"),
    StateOwnership("trace", "trace", "nous_runtime.services.traces", "reasoning traces table"),
    StateOwnership("event", "event", "nous_runtime.services.events", "events journal"),
    StateOwnership("decision", "intelligence", "nous_runtime.intelligence", "decision JSONL store"),
    StateOwnership("outcome", "intelligence", "nous_runtime.intelligence", "outcome JSONL store"),
    StateOwnership("profile", "intelligence", "nous_runtime.intelligence.profiles", "profile JSONL store"),
    StateOwnership("reliability", "intelligence", "nous_runtime.intelligence.reliability", "reliability JSONL store"),
    StateOwnership("retrieval", "retrieval", "nous_runtime.retrieval", "retrieval index stores"),
)


def list_state_owners() -> list[StateOwnership]:
    """Return all known state ownership records."""
    return list(STATE_OWNERSHIP)


def get_state_owner(state: str) -> StateOwnership | None:
    """Return the ownership record for a state name."""
    normalized = state.strip().lower()
    for record in STATE_OWNERSHIP:
        if record.state == normalized:
            return record
    return None


def validate_unique_state_owners() -> list[str]:
    """Return duplicate ownership findings."""
    seen: set[str] = set()
    duplicates: list[str] = []
    for record in STATE_OWNERSHIP:
        if record.state in seen:
            duplicates.append(record.state)
        seen.add(record.state)
    return duplicates
