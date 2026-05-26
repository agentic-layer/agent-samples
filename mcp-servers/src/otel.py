"""OpenTelemetry setup for MCP servers."""

import logging
import os

from opentelemetry import _logs, metrics, trace
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.logging.handler import LoggingHandler
from opentelemetry.instrumentation.starlette import StarletteInstrumentor
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

_logger = logging.getLogger(__name__)


def setup_otel() -> None:
    """Set up OpenTelemetry tracing, logging and metrics."""

    log_level = os.environ.get("LOGLEVEL", "INFO").upper()
    logging.basicConfig(level=getattr(logging, log_level, logging.INFO))

    # Set log level for urllib to WARNING to reduce noise (like sending logs to OTLP)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Traces
    trace_provider = TracerProvider()
    if os.environ.get("OTEL_EXPORTER_OTLP_PROTOCOL", "http/protobuf") == "grpc":
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter as OTLPSpanExporterGrpc

        trace_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporterGrpc()))
    else:
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter as OTLPSpanExporterHttp

        trace_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporterHttp()))
    trace.set_tracer_provider(trace_provider)

    # HTTP instrumentation - creates SERVER spans for incoming requests and CLIENT spans for outgoing requests
    StarletteInstrumentor().instrument()
    HTTPXClientInstrumentor().instrument()

    # Logs - inject trace context into log records and export logs via OTLP
    LoggingInstrumentor().instrument()

    logger_provider = LoggerProvider()
    if os.environ.get("OTEL_EXPORTER_OTLP_PROTOCOL", "http/protobuf") == "grpc":
        from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter as OTLPLogExporterGrpc

        logger_provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporterGrpc()))
    else:
        from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter as OTLPLogExporterHttp

        logger_provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporterHttp()))
    _logs.set_logger_provider(logger_provider)

    logging.getLogger().addHandler(LoggingHandler(logger_provider=logger_provider))

    # Sets the global default meter provider
    metrics.set_meter_provider(
        MeterProvider(
            metric_readers=[PeriodicExportingMetricReader(OTLPMetricExporter())],
        )
    )
