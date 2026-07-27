"""
Tests for subdomain enumeration.
"""

from pathlib import Path
from unittest.mock import patch

from nettools.subdomains import (
    SubdomainEnumerator,
)


def test_wordlist_loading(
    tmp_path: Path,
) -> None:
    """
    Test loading wordlist entries.
    """

    wordlist = tmp_path / "words.txt"

    wordlist.write_text(
        "www\napi\nwww\n\n",
        encoding="utf-8",
    )

    enumerator = SubdomainEnumerator(
        wordlist=wordlist,
    )

    results = enumerator.load_wordlist()

    assert results == [
        "api",
        "www",
    ]


def test_resolve_failure() -> None:
    """
    Test invalid hostname handling.
    """

    enumerator = SubdomainEnumerator()

    with patch(
        "socket.gethostbyname",
        side_effect=Exception,
    ):
        result = enumerator.resolve(
            "invalid.example.com",
        )

    assert result is None


def test_enumeration_returns_list(
    tmp_path: Path,
) -> None:
    """
    Test enumeration output format.
    """

    wordlist = tmp_path / "words.txt"

    wordlist.write_text(
        "www\napi\n",
        encoding="utf-8",
    )

    enumerator = SubdomainEnumerator(
        wordlist=wordlist,
    )

    with patch.object(
        enumerator,
        "resolve",
        return_value=None,
    ):
        results = enumerator.enumerate(
            "example.com",
        )

    assert isinstance(
        results,
        list,
    )
