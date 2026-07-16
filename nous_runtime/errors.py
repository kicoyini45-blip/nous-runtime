"""Public exception hierarchy for Nous Runtime."""

from __future__ import annotations


class NousError(Exception):
    """Base class for public Nous Runtime errors."""


class NousRuntimeError(NousError):
    """Raised when runtime execution cannot proceed."""


class GovernanceError(NousError):
    """Raised when an operation is not authorized or cannot be audited."""


class ContextError(NousError):
    """Raised when context loading, packing, or restoration fails."""


class AgentError(NousError):
    """Raised when an agent cannot register, bind, or execute."""


class DeploymentError(NousError):
    """Raised when deployment, packaging, or platform validation fails."""


__all__ = [
    "AgentError",
    "ContextError",
    "DeploymentError",
    "GovernanceError",
    "NousError",
    "NousRuntimeError",
]
