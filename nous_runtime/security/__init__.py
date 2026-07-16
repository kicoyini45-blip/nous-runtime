# -*- coding: utf-8 -*-
"""
Security module -wraps nous_core.security with a clean public API.
"""

from __future__ import annotations

from nous_runtime.compat.security import (
    check_risk,
    check_module_permission,
    register_module_permissions,
    check_rate_limit,
    record_security_event,
    get_security_stats,
)

__all__ = [
    "check_risk",
    "check_module_permission",
    "register_module_permissions",
    "check_rate_limit",
    "record_security_event",
    "get_security_stats",
]
