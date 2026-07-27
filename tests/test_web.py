"""
Tests for web client.
"""

from unittest.mock import patch, Mock

from nettools.web import WebClient


def test_web_fetch_success() -> None:
    """
    Test successful HTTP fetch.
    """

    client = WebClient()

    mock_response = Mock()
    mock_response.url = "https://example.com/"
    mock_response.status_code = 200
    mock_response.text = "<html><title>Example</title></html>"
    mock_response.headers = {
        "server": "cloudflare",
        "content-type": "text/html",
    }
    mock_response.history = []

    with patch(
        "requests.get",
        return_value=mock_response,
    ):
        result = client.fetch("https://example.com")

    assert result is not None
    assert result.status_code == 200
    assert result.title == "Example"
    assert result.https is True


def test_web_fetch_failure() -> None:
    """
    Test HTTP failure handling.
    """

    client = WebClient()

    with patch(
        "requests.get",
        side_effect=Exception,
    ):
        result = client.fetch("https://invalid.example")

    assert result is None
