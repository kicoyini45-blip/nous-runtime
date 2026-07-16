# -*- coding: utf-8 -*-
"""Context Runtime schema — enums, constants, schema version."""

from __future__ import annotations

from enum import Enum

# Bump when model shape changes; used for migration checks.
CONTEXT_SCHEMA_VERSION = "1.0.0"


class ContextSource(str, Enum):
    """Canonical sources of context data.

    Context reads FROM these sources; it does not own them.
    """

    MEMORY = "memory"
    PROJECT = "project"
    AGENT = "agent"
    DEVICE = "device"
    DECISION = "decision"
    RETRIEVAL = "retrieval"
    EXPERIENCE = "experience"
    RUNTIME = "runtime"


class SnapshotStatus(str, Enum):
    """Lifecycle status of a ContextSnapshot."""

    ACTIVE = "active"        # Currently in use
    ARCHIVED = "archived"    # Historical, kept for audit
    RESTORED = "restored"    # Was restored from a previous session
    STALE = "stale"          # Expired, pending cleanup
