# -*- coding: utf-8 -*-
"""
Nous Runtime Governance — B1 authorization foundation.

Public API:
  - get_gate() — singleton ExecutionAuthorizationGate
  - get_store() — singleton GovernanceStore
  - All canonical contracts (AuthorizationContext, ActionProposal, etc.)
  - ApprovalManager, LeaseManager, DelegationManager
"""

from nous_runtime.governance.contracts import (
    ActionProposal,
    ApprovalRequest,
    ApprovalResponse,
    ApprovalScope,
    AuthorizationContext,
    AuthorizationDecision,
    AuthorizationEvidenceBundle,
    AuthorizationLease,
    DelegationConstraint,
    DelegationGrant,
    EscalationRecord,
    RevocationRecord,
    RiskAssessment,
    RiskEnvelope,
)
from nous_runtime.governance.gate import ExecutionAuthorizationGate, get_gate
from nous_runtime.governance.store import GovernanceStore
from nous_runtime.governance.enterprise import (
    EnterprisePolicyInterface,
    OrganizationMembership,
)
from nous_runtime.governance.approval import ApprovalManager
from nous_runtime.governance.lease import LeaseManager
from nous_runtime.governance.delegation import DelegationManager
from nous_runtime.governance.runtime_mode import (
    GovernanceRuntimeMode,
    mode_policy,
    resolve_runtime_mode,
    should_fail_closed,
)

__all__ = [
    # Gate
    "ExecutionAuthorizationGate",
    "get_gate",
    # Store
    "GovernanceStore",
    # Contracts
    "ActionProposal",
    "AuthorizationContext",
    "AuthorizationDecision",
    "ApprovalRequest",
    "ApprovalResponse",
    "ApprovalScope",
    "AuthorizationLease",
    "DelegationGrant",
    "DelegationConstraint",
    "RevocationRecord",
    "EscalationRecord",
    "RiskEnvelope",
    "RiskAssessment",
    "AuthorizationEvidenceBundle",
    "EnterprisePolicyInterface",
    "OrganizationMembership",
    # Managers
    "ApprovalManager",
    "LeaseManager",
    "DelegationManager",
    "GovernanceRuntimeMode",
    "mode_policy",
    "resolve_runtime_mode",
    "should_fail_closed",
]
