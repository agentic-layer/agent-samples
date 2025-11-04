VERSION ?= latest
IMAGE_TAG_BASE ?= ghcr.io/agentic-layer/mock-agent
IMG ?= $(IMAGE_TAG_BASE):$(VERSION)
PLATFORMS ?= linux/arm64,linux/amd64

.PHONY: all
all: docker-build

.PHONY: docker-build
docker-build:
	docker build -t $(IMG) .

.PHONY: docker-run
docker-run: docker-build
	@echo "Starting Mock Agent on port 8000"
	@echo "Agent Card URL: http://localhost:8000/.well-known/agent-card.json"
	@echo "Health Check URL: http://localhost:8000/health"
	docker run --rm -it -p 8000:8000 $(IMG)
