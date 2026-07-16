"""Plugin package integrity and optional signature boundaries."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Protocol

from nous_runtime.plugins.models import PluginManifest


class SignatureVerifier(Protocol):
    def verify(self, payload_digest: str, signature: str) -> bool: ...


def package_checksum(root: str | Path, manifest: PluginManifest) -> str:
    package = Path(root).resolve()
    digest = hashlib.sha256()
    public_manifest = manifest.to_dict()
    public_manifest["package_checksum"] = ""
    public_manifest["signature"] = ""
    digest.update(json.dumps(public_manifest, sort_keys=True, separators=(",", ":")).encode())
    for path in sorted(item for item in package.rglob("*") if item.is_file() and item.name != "plugin.json"):
        relative = path.relative_to(package).as_posix()
        if relative.startswith(".nous/") or "__pycache__" in path.parts:
            continue
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
    return digest.hexdigest()


def validate_package(root: str | Path, manifest: PluginManifest, *, verifier: SignatureVerifier | None = None) -> list[str]:
    errors = manifest.validate()
    calculated = package_checksum(root, manifest)
    if not manifest.package_checksum:
        errors.append("package_checksum is required")
    elif manifest.package_checksum != calculated:
        errors.append("package checksum mismatch")
    if manifest.signature:
        if verifier is None:
            errors.append("signature is present but no verifier is configured")
        elif not verifier.verify(calculated, manifest.signature):
            errors.append("plugin signature verification failed")
    return errors
