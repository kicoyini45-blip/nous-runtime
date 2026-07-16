"""Minimal authenticated HTTP adapter for the Runtime API route table."""

from __future__ import annotations

import ipaddress
import json
import os
import ssl
import threading
import time
from collections import defaultdict, deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, urlsplit

from nous_runtime.api.routes import route_server


class RuntimeHTTPServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, server_address, handler_class, *, max_request_bytes: int = 1_048_576, requests_per_minute: int = 120):
        super().__init__(server_address, handler_class)
        self.max_request_bytes = max_request_bytes
        self.requests_per_minute = requests_per_minute
        self._rate_lock = threading.Lock()
        self._rate: dict[str, deque[float]] = defaultdict(deque)

    def allow_request(self, source: str) -> bool:
        now = time.monotonic()
        with self._rate_lock:
            entries = self._rate[source]
            while entries and now - entries[0] >= 60:
                entries.popleft()
            if len(entries) >= self.requests_per_minute:
                return False
            entries.append(now)
            return True


class RuntimeAPIHandler(BaseHTTPRequestHandler):
    server_version = "NousRuntimeAPI/0.1"

    def do_GET(self) -> None:
        self._dispatch("GET")

    def do_POST(self) -> None:
        self._dispatch("POST")

    def do_PUT(self) -> None:
        self._dispatch("PUT")

    def do_PATCH(self) -> None:
        self._dispatch("PATCH")

    def do_DELETE(self) -> None:
        self._dispatch("DELETE")

    def log_message(self, format: str, *args: Any) -> None:
        return None

    def _dispatch(self, method: str) -> None:
        server: RuntimeHTTPServer = self.server  # type: ignore[assignment]
        if not server.allow_request(self.client_address[0]):
            self._write(429, {"ok": False, "error": {"code": "NOUS_RATE_LIMITED", "message": "Request rate limit exceeded."}})
            return
        parsed = urlsplit(self.path)
        query = parse_qs(parsed.query, keep_blank_values=True)
        query_token = any(name.lower() in {"token", "api_key", "access_token"} for name in query)
        params = {name: values[-1] for name, values in query.items() if values and name.lower() not in {"token", "api_key", "access_token"}}
        try:
            body = self._read_body()
        except ValueError as exc:
            self._write(413 if "large" in str(exc) else 400, {"ok": False, "error": {"code": "NOUS_INVALID_REQUEST", "message": str(exc)}})
            return
        headers = {name.lower(): value for name, value in self.headers.items() if name.lower() in {"authorization", "x-auth-token"}}
        response = route_server(method, parsed.path, body=body, params=params, auth={"headers": headers, "query_token": query_token})
        self._write(self._status(response), response)

    def _read_body(self) -> dict[str, Any] | None:
        length_text = self.headers.get("Content-Length", "0")
        try:
            length = int(length_text)
        except ValueError as exc:
            raise ValueError("Invalid Content-Length.") from exc
        server: RuntimeHTTPServer = self.server  # type: ignore[assignment]
        if length < 0 or length > server.max_request_bytes:
            raise ValueError("Request body is too large.")
        if length == 0:
            return None
        media_type = self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        if media_type != "application/json":
            raise ValueError("Content-Type must be application/json.")
        try:
            data = json.loads(self.rfile.read(length))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise ValueError("Request body is not valid JSON.") from exc
        if not isinstance(data, dict):
            raise ValueError("Request JSON must be an object.")
        return data

    def _write(self, status: int, data: dict[str, Any]) -> None:
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(payload)

    @staticmethod
    def _status(response: dict[str, Any]) -> int:
        if response.get("ok"):
            return 200
        error = response.get("error") or {}
        code = str(error.get("code") if isinstance(error, dict) else "")
        if code in {"NOUS_AUTH_REQUIRED", "NOUS_UNAUTHORIZED", "NOUS_UNAUTHENTICATED"}:
            return 401
        if code in {"NOUS_FORBIDDEN", "NOUS_GOVERNANCE_DENIED", "NOUS_APPROVAL_REQUIRED"}:
            return 403
        if code == "NOUS_INVALID_REQUEST":
            return 400
        return 500


def create_server(host: str = "127.0.0.1", port: int = 8770, *, ssl_context: ssl.SSLContext | None = None, trusted_private_transport: bool = False, max_request_bytes: int = 1_048_576, requests_per_minute: int = 120) -> RuntimeHTTPServer:
    address = ipaddress.ip_address(host)
    remote = not address.is_loopback
    if remote and not os.environ.get("NOUS_API_TOKEN"):
        raise RuntimeError("NOUS_API_TOKEN is required for remote API binding")
    if remote and ssl_context is None and not trusted_private_transport:
        raise RuntimeError("remote API binding requires TLS or an explicitly trusted private transport")
    server = RuntimeHTTPServer((host, port), RuntimeAPIHandler, max_request_bytes=max_request_bytes, requests_per_minute=requests_per_minute)
    if ssl_context is not None:
        server.socket = ssl_context.wrap_socket(server.socket, server_side=True)
    return server
