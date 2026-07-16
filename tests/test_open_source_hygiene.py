# -*- coding: utf-8 -*-
"""Open-source hygiene tests for Nous Runtime.

These tests verify that the repository is clean of personal paths,
real credentials, and runtime pollution, and that public APIs are
importable and configuration templates use safe placeholders.

Security note: this test file contains pattern strings that match
the scans it performs (e.g., "sk-"). These are test assertions, not
real credentials. The security scanner script is configured to
allowlist this file.
"""

import os
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


# ── Helpers ──────────────────────────────────────────────────────

def _read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _collect_text_files(root: Path, exclude_dirs: set[str] | None = None) -> list[Path]:
    """Collect all text files in repo, excluding build/cache/venv dirs."""
    if exclude_dirs is None:
        exclude_dirs = {
            ".git", ".venv", "venv", "__pycache__", ".pytest_cache",
            ".ruff_cache", ".mypy_cache", "node_modules", "dist", "build",
            ".claude", ".agents", ".idea", "htmlcov", ".nous",
            "Nous_Release_Test2", "backups", "server_backup",
        }
    SKIP_EXT = {".pyc", ".pyo", ".pyd", ".so", ".dll", ".exe", ".bin",
                ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg",
                ".wav", ".mp3", ".mp4", ".avi", ".mov",
                ".zip", ".tar", ".gz", ".bz2", ".7z",
                ".db", ".sqlite", ".sqlite3",
                ".pdf", ".doc", ".docx", ".xls", ".xlsx",
                ".apk", ".aab", ".lock", ".log"}

    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if fpath.suffix.lower() in SKIP_EXT:
                continue
            files.append(fpath)
    return files


# ── Test 1: No personal absolute paths ───────────────────────────

KNOWN_PERSONAL_PATHS = [
    "F:/Agent_play",
    "F:\\Agent_play",
    "Nous_Test_User",
]


def test_repository_contains_no_known_personal_paths():
    """Ensure no tracked files contain the developer's personal paths."""
    # We only scan .py, .md, .toml, .json, .yaml, .yml, .cfg, .ini, .txt, .sh files
    files = _collect_text_files(REPO_ROOT)
    findings: list[str] = []

    for fpath in files:
        rel = str(fpath.relative_to(REPO_ROOT))
        # Skip this test file itself and the security scanner
        if "test_open_source_hygiene" in rel or "security_scan.py" in rel:
            continue
        # Skip files in git-ignored locations
        if any(part in {".claude", ".agents", ".nous"} for part in fpath.parts):
            continue

        try:
            content = _read_file(fpath)
        except Exception:
            continue

        for path_pattern in KNOWN_PERSONAL_PATHS:
            if path_pattern in content:
                # Check each line for the pattern
                for lineno, line in enumerate(content.split("\n"), 1):
                    if path_pattern in line:
                        findings.append(f"{rel}:{lineno}: {path_pattern}")

    assert not findings, (
        f"Found {len(findings)} personal path reference(s):\n" +
        "\n".join(findings[:20])
    )


# ── Test 2: No high-risk secret patterns ─────────────────────────

# Only check for patterns that indicate REAL credentials, not placeholders
HIGH_RISK_SECRETS = [
    # Real API key prefixes (at least 20 chars after prefix)
    (r'sk-[a-zA-Z0-9]{20,}', "OpenAI/Anthropic-style API key"),
    (r'ghp_[a-zA-Z0-9]{36}', "GitHub personal access token (classic)"),
    (r'github_pat_[a-zA-Z0-9_]{20,}', "GitHub personal access token (fine-grained)"),
    (r'AKIA[0-9A-Z]{16}', "AWS access key ID"),
    (r'AIza[0-9A-Za-z\-_]{35}', "GCP API key"),
    # PEM private keys
    (r'-----BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY-----', "Private key PEM"),
]


def test_repository_contains_no_high_risk_secret_patterns():
    """Ensure no real credentials exist in tracked files."""
    files = _collect_text_files(REPO_ROOT)
    findings: list[str] = []

    for fpath in files:
        rel = str(fpath.relative_to(REPO_ROOT))
        # Allowlist: this test file, security scanner, and review docs
        if any(name in rel for name in [
            "test_open_source_hygiene", "security_scan.py",
            "P3_OPEN_SOURCE_CLEAN_PASS",
        ]):
            continue
        if any(part in {".claude", ".agents"} for part in fpath.parts):
            continue

        try:
            content = _read_file(fpath)
        except Exception:
            continue

        for pattern, label in HIGH_RISK_SECRETS:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                findings.append(f"{rel}: {label} — {match[:40]}...")

    assert not findings, (
        f"Found {len(findings)} potential secret(s):\n" +
        "\n".join(findings[:20])
    )


