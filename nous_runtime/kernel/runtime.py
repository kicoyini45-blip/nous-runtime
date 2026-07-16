# -*- coding: utf-8 -*-
"""
Nous Runtime lifecycle management.

The Runtime class provides the programmatic entry point for starting,
stopping, and querying the Nous Runtime. It wraps the initialization
sequence from brain.py's main() so that other entry points can start the
runtime without importing brain.py directly.
"""

from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field
from typing import Any

log = logging.getLogger("nous.runtime")


@dataclass
class RuntimeStatus:
    """Snapshot of runtime health."""
    running: bool = False
    version: str = __import__("nous_runtime.version", fromlist=["__version__"]).__version__
    uptime_seconds: float = 0.0
    providers: int = 0
    capabilities: int = 0
    packs: int = 0
    devices: int = 0
    events_total: int = 0
    jobs_pending: int = 0
    demo_mode: bool = False
    errors: list[str] = field(default_factory=list)


class Runtime:
    """
    Nous Runtime lifecycle manager.

    start() initializes database migrations, event dispatching, capability
    seeding, automation rules, device sync, and stale job recovery.
    """

    def __init__(self):
        self._started = False
        self._start_time: float = 0.0
        self._status = RuntimeStatus()

    def start(self, demo_mode: bool = False, config_overrides: dict[str, Any] | None = None) -> RuntimeStatus:
        """Initialize the Nous Runtime kernel."""
        if self._started:
            log.warning("Runtime already started")
            return self._status

        errors: list[str] = []
        self._start_time = time.time()

        if demo_mode or os.environ.get("NOUS_DEMO_MODE") == "1":
            self._enable_demo()
            self._status.demo_mode = True

        try:
            from nous_runtime.services.lifecycle import run_migrations

            run_migrations()
            log.info("Kernel migrations applied")
        except Exception as e:
            errors.append(f"migrations: {e}")
            log.error("Migration failed: %s", e)

        try:
            from nous_runtime.services.lifecycle import seed_capabilities

            n = seed_capabilities()
            self._status.capabilities = n
            log.info("Capabilities seeded: %d", n)
        except Exception as e:
            errors.append(f"capabilities: {e}")
            log.error("Capability seeding failed: %s", e)

        try:
            from nous_runtime.services.lifecycle import (
                count_automation_rules,
                start_event_dispatcher,
            )

            start_event_dispatcher(interval=5.0)
            try:
                self._status.packs = count_automation_rules()
            except Exception as e:
                errors.append(f"automation: {e}")
            log.info("Event dispatcher started")
        except Exception as e:
            errors.append(f"dispatcher: {e}")
            log.error("Dispatcher failed: %s", e)

        try:
            from nous_runtime.services.lifecycle import sync_legacy_devices

            self._status.devices = sync_legacy_devices()
        except Exception as e:
            errors.append(f"devices: {e}")

        try:
            from nous_runtime.services.lifecycle import recover_stale_jobs

            n = recover_stale_jobs()
            if n:
                log.info("Recovered %d stale jobs", n)
        except Exception as e:
            errors.append(f"jobs: {e}")

        self._status.running = True
        self._status.uptime_seconds = 0.0
        self._status.errors = errors
        self._status.providers = self._count_providers()
        self._status.events_total = self._count_events()
        self._status.jobs_pending = self._count_pending_jobs()

        self._started = True
        if errors:
            log.warning("Runtime started with %d errors: %s", len(errors), errors)
        else:
            log.info("Nous Runtime v%s started successfully", self._status.version)
        return self._status

    def stop(self) -> None:
        """Gracefully stop the runtime."""
        if not self._started:
            return
        try:
            from nous_runtime.services.lifecycle import stop_event_dispatcher

            stop_event_dispatcher()
        except Exception:
            pass
        self._started = False
        self._status.running = False
        log.info("Runtime stopped")

    def status(self) -> RuntimeStatus:
        """Return a current snapshot of runtime health."""
        self._status.providers = self._count_providers()
        self._status.capabilities = self._count_capabilities()
        self._status.devices = self._count_devices()
        self._status.events_total = self._count_events()
        self._status.jobs_pending = self._count_pending_jobs()
        if self._started:
            self._status.uptime_seconds = time.time() - self._start_time
        return self._status

    def _enable_demo(self) -> None:
        try:
            from nous_runtime.services.lifecycle import enable_demo_mode

            enable_demo_mode()
        except Exception:
            pass

    @staticmethod
    def _count_providers() -> int:
        try:
            from nous_runtime.services.lifecycle import count_providers

            return count_providers()
        except Exception:
            return 0

    @staticmethod
    def _count_capabilities() -> int:
        try:
            from nous_runtime.services.lifecycle import count_capabilities

            return count_capabilities()
        except Exception:
            return 0

    @staticmethod
    def _count_devices() -> int:
        try:
            from nous_runtime.services.lifecycle import count_devices

            return count_devices()
        except Exception:
            return 0

    @staticmethod
    def _count_events() -> int:
        try:
            from nous_runtime.services.lifecycle import count_events

            return count_events()
        except Exception:
            return 0

    @staticmethod
    def _count_pending_jobs() -> int:
        try:
            from nous_runtime.services.lifecycle import count_pending_jobs

            return count_pending_jobs()
        except Exception:
            return 0

    @staticmethod
    def _count_automation_rules() -> int:
        try:
            from nous_runtime.services.lifecycle import count_automation_rules

            return count_automation_rules()
        except Exception:
            return 0
