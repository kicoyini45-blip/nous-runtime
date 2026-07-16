# -*- coding: utf-8 -*-
"""
Provider base -re-exports nous_core.provider.Provider.
"""

from __future__ import annotations

from nous_runtime.compat.provider import (
    Provider,
    register_adapter,
    unregister_adapter,
    get_provider,
    list_providers,
    invoke_via_provider,
    invoke_via_provider_observation,
)

__all__ = [
    "Provider",
    "register_adapter",
    "unregister_adapter",
    "get_provider",
    "list_providers",
    "invoke_via_provider",
    "invoke_via_provider_observation",
]
