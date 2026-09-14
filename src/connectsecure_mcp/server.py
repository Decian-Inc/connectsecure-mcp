"""MCP server exposing every operation in the supplied ConnectSecure API specification."""

from __future__ import annotations

import asyncio
import json
import os
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from mcp.server.fastmcp import FastMCP

from .operations import OPERATIONS, Operation


class ConnectSecureClient:
    """Standard-library client for the ConnectSecure API."""

    def __init__(self, base_url: str | None = None, access_token: str | None = None, user_id: str | None = None, client_auth_token: str | None = None) -> None:
        self.base_url = (base_url or os.getenv("CONNECTSECURE_BASE_URL") or "").rstrip("/")
        self.access_token = access_token or os.getenv("CONNECTSECURE_ACCESS_TOKEN")
        self.user_id = user_id or os.getenv("CONNECTSECURE_USER_ID")
        self.client_auth_token = client_auth_token or os.getenv("CONNECTSECURE_CLIENT_AUTH_TOKEN")

    def request(self, operation: Operation, path_params: dict[str, str], query: dict[str, Any], headers: dict[str, str], body: Any | None) -> dict[str, Any]:
        if not self.base_url:
            raise ValueError("CONNECTSECURE_BASE_URL is not configured.")
        if operation.name == "post_w_authorize":
            if not self.client_auth_token:
                raise ValueError("CONNECTSECURE_CLIENT_AUTH_TOKEN is required for authorization.")
        elif not self.access_token:
            raise ValueError("CONNECTSECURE_ACCESS_TOKEN is not configured.")

        try:
            safe_params = {key: quote(str(value), safe="") for key, value in path_params.items()}
            path = operation.path.format(**safe_params)
        except KeyError as exc:
            raise ValueError(f"Missing required path parameter: {exc.args[0]}") from exc
        url = f"{self.base_url}{path}"
        if query:
            url = f"{url}?{urlencode(query, doseq=True)}"
        request_headers = {"Accept": "application/json", **headers}
        if operation.name == "post_w_authorize":
            request_headers.setdefault("Client-Auth-Token", self.client_auth_token or "")
        else:
            request_headers.setdefault("Authorization", f"Bearer {self.access_token}")
            if self.user_id:
                request_headers.setdefault("X-USER-ID", self.user_id)
        data = json.dumps(body).encode("utf-8") if body is not None else None
        if data is not None:
            request_headers.setdefault("Content-Type", "application/json")
        request = Request(url, data=data, headers=request_headers, method=operation.method)
        try:
            with urlopen(request, timeout=60) as response:  # nosec B310 - base URL is operator configured
                raw = response.read().decode("utf-8")
                try:
                    payload: Any = json.loads(raw) if raw else None
                except json.JSONDecodeError:
                    payload = raw
                return {"status": response.status, "data": payload}
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"ConnectSecure API returned HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"Unable to reach ConnectSecure API: {exc.reason}") from exc


def create_server(client: ConnectSecureClient | None = None) -> FastMCP:
    """Create an MCP server with one tool per OpenAPI operation."""
    api_client = client or ConnectSecureClient()
    server = FastMCP("ConnectSecure")

    def make_tool(operation: Operation):
        async def invoke(
            path_params: dict[str, str] | None = None,
            query: dict[str, Any] | None = None,
            headers: dict[str, str] | None = None,
            body: Any | None = None,
        ) -> dict[str, Any]:
            """Call one ConnectSecure API operation."""
            if operation.has_body and body is None:
                raise ValueError("This operation requires a request body.")
            return await asyncio.to_thread(api_client.request, operation, path_params or {}, query or {}, headers or {}, body)

        invoke.__name__ = operation.name
        invoke.__doc__ = (
            f"{operation.summary} Calls `{operation.method} {operation.path}`. "
            "Provide route IDs in path_params, filters and pagination in query, and any required request headers in headers. "
            + ("Provide the request payload in body." if operation.has_body else "")
        )
        return invoke

    for operation in OPERATIONS:
        invoke = make_tool(operation)
        server.tool(name=operation.name, description=invoke.__doc__)(invoke)
    return server


mcp = create_server()


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
