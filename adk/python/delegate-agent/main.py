import logging
import os

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from starlette.requests import Request
from starlette.responses import JSONResponse

from delegate.agent import root_agent

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

app = to_a2a(
    root_agent,
    host=os.environ.get("A2A_HOST", "localhost"),
    port=os.environ.get("A2A_HTTP_PORT", "8000"),
)


def health(_: Request):
    return JSONResponse(content={"status": "healthy"})


app.add_route("/health", health)
