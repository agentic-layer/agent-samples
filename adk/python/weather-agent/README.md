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

Copy the `.env` template and add the Google API key:
```shell
cp .env.example .env
```

Run the agent with:

```shell
# Native Python environment
make run
# Docker container
make docker-run
```

After successful start, the agent will be available at:

* **Server**: http://127.0.0.1:8001
* **Agent Card**: http://127.0.0.1:8001/.well-known/agent-card.json

Ask the agent a question using curl:
```shell
curl http://localhost:8001/ \
    -H "Content-Type: application/json" \
    -d '{
      "jsonrpc": "2.0",
      "id": 1,
      "method": "message/send",
      "params": {
        "message": {
          "role": "agent",
          "parts": [
            {
              "kind": "text",
              "text": "What is the weather in New York?"
            }
          ],
          "messageId": "9229e770-767c-417b-a0b0-f0741243c589"
        },
        "metadata": {}
      }
    }' | jq
```

## Configuration

The agent can be configured using environment variables.

* `A2A_HOST`: Host for the Agent-to-Agent communication (default: "localhost")
