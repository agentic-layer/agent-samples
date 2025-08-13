.PHONY: all build run docker-build docker-run

IMAGE_NAME ?= weather-agent
GCP_LOCATION ?= europe-west3
GCP_PROJECT_ID ?= qaware-paal
GCP_REPOSITORY ?= agentic-layer

all: docker-build

build:
	uv sync

run: build
	uv run uvicorn main:app

docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run: docker-build
	@echo "Agent Card URL: http://127.0.0.1:8000/.well-known/agent-card.json"
	docker run --rm -it -p 8000:8000 $(IMAGE_NAME)

docker-push: docker-build
	$(eval image_name = $(GCP_LOCATION)-docker.pkg.dev/$(GCP_PROJECT_ID)/$(GCP_REPOSITORY)/$(IMAGE_NAME):$(shell git describe --tags --always))
	docker tag $(IMAGE_NAME) $(image_name)
	docker push $(image_name)
