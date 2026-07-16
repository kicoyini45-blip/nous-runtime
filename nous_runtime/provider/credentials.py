"""Resolve Provider credentials from references without persisting secret values."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class CredentialStatus:
    reference: str
    source: str
    available: bool
    detail: str


class CredentialStoreUnavailable(RuntimeError):
    """Raised when an optional operating-system credential backend is absent."""


def resolve_credential(reference: str) -> str:
    """Resolve an environment or OS secret-store reference."""
    if not reference:
        return ""
    source, service, account = _parse_reference(reference)
    if source == "env":
        return os.environ.get(service, "")
    keyring = _keyring()
    return str(keyring.get_password(service, account) or "")


def store_credential(reference: str, value: str) -> None:
    """Store a credential through the optional OS-backed keyring."""
    source, service, account = _parse_reference(reference)
    if source == "env":
        raise ValueError("Environment references are set outside Nous")
    if not value:
        raise ValueError("Credential value is empty")
    _keyring().set_password(service, account, value)


def credential_status(reference: str) -> CredentialStatus:
    """Describe availability without exposing the credential value."""
    if not reference:
        return CredentialStatus("", "none", True, "Not required")
    try:
        source, service, _ = _parse_reference(reference)
        value = resolve_credential(reference)
    except (CredentialStoreUnavailable, ValueError) as exc:
        return CredentialStatus(reference, "secret-store", False, str(exc))
    label = "Environment variable" if source == "env" else "OS secret store"
    detail = "Available" if value else "Reference configured; credential missing"
    return CredentialStatus(reference, label, bool(value), detail)


def describe_credential_reference(reference: str) -> str:
    """Return a safe display label containing no credential material."""
    if not reference:
        return "Not required"
    source, service, account = _parse_reference(reference)
    if source == "env":
        return f"Environment variable · {service}"
    return f"OS secret store · {service}/{account}"


def _parse_reference(reference: str) -> tuple[str, str, str]:
    if reference.startswith("env:"):
        name = reference[4:].strip()
        if not name or not name.replace("_", "A").isalnum():
            raise ValueError("Invalid environment-variable reference")
        return "env", name, ""
    for prefix in ("secret:", "keyring:", "credman:"):
        if reference.startswith(prefix):
            value = reference[len(prefix) :]
            service, separator, account = value.partition(":")
            if not separator:
                service, separator, account = value.partition("/")
            if not service or not separator or not account:
                raise ValueError("Secret-store references require service and account")
            return "secret", service, account
    raise ValueError("Credential reference must use env:, secret:, keyring:, or credman:")


def _keyring():
    try:
        import keyring
    except ImportError as exc:
        raise CredentialStoreUnavailable(
            "OS secret store support requires the optional 'keyring' package"
        ) from exc
    return keyring