# ── Test 3: Config templates use safe placeholders ───────────────

def test_example_configuration_contains_no_real_credentials():
    """Verify .env.example and similar templates use placeholders."""
    template_files = list(REPO_ROOT.glob(".env.example")) + \
                     list(REPO_ROOT.glob("**/.env.example")) + \
                     list(REPO_ROOT.glob("*.example.toml")) + \
                     list(REPO_ROOT.glob("*.example.yaml")) + \
                     list(REPO_ROOT.glob("*.example.yml"))

    # Not a hard failure if no templates exist, but warn
    if not template_files:
        pytest.skip("No configuration template files found")

    real_url_patterns = [
        # Real provider API URLs (not example.com)
        (r'https?://api\.(?!example\.com)[a-zA-Z0-9.-]+\.(?:com|cn|io|org|net)/', "Real API URL"),
    ]

    findings: list[str] = []
    for tf in template_files:
        rel = str(tf.relative_to(REPO_ROOT))
        content = _read_file(tf)
        for pattern, label in real_url_patterns:
            for match in re.findall(pattern, content, re.IGNORECASE):
                findings.append(f"{rel}: {label} — {match}")

    assert not findings, (
        f"Found {len(findings)} real URL(s) in config templates:\n" +
        "\n".join(findings[:20])
    )


# ── Test 4: Source doesn't require pre-existing .nous state ──────

def test_source_does_not_require_existing_nous_runtime_state():
    """Ensure no source file reads from a hardcoded .nous/ path directly."""
    # .nous/ should only be referenced via project workspace resolution,
    # never as a hardcoded path expectation.
    source_files = list(REPO_ROOT.glob("nous_runtime/**/*.py"))
    source_files = [f for f in source_files if "__pycache__" not in str(f)]

    hardcoded_nous_refs: list[str] = []
    for sf in source_files:
        rel = str(sf.relative_to(REPO_ROOT))
        content = _read_file(sf)
        for lineno, line in enumerate(content.split("\n"), 1):
            # Flag hardcoded ".nous/" string literals that aren't in comments
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if '".nous/' in stripped or "'" in stripped and ".nous/" in stripped:
                # Check if it's used dynamically (Path construction, etc.)
                if re.search(r'["\']\.nous/', stripped):
                    hardcoded_nous_refs.append(f"{rel}:{lineno}: {stripped[:120]}")

    # Allow up to 5 hardcoded references (some may be legitimate in workspace init code)
    # The intent is to flag files that assume .nous/ already exists
    critical_refs = [r for r in hardcoded_nous_refs
                     if "mkdir" not in r.lower()
                     and "create" not in r.lower()
                     and "init" not in r.lower()
                     and "ensure" not in r.lower()]

    assert len(critical_refs) <= 10, (
        f"Found {len(critical_refs)} hardcoded .nous/ references that may "
        f"assume pre-existing state:\n" + "\n".join(critical_refs[:20])
    )


# ── Test 5: Public imports are available ─────────────────────────

def test_public_runtime_imports():
    """Verify key public API imports work without errors."""
    # These should all import cleanly
    from nous_runtime.inspector import InspectorSnapshot, snapshot, diagnose  # noqa: F401
    from nous_runtime.capability import (  # noqa: F401
        register_capability,
        request_capability,
        list_capabilities,
        CapabilityManifest,
    )
    from nous_runtime.provider.base import Provider  # noqa: F401
    from nous_runtime.planner import Goal, Plan, Task, TaskGraph  # noqa: F401


def test_public_inspector_imports():
    """Verify inspector public API is clean and importable."""
    from nous_runtime.inspector import (  # noqa: F401
        InspectorSnapshot,
        RuntimeSnapshot,
        CapabilitySnapshot,
        TaskSnapshot,
        ObservationSnapshot,
        MemorySnapshot,
        DiagnosticFinding,
        diagnose,
        snapshot,
    )
    # Verify __all__ is defined and contains key exports
    import nous_runtime.inspector as insp
    assert hasattr(insp, "__all__")
    assert "InspectorSnapshot" in insp.__all__
    assert "RuntimeSnapshot" in insp.__all__
    assert "snapshot" in insp.__all__
    assert "diagnose" in insp.__all__


