"""Configurable OpenAI-compatible Provider adapter."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any, Iterable

from nous_runtime.compat.provider import Provider
from nous_runtime.provider.credentials import resolve_credential

_SUPPORTED = {
    "model.reason",
    "model.code",
    "model.embed",
    "model.vision",
    "model.rerank",
}


class OpenAIProvider(Provider):
    """Provider for OpenAI-compatible HTTP APIs with per-instance configuration."""

    provider_id = "openai"
    provider_name = "openai"
    version = "1.1.0"

    def __init__(
        self,
        *,
        provider_id: str = "openai",
        provider_name: str = "OpenAI Compatible",
        endpoint: str = "",
        model: str = "",
        credential_ref: str = "",
        capabilities: Iterable[str] = ("model.reason", "model.code"),
        capability_endpoints: dict[str, str] | None = None,
    ) -> None:
        self.provider_id = provider_id
        self.provider_name = provider_name
        self.endpoint = endpoint
        self.model = model
        self.credential_ref = credential_ref
        self.capabilities = tuple(
            capability for capability in capabilities if capability in _SUPPORTED
        ) or ("model.reason", "model.code")
        self.capability_endpoints = dict(capability_endpoints or {})

    def list_capabilities(self) -> list[str]:
        return list(self.capabilities)

    def invoke(self, capability_id: str, **params: Any) -> dict[str, Any]:
        if capability_id not in self.capabilities:
            return {
                "ok": False,
                "error": f"Capability '{capability_id}' is not configured",
                "error_code": "NOUS_PROVIDER_CAPABILITY_UNAVAILABLE",
            }
        model = str(params.get("model") or self.model or os.environ.get("NOUS_LLM_MODEL") or "")
        endpoint = self._endpoint(capability_id)
        if not endpoint or not model:
            return {
                "ok": False,
                "error": "Provider endpoint or model is not configured",
                "error_code": "NOUS_PROVIDER_CONFIG_INCOMPLETE",
            }
        api_key = self._credential()
        if self.credential_ref and not api_key:
            return {
                "ok": False,
                "error": "Configured credential reference is unavailable",
                "error_code": "NOUS_PROVIDER_CREDENTIAL_UNAVAILABLE",
            }
        body = self._request_body(capability_id, model, params)
        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        try:
            request = urllib.request.Request(
                endpoint,
                data=json.dumps(body).encode("utf-8"),
                headers=headers,
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read())
            return self._parse_response(capability_id, payload, model)
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
        if not (self.model or os.environ.get("NOUS_LLM_MODEL")):
            return {"status": "degraded", "error": "Default model is not configured"}
        if self.credential_ref and not self._credential():
            return {"status": "degraded", "error": "Credential reference is unavailable"}
        return {
            "status": "ok",
            "model": self.model or os.environ.get("NOUS_LLM_MODEL", ""),
            "endpoint_configured": bool(self.endpoint or os.environ.get("NOUS_LLM_API_URL")),
        }

    def _credential(self) -> str:
        if self.credential_ref:
            try:
                return resolve_credential(self.credential_ref)
            except (RuntimeError, ValueError):
                return ""
        return os.environ.get("NOUS_LLM_API_KEY", "")

    def _endpoint(self, capability_id: str) -> str:
        configured = self.capability_endpoints.get(capability_id)
        if configured:
            return configured
        endpoint = self.endpoint or os.environ.get(
            "NOUS_LLM_API_URL",
            "https://api.openai.com/v1/chat/completions",
        )
        replacements = {
            "model.embed": "embeddings",
            "model.rerank": "rerank",
        }
        suffix = replacements.get(capability_id)
        if not suffix:
            return endpoint
        if endpoint.endswith("/chat/completions"):
            return endpoint[: -len("chat/completions")] + suffix
        return endpoint.rstrip("/") + f"/{suffix}"

    @staticmethod
    def _request_body(
        capability_id: str,
        model: str,
        params: dict[str, Any],
    ) -> dict[str, Any]:
        if capability_id == "model.embed":
            return {"model": model, "input": params.get("text") or params.get("input") or ""}
        if capability_id == "model.rerank":
            return {
                "model": model,
                "query": params.get("query") or "",
                "documents": params.get("documents") or (),
            }
        content: Any = params.get("prompt", "")
        if capability_id == "model.vision" and params.get("image_url"):
            content = [
                {"type": "text", "text": str(params.get("prompt") or "Describe the image")},
                {"type": "image_url", "image_url": {"url": str(params["image_url"])}},
            ]
        return {
            "model": model,
            "messages": params.get("messages") or [{"role": "user", "content": content}],
            "max_tokens": int(params.get("max_tokens") or 1024),
        }

    @staticmethod
    def _parse_response(
        capability_id: str,
        payload: dict[str, Any],
        model: str,
    ) -> dict[str, Any]:
        if capability_id == "model.embed":
            vector = (payload.get("data") or [{}])[0].get("embedding") or []
            return {"ok": True, "embedding": vector, "vector_dim": len(vector), "model": model}
        if capability_id == "model.rerank":
            return {"ok": True, "results": payload.get("results") or (), "model": model}
        content = (payload.get("choices") or [{}])[0].get("message", {}).get("content", "")
        return {"ok": True, "content": content, "model": model}
