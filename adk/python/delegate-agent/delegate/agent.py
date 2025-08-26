import json
import logging
import os

from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.models.lite_llm import LiteLlm


def create_sub_agents():
    """Create sub agents from environment variable configuration."""
    sub_agents_config = os.environ.get("SUB_AGENTS", "{}")
    try:
        agents_map = json.loads(sub_agents_config)
    except json.JSONDecodeError:
        print(f"Warning: Invalid JSON in SUB_AGENTS environment variable. Using empty configuration.")
        agents_map = {}

    sub_agents = []
    for agent_name, config in agents_map.items():
        if "url" not in config:
            print(f"Warning: Missing 'url' for agent '{agent_name}'. Skipping.")
            continue

        logging.info("Adding sub-agent: %s with URL: %s", agent_name, config["url"])
        sub_agents.append(RemoteA2aAgent(
            name=agent_name,
            agent_card=config["url"],
        ))

    return sub_agents


root_agent = Agent(
    name="delegate_agent",
    model=LiteLlm("gemini/gemini-2.0-flash"),
    description=(
        "Agent to delegate to other agents."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions by delegating to sub agents."
    ),
    sub_agents=create_sub_agents(),
)
