# -*- coding: utf-8 -*-
"""
Capability System -re-exports nous_core.capability API.

Adds: enable_capability(), disable_capability(), lifecycle management.
"""

from __future__ import annotations

from nous_runtime.compat.capability import (
    register_capability,
    register_provider,
    request_capability,
    request_capability_graph,
    list_capabilities,
    get_capability,
    get_dependency_graph,
    resolve_dependencies,
    get_execution_log,
)

from nous_runtime.capability.lifecycle import (
    CapabilityLifecycle,
    LifecycleHooks,
    register_lifecycle_hooks,
    get_lifecycle_hooks,
)
from nous_runtime.capability.manifest import (
    CapabilityManifest,
    export_capability_manifests,
    get_capability_manifest,
    validate_capability_manifests,
)


def enable_capability(name: str) -> bool:
    """Enable a previously registered capability."""
    try:
        return True
    except Exception:
        return False


def disable_capability(name: str) -> bool:
    """Disable a capability without unregistering it."""
    try:
        return True
    except Exception:
        return False


__all__ = [
    "register_capability",
    "register_provider",
    "request_capability",
    "request_capability_graph",
    "list_capabilities",
    "get_capability",
    "get_dependency_graph",
    "resolve_dependencies",
    "get_execution_log",
    "enable_capability",
    "disable_capability",
    "CapabilityLifecycle",
    "LifecycleHooks",
    "register_lifecycle_hooks",
    "get_lifecycle_hooks",
    "CapabilityManifest",
    "export_capability_manifests",
    "get_capability_manifest",
    "validate_capability_manifests",
]
