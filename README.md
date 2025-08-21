# Agent Samples

A collection of sample agents demonstrating best practices and various use cases for building agents with the Agent Development Kit (ADK). This repository serves as a comprehensive resource for developers who want to learn, test, and contribute to agent development using modern frameworks and deployment strategies.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Sample Agent: Weather Agent](#sample-agent-weather-agent)

----

## Prerequisites

Before you begin, ensure you have the following tools installed:

* **Python** >= 3.13
* **uv** package manager (latest version recommended)
* **Docker** for containerization
* **Make** for build automation
* **Git** for version control

----

## Getting Started

### Installation

1. Navigate to the specific agent directory you want to work with, for example, the weather agent:
   ```bash
   cd adk/python/weather-agent
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

### Running Your Agent

The recommended approach is to use a `Makefile` for automation, see [`adk/python/weather-agent/Makefile`](adk/python/weather-agent/Makefile).

#### Local Development
```shell
make run
```
The server will be running at http://localhost:8000

#### Docker Container
```bash
make docker-run
```
After successful start, the agent will be available at:
* **Server**: http://127.0.0.1:8000
* **Agent Card**: http://127.0.0.1:8000/.well-known/agent-card.json

### Verifying Installation

Once the agent is running, you can verify it's working correctly by accessing the health endpoint:
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status": "healthy"}
```

## Configuration

### Environment Variables

Best practice is to configure agents through environment variables:

* `A2A_HOST`: Host for the Agent-to-Agent communication (default: "localhost")
* `PORT`: Port number for the server (default: 8000)

## Contributing

We welcome contributions\! Please follow these guidelines to ensure a smooth development process. Check out the [Contributing Guide](https://github.com/agentic-layer/.github?tab=contributing-ov-file) for more details.

### Setup for Contributors

1. **Install pre-commit hooks** (mandatory):
   ```bash
   pre-commit install
   ```

2. **Code Style**: We follow Python best practices with automated formatting and linting

### Creating New Agents

When creating a new agent:

1. Follow the existing project structure under `adk/python/`
2. Include a `Makefile` with standard targets (`build`, `run`, `docker-build`, `docker-run`)
3. Provide a `pyproject.toml` with proper dependencies
4. Include a health endpoint in your main application
5. Add comprehensive documentation

## Sample Agent: Weather Agent
The weather agent demonstrates basic agent functionality with weather-related capabilities. This agent showcases:
* Agent-to-Agent (A2A) communication patterns
* RESTful API endpoints
* Health monitoring
* Docker containerization
* Multi-platform deployment
