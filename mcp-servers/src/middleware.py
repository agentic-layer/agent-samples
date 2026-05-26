"""Shared OpenTelemetry metrics middleware for MCP servers."""

import time

from fastmcp.server.middleware import Middleware, MiddlewareContext
from opentelemetry import metrics

meter = metrics.get_meter(__name__)

tool_call_counter = meter.create_counter("mcp.tool.calls", description="Number of MCP tool calls")
tool_call_duration = meter.create_histogram("mcp.tool.duration", unit="s", description="Duration of MCP tool calls")


class OtelMetricsMiddleware(Middleware):
    """Middleware that records OpenTelemetry metrics for tool calls."""

    async def on_call_tool(self, context: MiddlewareContext, call_next):  # type: ignore[override]
        tool_name = getattr(context.message, "name", "unknown")
        start = time.perf_counter()
        try:
            result = await call_next(context)
            tool_call_counter.add(1, {"tool.name": tool_name, "status": "success"})
            return result
        except Exception:
            tool_call_counter.add(1, {"tool.name": tool_name, "status": "error"})
            raise
        finally:
            tool_call_duration.record(time.perf_counter() - start, {"tool.name": tool_name})
