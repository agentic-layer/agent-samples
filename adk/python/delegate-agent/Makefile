VERSION ?= $(shell git describe --tags --always | sed 's/^v//')
IMAGE_TAG_BASE ?= eu.gcr.io/agentic-layer/delegate-agent
IMG ?= $(IMAGE_TAG_BASE):$(VERSION)
GCP_LOCATION ?= europe-west3
GCP_PROJECT_ID ?= qaware-paal
GCP_REPOSITORY ?= agentic-layer
PLATFORMS ?= linux/arm64,linux/amd64

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
	@echo "Agent Card URL: http://127.0.0.1:8000/.well-known/agent-card.json"
	docker run --rm -it -p 8000:8000 $(IMG)

.PHONY: docker-push
docker-push:
	- docker buildx create --name agent-builder
	docker buildx use agent-builder
	docker buildx build --push --platform=$(PLATFORMS) --tag ${IMG} .
