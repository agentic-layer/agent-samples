# Mock Agent

A simple mock agent for testing purposes that implements the Agent-to-Agent (A2A) communication protocol. The agent echoes back the received message, making it ideal for automated testing scenarios without requiring the deployment of a real AI service.

## Features

* Implements A2A Request/Response protocol (JSON-RPC 2.0)
* Echo functionality: Returns received questions in the response
* Minimal container image based on Wiremock
* Fast startup time
* Configurable via mounted configuration files
* Health check endpoint
* Agent Card endpoint

## Prerequisites

Before you begin, ensure you have the following tools installed:

* **Docker** for containerization
* **Make** for build automation
* **curl** and **jq** for testing (optional)

## Usage

Build and run the agent with:

```shell
# Build Docker image
make docker-build

# Run the agent (accessible on port 8080)
make docker-run
```

After successful start, the agent will be available at:

* **Server**: http://localhost:8080
* **Agent Card**: http://localhost:8080/.well-known/agent-card.json
* **Health Check**: http://localhost:8080/health

Ask the agent a question using curl:

```shell
curl http://localhost:8080/ \
    -H "Content-Type: application/json" \
    -d '{
      "jsonrpc": "2.0",
      "id": 1,
      "method": "message/send",
      "params": {
        "message": {
          "role": "user",
          "parts": [
            {
              "kind": "text",
              "text": "Message to echo back"
            }
          ],
          "messageId": "9229e770-767c-417b-a0b0-f0741243c589",
          "contextId": "abcd1234-5678-90ab-cdef-1234567890ab"
        },
        "metadata": {}
      }
    }' | jq
```


Expected response:

```json
{
  "id": "1",
  "jsonrpc": "2.0",
  "result": {
    "artifacts": [
      {
        "artifactId": "1d80baa9-00c6-4107-9bde-078e099e9594",
        "parts": [
          {
            "kind": "text",
            "text": "What is the weather in New York?"
          }
        ]
      }
    ],
    "contextId": "abcd1234-5678-90ab-cdef-1234567890ab",
    "history": [
      {
        "contextId": "abcd1234-5678-90ab-cdef-1234567890ab",
        "kind": "message",
        "messageId": "9229e770-767c-417b-a0b0-f0741243c589",
        "parts": [
          {
            "kind": "text",
            "text": "What is the weather in New York?"
          }
        ],
        "role": "user",
        "taskId": "067afadd-dbdb-41b8-a738-97a66b438a91"
      },
      {
        "kind": "message",
        "messageId": "cc533f58-9c13-43e3-a553-42e5820245ea",
        "parts": [
          {
            "kind": "text",
            "text": "What is the weather in New York?"
          }
        ],
        "role": "agent"
      }
    ],
    "id": "d28ee519-5ad6-43ed-82e5-748358295588",
    "kind": "task",
    "metadata": {
      "adk_app_name": "mock_agent",
      "adk_author": "mock_agent"
    },
    "status": {
      "state": "completed",
      "timestamp": "2025-10-21T12:25:45"
    }
  }
}
```

## Configuration

The mock agent uses Wiremock with mappings located in the `mappings/` directory:

* `a2a-message.json` - Handles A2A message/send requests with echo functionality
* `agent-card.json` - Provides Agent Card
* `health.json` - Health check endpoint

### Customizing Configuration

You can override the default configuration by mounting a custom 'mappings' directory:

```shell
docker run --rm -it \
    -p 8080:8080 \
    -v $(pwd)/custom-mapping-directory:/home/wiremock/mappings \
    ghcr.io/agentic-layer/mock-agent:latest
```