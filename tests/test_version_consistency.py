# -*- coding: utf-8 -*-
"""Version consistency tests — single source of truth."""

import re
import os


def test_version_module_exists():
    """version.py must exist and export __version__."""
    from nous_runtime.version import __version__
    assert __version__
    assert re.match(r"^\d+\.\d+\.\d+((\.dev\d+)|(a\d+))?$", __version__), f"Invalid semver: {__version__}"


def test_init_imports_from_version():
    """nous_runtime.__version__ must come from nous_runtime.version."""
    from nous_runtime import __version__ as init_ver
    from nous_runtime.version import __version__ as src_ver
    assert init_ver == src_ver, f"Init: {init_ver} != Source: {src_ver}"


def test_pyproject_toml_consistent():
    """pyproject.toml version must match nous_runtime.version."""
    from nous_runtime.version import __version__

    # Read pyproject.toml
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    toml_path = os.path.join(root, "pyproject.toml")
    if not os.path.isfile(toml_path):
        return  # Skip if not found

    with open(toml_path, encoding="utf-8") as f:
        content = f.read()

    # Find version in toml
    match = re.search(r'version\s*=\s*"(\d+\.\d+\.\d+(?:(?:\.dev\d+)|(?:a\d+))?)"', content)
    if match:
        toml_ver = match.group(1)
        assert toml_ver == __version__, f"pyproject.toml: {toml_ver} != version.py: {__version__}"


def test_no_hardcoded_versions_in_cli():
    """CLI files must not hardcode version strings."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cli_dir = os.path.join(root, "nous_runtime", "cli")

    for filename in ["main.py", "shell_v2.py", "wizard.py"]:
        path = os.path.join(cli_dir, filename)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()

        # These files import _V from nous_runtime.version
        assert "from nous_runtime.version import __version__" in content or \
               "from nous_runtime.version import __version__ as _V" in content, \
               f"{filename}: missing version import"

        # Should NOT contain hardcoded "v1.0.0" or "v1.1.0" (except in import)
        lines = [
            line for line in content.split("\n")
            if "version" not in line.lower() and "import" not in line
        ]
        hardcoded = [
            line for line in lines
            if re.search(r'"v\d+\.\d+\.\d+"', line)
            or re.search(r"'v\d+\.\d+\.\d+'", line)
        ]
        assert not hardcoded, f"{filename}: hardcoded version found: {hardcoded}"
