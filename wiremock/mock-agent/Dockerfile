FROM wiremock/wiremock:3.13.1

COPY mappings /home/wiremock/mappings

ENV WIREMOCK_OPTIONS="--port 8000 --permitted-system-keys AGENT_.*"
