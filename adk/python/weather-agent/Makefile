.PHONY: all build run docker-build docker-run

all: docker-build

build:
	uv sync

run: build
	uv run uvicorn main:app

docker-build:
	docker build -t weather-agent .

docker-run: docker-build
	@echo "Agent Card URL: http://127.0.0.1:8000/.well-known/agent-card.json"
	docker run --rm -it -p 8000:8000 weather-agent