# weather-agent

The weather agent demonstrates basic agent functionality with Python ADK. This agent showcases:

* Agent-to-Agent (A2A) communication patterns
* RESTful API endpoints
* Health monitoring
* Docker containerization
* Multi-platform deployment

## Prerequisites

Before you begin, ensure you have the following tools installed:

* **uv** package manager
* **Docker** for containerization
* **Make** for build automation

## Usage

Run the agent with:

```shell
# Native Python environment
make run
# Docker container
make docker-run
```

After successful start, the agent will be available at:

* **Server**: http://127.0.0.1:8000
* **Agent Card**: http://127.0.0.1:8000/.well-known/agent-card.json

## Configuration

The agent can be configured using environment variables.

* `A2A_HOST`: Host for the Agent-to-Agent communication (default: "localhost")
