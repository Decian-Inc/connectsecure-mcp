# ConnectSecure MCP

An MCP server exposing every operation in the supplied ConnectSecure OpenAPI specification for vulnerability management, assets, assessments, integrations, and reporting.

## Install

```bash
pip install connectsecure-mcp
```

Or, from this checkout:

```bash
pip install -e ".[dev]"
```

## Configure

```bash
export CONNECTSECURE_BASE_URL="https://your-connectsecure-api-host"
export CONNECTSECURE_ACCESS_TOKEN="your-jwt-access-token"
export CONNECTSECURE_USER_ID="your-connectsecure-user-id"
# Required only for authorize_connectsecure:
export CONNECTSECURE_CLIENT_AUTH_TOKEN="base64(tenant+client_id:client_secret)"
```

`CONNECTSECURE_BASE_URL` is required because the supplied API specification does not declare a server URL. For ordinary endpoints the server sends `Authorization: Bearer <CONNECTSECURE_ACCESS_TOKEN>` and, when configured, `X-USER-ID`. The authorization endpoint sends `Client-Auth-Token`.

## Connect an MCP client

```json
{
  "mcpServers": {
    "connectsecure": {
      "command": "connectsecure-mcp",
      "env": {
        "CONNECTSECURE_BASE_URL": "https://your-connectsecure-api-host",
        "CONNECTSECURE_ACCESS_TOKEN": "your-jwt-access-token",
        "CONNECTSECURE_USER_ID": "your-connectsecure-user-id"
      }
    }
  }
}
```

Every API operation is an MCP tool. Put URI IDs in `path_params`, filtering/pagination in `query`, required per-call HTTP headers in `headers`, and JSON payloads in `body`.

See [TOOLS.md](TOOLS.md) for the complete catalog.

## Safety

The specification includes create, update, delete, and action endpoints. Those tools make the API call immediately; agents should confirm intent before invoking them.

