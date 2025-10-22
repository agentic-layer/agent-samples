FROM wiremock/wiremock:3.13.1

COPY mappings /home/wiremock/mappings

EXPOSE 8080

CMD ["--port", "8080", "--global-response-templating", "--permitted-system-keys", "AGENT_.*", "--verbose"]
