import os

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from starlette.requests import Request
from starlette.responses import JSONResponse

from weather.agent import root_agent

app = to_a2a(
    root_agent,
    host=os.environ.get("A2A_HOST", "localhost"),
)


def health(_: Request):
    return JSONResponse(content={"status": "healthy"})


app.add_route("/health", health)
