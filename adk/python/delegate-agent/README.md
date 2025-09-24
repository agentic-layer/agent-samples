# delegate-agent

The delegate agent demonstrates A2A delegation with Python ADK. This agent showcases:

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

* **Server**: http://127.0.0.1:8100
* **Agent Card**: http://127.0.0.1:8100/.well-known/agent-card.json

Ask the agent a question using curl:
```shell
curl http://localhost:8100/ \
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
          "messageId": "9229e770-767c-417b-a0b0-f0741243c589",
          "contextId": "abcd1234-5678-90ab-cdef-1234567890ab"
        },
        "metadata": {}
      }
    }' | jq
```

## Configuration

The agent can be configured using environment variables:

* `AGENT_A2A_RPC_URL`: Base URL for the Agent-to-Agent communication
* `SUB_AGENTS`: JSON map of sub agents to delegate to. Format: `{"agent_name": {"url": "http://agent-url/.well-known/agent-card.json"}}` (default: empty)

### Sub Agents Configuration

The delegate agent can work with multiple sub agents by configuring the `SUB_AGENTS` environment variable. Each sub agent is defined by its name and the URL to its agent card. See [.env.example](.env.example) for an example configuration.
