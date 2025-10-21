# Agent Samples

A collection of sample agents that can be deployed to the Agentic Layer and demonstrate different integration patterns
and tools.

## Table of Contents

- [Agents](#agents)
- [Creating New Agents](#creating-new-agents)

----

## Agents

* [Weather Agent](./adk/python/weather-agent/README.md): A simple agent that provides weather information and
  demonstrates basic agent functionality.
* [Delegate Agent](./adk/python/delegate-agent/README.md): A simple agent that delegates all tasks to sub-agents.
* [Mock Agent](./adk/wiremock/mock-agent/README.md): A simple mock agent that echoes back messages.

----

## Creating New Agents

When creating a new agent:

1. Follow the existing project structure, i.e. for a Python ADK based agent under `adk/python/`
2. Include a `Makefile` with standard targets (`build`, `run`, `docker-build`, `docker-run`)
3. Add the agent to GitHub workflows for CI/CD

## Development

Tip: If you want to adapt the agentic layer SDK, consider using a local path dependency in the agent's `pyproject.toml`:

```toml
[tool.uv.sources]
agentic-layer-sdk-adk = { path = "<path-to-sdk-python>/adk", editable = true }
```

## Creating a release

Create and push a GIT tag like `v0.1.0` and GitHub workflows will build and publish the package to PyPI.
Follow [Semantic Versioning](https://semver.org/).