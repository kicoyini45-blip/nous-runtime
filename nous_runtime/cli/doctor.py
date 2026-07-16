# -*- coding: utf-8 -*-
"""
Environment Detection System -`nous doctor`.

Detects OS, CPU, RAM, disk, Python, network, permissions, dependencies
before installation and at runtime. Provides actionable fix suggestions.
"""

from __future__ import annotations

import importlib.util
import os
import platform
import shutil
import socket
import sys
from dataclasses import dataclass, field


@dataclass
class CheckResult:
    name: str
    status: str        # pass | warn | fail
    value: str = ""
    suggestion: str = ""


@dataclass
class DoctorReport:
    checks: list[CheckResult] = field(default_factory=list)
    passed: int = 0
    warnings: int = 0
    failures: int = 0

    def add(self, check: CheckResult) -> None:
        self.checks.append(check)
        if check.status == "pass":
            self.passed += 1
        elif check.status == "fail":
            self.failures += 1
        else:
            self.warnings += 1

    @property
    def ready(self) -> bool:
        return self.failures == 0


def run_diagnostics() -> DoctorReport:
    """Run full environment diagnostics."""
    report = DoctorReport()

    # Operating System
    system = platform.system()
    if system == "Windows":
        report.add(CheckResult("Operating System", "pass", f"Windows {platform.release()}"))
        report.add(CheckResult("Architecture", "pass", platform.machine()))
    elif system == "Linux":
        report.add(CheckResult("Operating System", "pass", f"Linux {platform.release()}"))
        report.add(CheckResult("Architecture", "pass", platform.machine()))
    elif system == "Darwin":
        report.add(CheckResult("Operating System", "pass", f"macOS {platform.mac_ver()[0]}"))
        report.add(CheckResult("Architecture", "pass", platform.machine()))
    else:
        report.add(CheckResult("Operating System", "warn", system, "May not be fully supported"))

    # Python
    py_ver = sys.version_info
    if py_ver >= (3, 10):
        report.add(CheckResult("Python", "pass", f"{py_ver.major}.{py_ver.minor}.{py_ver.micro}"))
    else:
        report.add(CheckResult("Python", "fail", f"{py_ver.major}.{py_ver.minor}", "Python 3.10+ required"))

    # Python executable
    report.add(CheckResult("Python Path", "pass", sys.executable))

    # Memory
    try:
        import psutil
        mem = psutil.virtual_memory()
        gb = mem.total / (1024**3)
        if gb >= 4:
            report.add(CheckResult("Memory", "pass", f"{gb:.1f} GB"))
        elif gb >= 2:
            report.add(CheckResult("Memory", "warn", f"{gb:.1f} GB", "4GB+ recommended for LLM providers"))
        else:
            report.add(CheckResult("Memory", "fail", f"{gb:.1f} GB", "2GB+ required"))
    except ImportError:
        # Fallback: try to get memory info without psutil
        try:
            total = _get_memory_fallback()
            gb = total / (1024**3)
            report.add(CheckResult("Memory", "pass", f"~{gb:.1f} GB"))
        except Exception:
            report.add(CheckResult("Memory", "warn", "unknown", "Install psutil: pip install psutil"))

    # Disk
    try:
        cwd = os.getcwd()
        usage = shutil.disk_usage(cwd)
        free_gb = usage.free / (1024**3)
        if free_gb >= 1:
            report.add(CheckResult("Disk", "pass", f"{free_gb:.1f} GB free"))
        else:
            report.add(CheckResult("Disk", "fail", f"{free_gb:.1f} GB free", "1GB+ free space required"))
    except Exception:
        report.add(CheckResult("Disk", "warn", "unknown"))

    # Network
    try:
        with socket.create_connection(("8.8.8.8", 53), timeout=3):
            pass
        report.add(CheckResult("Network", "pass", "Connected"))
    except OSError:
        report.add(CheckResult("Network", "warn", "No internet", "Network required for LLM providers"))

    try:
        hostname = socket.gethostname()
        report.add(CheckResult("Hostname", "pass", hostname))
    except Exception:
        pass

    # Permissions
    try:
        test_path = os.path.join(os.getcwd(), ".nous_test_write")
        with open(test_path, "w") as f:
            f.write("test")
        os.remove(test_path)
        report.add(CheckResult("Write Permission", "pass", os.getcwd()))
    except Exception:
        report.add(CheckResult("Write Permission", "fail", os.getcwd(), "Cannot write to current directory"))

    # Dependencies
    for dep, name in [
        ("chromadb", "ChromaDB (vector store)"),
        ("fastembed", "FastEmbed (embeddings)"),
        ("typer", "Typer (CLI)"),
        ("yaml", "PyYAML (config)"),
    ]:
        if importlib.util.find_spec(dep) is not None:
            report.add(CheckResult(name, "pass", "installed"))
        else:
            report.add(CheckResult(name, "warn", "not installed", f"pip install {dep}"))

    # Git
    git = shutil.which("git")
    if git:
        report.add(CheckResult("Git", "pass", git))
    else:
        report.add(CheckResult("Git", "warn", "not found", "Install git for pack management"))

    # Runtime
    try:
        from nous_runtime.version import __version__
        report.add(CheckResult("Runtime", "pass", f"v{__version__}"))
    except Exception:
        report.add(CheckResult("Runtime", "fail", "not found", "Reinstall: pip install nous-runtime"))

    # Workspace
    try:
        from nous_runtime.project.workspace import find_workspace
        ws = find_workspace()
        if ws:
            report.add(CheckResult("Workspace", "pass", str(ws)))
        else:
            report.add(CheckResult("Workspace", "warn", "not found",
                                    "Run: nous project init"))
    except Exception:
        report.add(CheckResult("Workspace", "warn", "error", "Check .nous/ directory"))

    # Project
    try:
        if ws:
            from nous_runtime.project.workspace import read_project_config
            cfg = read_project_config(ws)
            report.add(CheckResult("Project", "pass", cfg.get("name", os.path.basename(os.getcwd()))))
        else:
            report.add(CheckResult("Project", "warn", os.path.basename(os.getcwd()),
                                    "Create .nous/ for project features"))
    except Exception:
        report.add(CheckResult("Project", "warn", os.path.basename(os.getcwd())))

    # Provider
    try:
        from nous_runtime.cli.provider_setup import load_providers_from_config
        load_providers_from_config()
        from nous_runtime.services.providers import list_provider_summaries
        provs = list_provider_summaries()
        if provs:
            names = ", ".join(p.get("name", "?") for p in provs)
            report.add(CheckResult("Provider", "pass", names))
        else:
            report.add(CheckResult("Provider", "warn", "none configured",
                                    "Run: nous provider setup"))
    except Exception as e:
        report.add(CheckResult("Provider", "warn", str(e)[:40],
                                "Run: nous provider setup"))

    # Memory
    try:
        if ws:
            from nous_runtime.project.memory import read_all
            events = read_all(str(ws), "timeline")
            report.add(CheckResult("Memory", "pass", f"{len(events)} timeline events"))
        else:
            report.add(CheckResult("Memory", "warn", "no workspace"))
    except Exception:
        report.add(CheckResult("Memory", "warn", "unavailable"))

    # Capabilities
    try:
        from nous_runtime.services.capabilities import list_capabilities
        caps = list_capabilities()
        report.add(CheckResult("Capabilities", "pass", f"{len(caps)} loaded"))
    except Exception:
        report.add(CheckResult("Capabilities", "fail", "error",
                                "DB may need initialization"))

    # Environment
    env_healthy = True
    if not os.environ.get("NOUS_LLM_API_KEY"):
        env_healthy = False
    if env_healthy:
        report.add(CheckResult("Environment", "pass", "healthy"))
    else:
        report.add(CheckResult("Environment", "warn", "API key not set",
                                "Run: nous provider setup"))

    return report


def _get_memory_fallback() -> int:
    """Get total memory without psutil."""
    system = platform.system()
    if system == "Linux":
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    return int(line.split()[1]) * 1024  # kB ->bytes
    elif system == "Windows":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                        ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                        ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong)]
        ms = MEMORYSTATUSEX()
        ms.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        kernel32.GlobalMemoryStatusEx(ctypes.byref(ms))
        return ms.ullTotalPhys
    raise NotImplementedError(f"Memory detection not supported on {system}")


def format_report(report: DoctorReport) -> str:
    """Format a doctor report for terminal display."""
    lines = ["", "Nous Environment Check", "-" * 30, ""]
    for c in report.checks:
        icon = {"pass": "PASS", "warn": "WARN", "fail": "FAIL"}.get(c.status, "UNKNOWN")
        lines.append(f"  {icon} {c.name}: {c.value}")
        if c.suggestion:
            lines.append(f"    suggestion: {c.suggestion}")
    lines.append("")
    lines.append(f"  Passed: {report.passed}  Warnings: {report.warnings}  Failures: {report.failures}")
    if report.ready:
        lines.append("  Status: Ready")
    else:
        lines.append("  Status: Not ready - fix failures above")
    return "\n".join(lines)
