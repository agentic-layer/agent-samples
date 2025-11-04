FROM wiremock/wiremock:3.13.1

COPY mappings /home/wiremock/mappings

EXPOSE 8000

CMD ["--port", "8000", "--global-response-templating", "--permitted-system-keys", "AGENT_.*", "--verbose"]
