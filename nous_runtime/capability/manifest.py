# -*- coding: utf-8 -*-
"""Capability Manifest helpers.

The manifest is the open, stable contract for a capability. It is derived
from the runtime capability registry and can be exported for docs, packs,
devices, and runtime inspection without exposing local configuration.
"""

from __future__ import annotations

import json as _json
import re as _re
from dataclasses import dataclass, field
from typing import Any

SCHEMA_VERSION = "1.0"
RISK_LEVELS = {"low", "medium", "high", "critical"}
_CAPABILITY_ID_RE = _re.compile(r"^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$")


@dataclass
class CapabilityManifest:
    """Stable capability contract exported by the Runtime."""

    capability_id: str
    category: str = ""
    description: str = ""
    provider: str = ""
    risk_level: str = "low"
    version: str = "1.0.0"
    input_schema: dict[str, Any] = field(default_factory=dict)
    output_schema: dict[str, Any] = field(default_factory=dict)
    timeout_ms: int = 30000
    max_retries: int = 1
    requires_approval: bool = False
    requires_auth: bool = False
    requires_device: bool = False
    depends_on: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    availability: str = "unknown"
    unavailable_reason: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_capability(cls, cap: dict[str, Any], availability: dict[str, str] | None = None) -> "CapabilityManifest":
        """Build a manifest from a capability registry row."""
        metadata = _coerce_dict(cap.get("metadata", {}))
        risk = str(cap.get("risk_level", cap.get("risk", "low")) or "low")
        availability = availability or {}
        tags = metadata.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        if not isinstance(tags, list):
            tags = []

        return cls(
            capability_id=str(cap.get("capability_id", cap.get("name", ""))),
            category=str(cap.get("category", "")),
            description=str(cap.get("description", "")),
            provider=str(cap.get("provider", "")),
            risk_level=risk,
            version=str(metadata.get("version", "1.0.0")),
            input_schema=_coerce_schema(metadata.get("input_schema")),
            output_schema=_coerce_schema(metadata.get("output_schema")),
            timeout_ms=int(cap.get("timeout_ms", metadata.get("timeout_ms", 30000)) or 30000),
            max_retries=int(cap.get("max_retries", metadata.get("max_retries", 1)) or 1),
            requires_approval=bool(metadata.get("requires_approval", risk in {"high", "critical"})),
            requires_auth=bool(cap.get("requires_auth", metadata.get("requires_auth", False))),
            requires_device=bool(cap.get("requires_device", metadata.get("requires_device", False))),
            depends_on=_coerce_list(cap.get("depends_on", metadata.get("depends_on", []))),
            tags=[str(t) for t in tags],
            availability=availability.get("status", "unknown"),
            unavailable_reason=availability.get("reason", ""),
            metadata=_public_metadata(metadata),
        )

    def validate(self) -> list[str]:
        """Return validation errors for this manifest."""
        errors: list[str] = []
        if not _CAPABILITY_ID_RE.match(self.capability_id):
            errors.append(f"invalid capability_id: {self.capability_id}")
        if self.risk_level not in RISK_LEVELS:
            errors.append(f"invalid risk_level: {self.risk_level}")
        if self.timeout_ms <= 0 or self.timeout_ms > 600000:
            errors.append("timeout_ms must be > 0 and <= 600000")
        if not isinstance(self.input_schema, dict):
            errors.append("input_schema must be an object")
        if not isinstance(self.output_schema, dict):
            errors.append("output_schema must be an object")
        for dep in self.depends_on:
            if not _CAPABILITY_ID_RE.match(dep):
                errors.append(f"invalid depends_on capability_id: {dep}")
        return errors

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "capability_id": self.capability_id,
            "version": self.version,
            "category": self.category,
            "description": self.description,
            "provider": self.provider,
            "risk_level": self.risk_level,
            "input_schema": self.input_schema,
            "output_schema": self.output_schema,
            "timeout_ms": self.timeout_ms,
            "max_retries": self.max_retries,
            "requires_approval": self.requires_approval,
            "requires_auth": self.requires_auth,
            "requires_device": self.requires_device,
            "depends_on": self.depends_on,
            "tags": self.tags,
            "availability": self.availability,
            "unavailable_reason": self.unavailable_reason,
            "metadata": self.metadata,
        }


def get_capability_manifest(capability_id: str, include_availability: bool = True) -> CapabilityManifest | None:
    """Return a manifest for one registered capability."""
    from nous_runtime.compat.capability import get_capability

    cap = get_capability(capability_id)
    if not cap:
        return None
    availability = _availability_map().get(capability_id, {}) if include_availability else {}
    return CapabilityManifest.from_capability(cap, availability=availability)


def export_capability_manifests(include_availability: bool = True) -> list[CapabilityManifest]:
    """Export all registered capabilities as manifests."""
    from nous_runtime.compat.capability import list_capabilities

    availability = _availability_map() if include_availability else {}
    manifests: list[CapabilityManifest] = []
    for cap in list_capabilities():
        if isinstance(cap, dict):
            manifest = CapabilityManifest.from_capability(
                cap,
                availability=availability.get(str(cap.get("name", "")), {}),
            )
            manifests.append(manifest)
    manifests.sort(key=lambda m: (m.category, m.capability_id))
    return manifests


def validate_capability_manifests(manifests: list[CapabilityManifest] | None = None) -> dict[str, list[str]]:
    """Validate manifests and return errors keyed by capability ID."""
    manifests = manifests if manifests is not None else export_capability_manifests()
    errors: dict[str, list[str]] = {}
    for manifest in manifests:
        manifest_errors = manifest.validate()
        if manifest_errors:
            errors[manifest.capability_id] = manifest_errors
    return errors


def _availability_map() -> dict[str, dict[str, str]]:
    try:
        from nous_runtime.capability.availability import check_availability

        result = check_availability()
    except Exception:
        return {}

    mapped: dict[str, dict[str, str]] = {}
    for cap in result.get("available", []):
        mapped[cap.get("name", "")] = {"status": "available"}
    for cap in result.get("unavailable", []):
        mapped[cap.get("name", "")] = {
            "status": "unavailable",
            "reason": cap.get("reason", ""),
        }
    return mapped


def _coerce_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if isinstance(value, str) and value.strip():
        try:
            parsed = _json.loads(value)
        except _json.JSONDecodeError:
            return {}
        return parsed if isinstance(parsed, dict) else {}
    return {}


def _coerce_schema(value: Any) -> dict[str, Any]:
    schema = _coerce_dict(value)
    return schema or {"type": "object", "properties": {}}


def _coerce_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(v) for v in value]
    if isinstance(value, str) and value.strip():
        try:
            parsed = _json.loads(value)
        except _json.JSONDecodeError:
            return [value]
        if isinstance(parsed, list):
            return [str(v) for v in parsed]
    return []


def _public_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    blocked_parts = ("api_key", "apikey", "token", "secret", "password", "private_key", "endpoint")
    return {
        str(k): v
        for k, v in metadata.items()
        if not any(part in str(k).lower().replace("-", "_") for part in blocked_parts)
        and k not in {"input_schema", "output_schema", "depends_on", "tags"}
    }
