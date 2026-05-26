VERSION ?= latest
IMAGE_TAG_BASE ?= ghcr.io/agentic-layer/weather-mcp-server
IMG ?= $(IMAGE_TAG_BASE):$(VERSION)
PLATFORMS ?= linux/arm64,linux/amd64

SERVER ?= src/weather.py
PORT ?= 8000

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
	uv run fastmcp run $(SERVER) --transport streamable-http --host 0.0.0.0 --port $(PORT)

.PHONY: docker-build
docker-build:
	docker build -t $(IMG) .

.PHONY: docker-run
docker-run: docker-build
	docker run --rm -it -p $(PORT):8000 $(IMG) $(SERVER)
