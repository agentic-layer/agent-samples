# MCP Servers

[Model Context Protocol](https://modelcontextprotocol.io/) servers built with
[FastMCP](https://gofastmcp.com/). The structure follows the
[`showcase-cross-selling/mcp-servers`](https://github.com/agentic-layer/showcase-cross-selling/tree/main/mcp-servers)
blueprint.

## Servers

| Server | Entry point | Tools |
| --- | --- | --- |
| Weather | `src/weather.py` | `get_weather`, `get_current_time` |

The weather server exposes the demo tools originally implemented inline in the
ADK weather-agent (see
[`adk/python/weather-agent/weather/agent.py`](../adk/python/weather-agent/weather/agent.py)).

## Layout

```
mcp-servers/
├── Dockerfile
├── Makefile
├── pyproject.toml
└── src/
    ├── weather.py     # MCP server (FastMCP app `mcp`)
    ├── middleware.py  # OpenTelemetry metrics middleware
    ├── otel.py        # OTel tracing/logging/metrics setup
    └── response.py    # Shared success/error response helpers
```

## Local development

Requires [`uv`](https://docs.astral.sh/uv/) and Python 3.14.

```bash
make build   # uv sync
make run     # fastmcp run src/weather.py --transport streamable-http --port 8000
```

Override the server or port:

```bash
make run SERVER=src/weather.py PORT=8080
```

## Docker

```bash
make docker-build
make docker-run
```

The container exposes port `8000` and runs the FastMCP CLI as its entrypoint.
The server module path is passed as the command argument, so any server in
`src/` can be selected:

```bash
docker run --rm -it -p 8000:8000 ghcr.io/agentic-layer/weather-mcp-server:latest src/weather.py
```

## Observability

OpenTelemetry traces, logs, and metrics are exported via OTLP. Configure with
the standard `OTEL_EXPORTER_OTLP_*` environment variables. The default
protocol is `http/protobuf`; set `OTEL_EXPORTER_OTLP_PROTOCOL=grpc` to switch.
