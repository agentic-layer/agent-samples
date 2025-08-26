from agenticlayer.a2a_starlette import agent_to_a2a_starlette
from agenticlayer.otel import setup_otel

from delegate.agent import root_agent

setup_otel()
app = agent_to_a2a_starlette(root_agent)
