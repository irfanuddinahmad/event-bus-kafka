"""
Kafka implementation for Open edX event bus.

Public API will be in this module for the most part.

See ADR ``docs/decisions/0006-public-api-and-app-organization.rst`` for the reasoning.
"""

from importlib.metadata import PackageNotFoundError, version

from edx_event_bus_kafka.internal.consumer import KafkaEventConsumer
from edx_event_bus_kafka.internal.producer import KafkaEventProducer, create_producer

try:
    __version__ = version('edx-event-bus-kafka')
except PackageNotFoundError:  # pragma: no cover
    pass
