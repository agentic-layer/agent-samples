FROM wiremock/wiremock:3.13.1-alpine

COPY mappings /home/wiremock/mappings

EXPOSE 8080

CMD ["--port", "8080", "--global-response-templating", "--verbose"]
