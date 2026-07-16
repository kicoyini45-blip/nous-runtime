# -*- coding: utf-8 -*-
"""Cross-Platform Runtime — unified interface for Linux, Windows, macOS, ARM, Jetson."""
from nous_runtime.platform.adapter import get_platform_adapter, PlatformAdapter
__all__ = ["get_platform_adapter", "PlatformAdapter"]
