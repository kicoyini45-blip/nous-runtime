"""Configurable Anthropic-compatible Provider adapter."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Iterable

from nous_runtime.compat.provider import Provider
from nous_runtime.provider.credentials import resolve_credential

_SUPPORTED = {"model.reason", "model.code", "model.vision"}


class AnthropicProvider(Provider):
    """Provider for Anthropic-compatible Messages APIs."""

    provider_id = "anthropic"
    provider_name = "Anthropic Compatible"
    version = "1.0.0"

    def __init__(
        self,
        *,
        provider_id: str = "anthropic",
        provider_name: str = "Anthropic Compatible",
        endpoint: str = "https://api.anthropic.com/v1/messages",
        model: str = "",
        credential_ref: str = "",
        capabilities: Iterable[str] = ("model.reason", "model.code"),
    ) -> None:
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.endpoint = endpoint
        self.model = model
        self.credential_ref = credential_ref
        self.capabilities = tuple(
            capability for capability in capabilities if capability in _SUPPORTED
        ) or ("model.reason", "model.code")

    def list_capabilities(self) -> list[str]:
        return list(self.capabilities)

    def invoke(self, capability_id: str, **params: Any) -> dict[str, Any]:
        if capability_id not in self.capabilities:
            return {
                "ok": False,
                "error": f"Capability '{capability_id}' is not configured",
                "error_code": "NOUS_PROVIDER_CAPABILITY_UNAVAILABLE",
            }
        credential = self._credential()
        if not credential:
            return {
                "ok": False,
                "error": "Configured credential reference is unavailable",
                "error_code": "NOUS_PROVIDER_CREDENTIAL_UNAVAILABLE",
            }
        content: Any = str(params.get("prompt") or "")
        if capability_id == "model.vision" and params.get("image_url"):
            content = [
                {"type": "text", "text": content or "Describe the image"},
                {"type": "image", "source": {"type": "url", "url": str(params["image_url"])}},
            ]
        body = {
            "model": str(params.get("model") or self.model),
            "max_tokens": int(params.get("max_tokens") or 1024),
            "messages": params.get("messages") or [{"role": "user", "content": content}],
        }
        try:
            request = urllib.request.Request(
                self.endpoint,
                data=json.dumps(body).encode("utf-8"),
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": credential,
                    "anthropic-version": "2023-06-01",
                },
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read())
            blocks = payload.get("content") or ()
            text = "".join(
                str(block.get("text") or "")
                for block in blocks
                if isinstance(block, dict) and block.get("type") == "text"
            )
            return {"ok": True, "content": text, "model": body["model"]}
        except urllib.error.HTTPError as exc:
            try:
                return {
                    "ok": False,
                    "error": f"HTTP {exc.code}: {exc.reason}",
                    "error_code": "NOUS_PROVIDER_HTTP_ERROR",
                    "http_status": exc.code,
                }
            finally:
                exc.close()
        except Exception as exc:
            return {
                "ok": False,
                "error": str(exc),
                "error_code": "NOUS_PROVIDER_CONNECTION_ERROR",
            }

    def health(self) -> dict[str, Any]:
        if not self.model:
            return {"status": "degraded", "error": "Default model is not configured"}
        if not self._credential():
            return {"status": "degraded", "error": "Credential reference is unavailable"}
        return {"status": "ok", "model": self.model, "endpoint_configured": bool(self.endpoint)}

    def _credential(self) -> str:
        try:
            return resolve_credential(self.credential_ref)
        except (RuntimeError, ValueError):
            return ""
