"""
DNS module tests.
"""

from __future__ import annotations

from unittest.mock import patch

from nettools.dns import DNSRecord, DNSResolver
from nettools.utils.validators import validate_domain


def test_dns_record_creation() -> None:
    """
    Test DNSRecord model.
    """

    record = DNSRecord(
        record_type="A",
        value="127.0.0.1",
        ttl=300,
    )

    assert record.record_type == "A"
    assert record.value == "127.0.0.1"
    assert record.ttl == 300


def test_dns_resolver_initialization() -> None:
    """
    Test resolver creation.
    """

    resolver = DNSResolver()

    assert resolver.timeout == 3.0


def test_domain_validation() -> None:
    """
    Test domain validation.
    """

    assert validate_domain("example.com")

    assert not validate_domain("hello")


def test_dns_lookup_failure() -> None:
    """
    Test failed DNS query handling.
    """

    resolver = DNSResolver()

    with patch(
        "dns.resolver.resolve",
        side_effect=Exception,
    ):
        records = resolver.lookup(
            "example.com",
            "A",
        )

    assert records == []


def test_reverse_lookup_failure() -> None:
    """
    Test reverse DNS failure handling.
    """

    resolver = DNSResolver()

    with patch(
        "socket.gethostbyaddr",
        side_effect=OSError,
    ):
        result = resolver.reverse_lookup(
            "192.0.2.1",
        )

    assert result is None
