"""Weather MCP server.

Exposes the weather and time tools originally implemented in the ADK
weather-agent (see adk/python/weather-agent/weather/agent.py) as MCP tools.
"""

import datetime
from zoneinfo import ZoneInfo

from fastmcp import FastMCP
from opentelemetry.trace import get_tracer

import middleware
import otel
import response

otel.setup_otel()
tracer = get_tracer(__name__)

# Create an MCP server for weather and time information
mcp: FastMCP = FastMCP(name="Weather", middleware=[middleware.OtelMetricsMiddleware()])


@mcp.tool()
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city: The name of the city for which to retrieve the weather report.

    Returns:
        Dictionary with the weather report on success, or error details on failure.
    """
    with tracer.start_as_current_span("weather.get_weather", attributes={"city": city}):
        if city.lower() == "new york":
            return response.create_success_response(
                f"Weather report for {city}",
                report=(
                    "The weather in New York is sunny with a temperature of 25 degrees"
                    " Celsius (77 degrees Fahrenheit)."
                ),
                city=city,
            )

        return response.create_error_response(
            f"Weather information for '{city}' is not available.",
            "WEATHER_NOT_AVAILABLE",
            requested_city=city,
        )


@mcp.tool()
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city: The name of the city for which to retrieve the current time.

    Returns:
        Dictionary with the local time on success, or error details on failure.
    """
    with tracer.start_as_current_span("weather.get_current_time", attributes={"city": city}):
        if city.lower() == "new york":
            tz_identifier = "America/New_York"
        else:
            return response.create_error_response(
                f"Sorry, I don't have timezone information for {city}.",
                "TIMEZONE_NOT_AVAILABLE",
                requested_city=city,
            )

        tz = ZoneInfo(tz_identifier)
        now = datetime.datetime.now(tz)
        report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'

        return response.create_success_response(
            f"Current time for {city}",
            report=report,
            city=city,
            timezone=tz_identifier,
        )
