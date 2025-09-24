VERSION ?= latest
IMAGE_TAG_BASE ?= ghcr.io/agentic-layer/delegate-agent
IMG ?= $(IMAGE_TAG_BASE):$(VERSION)
PLATFORMS ?= linux/arm64,linux/amd64

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

.PHONY: all
all: docker-build

.PHONY: build
build:
	uv sync

.PHONY: run
run: build
	uv run uvicorn main:app

.PHONY: docker-build
docker-build:
	docker build -t $(IMG) .

.PHONY: docker-run
docker-run: docker-build
	@echo "Agent Card URL: ${AGENT_A2A_RPC_URL}/.well-known/agent-card.json"
	docker run --rm -it -p ${UVICORN_PORT}:8000 $(IMG)
