from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_kernel_runtime_uses_lifecycle_service_boundary():
    path = REPO_ROOT / "nous_runtime" / "kernel" / "runtime.py"
    text = path.read_text(encoding="utf-8", errors="replace")

    assert "nous_runtime.compat" not in text
    assert "remote_terminal." not in text
    assert "nous_runtime.services.lifecycle" in text