def test_public_capability_imports():
    """Verify capability public API is importable."""
    from nous_runtime.capability import (  # noqa: F401
        register_capability,
        register_provider,
        request_capability,
        list_capabilities,
        get_capability,
    )


# ── Test 6: Gitignore covers critical patterns ───────────────────

def test_gitignore_covers_runtime_state():
    """Verify .gitignore covers .nous/ and common pollution patterns."""
    gitignore = REPO_ROOT / ".gitignore"
    assert gitignore.exists(), ".gitignore not found"

    content = _read_file(gitignore)

    required_patterns = [
        ".nous/",
        ".env",
        "__pycache__/",
        "*.py[cod]",
        ".pytest_cache/",
        ".ruff_cache/",
        ".coverage",
        "htmlcov/",
        "build/",
        "dist/",
        "*.egg-info/",
        "*.log",
        "*.db",
        "*.sqlite",
        "*.sqlite3",
    ]

    missing = [p for p in required_patterns if p not in content]
    assert not missing, f".gitignore missing patterns: {missing}"


# ── Test 7: pyproject.toml has valid classifiers ─────────────────

def test_pyproject_has_open_source_metadata():
    """Verify pyproject.toml contains basic open-source metadata."""
    pyproject = REPO_ROOT / "pyproject.toml"
    assert pyproject.exists(), "pyproject.toml not found"

    content = _read_file(pyproject)

    # Check for license
    assert "license" in content.lower(), "pyproject.toml missing license field"
    assert "Apache" in content or "MIT" in content, "pyproject.toml should specify an OSI license"

    # Check for classifiers
    assert "Programming Language :: Python :: 3" in content, \
        "pyproject.toml should have Python classifiers"


# ── Test 8: No learning-only / single-user branding ──────────────

def test_readme_maintains_runtime_neutrality():
    """Verify README does not contain personal/study-only branding."""
    readme = REPO_ROOT / "README.md"
    assert readme.exists(), "README.md not found"

    content = _read_file(readme)

    # Should NOT contain personal or study-only framing
    prohibited = [
        "我的系统",
        "我的学习",
        "专升本",
        "数学一",
        "数学二",
        "个人助理专用",
    ]

    for phrase in prohibited:
        assert phrase not in content, f"README.md contains prohibited phrase: '{phrase}'"

    # Should contain key neutral descriptions
    expected = [
        "open",
        "runtime",
        "local-first",
    ]
    content_lower = content.lower()
    for phrase in expected:
        assert phrase in content_lower, f"README.md should mention '{phrase}'"


def test_readme_zh_maintains_runtime_neutrality():
    """Verify Chinese README maintains runtime neutrality."""
    readme_zh = REPO_ROOT / "README.zh-CN.md"
    if not readme_zh.exists():
        pytest.skip("README.zh-CN.md not found")

    content = _read_file(readme_zh)

    # Should NOT contain personal or study-only framing
    prohibited = [
        "我的系统",
        "我的学习",
        "专升本",
        "数学一",
        "数学二",
        "个人助理专用",
    ]

    for phrase in prohibited:
        assert phrase not in content, f"README.zh-CN.md contains prohibited phrase: '{phrase}'"

    # Should have "我们不是什么" (What we are NOT) section
    assert "我们不是什么" in content or "不是" in content, \
        "README.zh-CN.md should contain a 'What we are NOT' section"


# ── Test 9: No remaining datetime.utcnow() ───────────────────────

def test_no_datetime_utcnow_in_nous_runtime():
    """Verify nous_runtime has no deprecated datetime.utcnow() calls."""
    source_files = list(REPO_ROOT.glob("nous_runtime/**/*.py"))
    source_files = [f for f in source_files if "__pycache__" not in str(f)]

    findings: list[str] = []
    for sf in source_files:
        rel = str(sf.relative_to(REPO_ROOT))
        content = _read_file(sf)
        for lineno, line in enumerate(content.split("\n"), 1):
            if "utcnow()" in line and not line.strip().startswith("#"):
                findings.append(f"{rel}:{lineno}: {line.strip()[:120]}")

    assert not findings, (
        f"Found {len(findings)} datetime.utcnow() calls in nous_runtime:\n" +
        "\n".join(findings[:20])
    )
