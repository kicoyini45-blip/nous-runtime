"""Compatibility adapter for legacy provider registry and base class."""

from remote_terminal.nous_core import provider as _legacy_provider
from remote_terminal.nous_core.provider import *  # noqa: F403

_providers = _legacy_provider._providers
