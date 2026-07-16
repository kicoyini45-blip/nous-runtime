# -*- coding: utf-8 -*-
"""
Unified configuration for the Nous Runtime.

Loads configuration from the same sources as remote_terminal/config.py:
  1. Environment variables (NOUS_* prefix)
  2. config.local.json (local overrides)
  3. Python defaults

This module wraps remote_terminal.config to provide a consistent API
for both brain.py and nous_runtime consumers.
"""

from __future__ import annotations

import os
import json
from typing import Any


def _find_project_root() -> str:
    """Find the project root directory (containing remote_terminal/ or nous_runtime/)."""
    # Start from this file's location and walk up
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        if os.path.isdir(os.path.join(current, "remote_terminal")):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    return os.getcwd()


PROJECT_ROOT = _find_project_root()


def get(key: str, default: Any = None) -> Any:
    """
    Get a configuration value.

    Priority: env NOUS_{KEY} > config.local.json > default.

    Args:
        key: Config key name (e.g., "BRAIN_HOST", "LLM_MODEL").
        default: Fallback value if not found anywhere.

    Returns:
        The resolved config value.
    """
    # 1. Environment variable
    env_val = os.environ.get(f"NOUS_{key}")
    if env_val is not None:
        return _cast(env_val)

    # 2. config.local.json
    try:
        config_path = os.path.join(PROJECT_ROOT, "remote_terminal", "config.local.json")
        if os.path.isfile(config_path):
            with open(config_path, encoding="utf-8") as f:
                local = json.load(f)
            if key in local:
                return local[key]
    except Exception:
        pass

    # 3. Default
    return default


def get_bool(key: str, default: bool = False) -> bool:
    """Get a boolean config value."""
    val = get(key, str(default).lower())
    if isinstance(val, bool):
        return val
    return str(val).lower() in ("1", "true", "yes", "on")


def get_int(key: str, default: int = 0) -> int:
    """Get an integer config value."""
    try:
        return int(get(key, str(default)))
    except (ValueError, TypeError):
        return default


def _cast(value: str) -> Any:
    """Cast a string to the most appropriate Python type."""
    if value.lower() in ("true", "yes", "on"):
        return True
    if value.lower() in ("false", "no", "off"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value
