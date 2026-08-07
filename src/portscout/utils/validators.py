"""
Validation utilities.
"""

from __future__ import annotations

import re


DOMAIN_PATTERN = re.compile(
    r"^(?=.{1,253}$)"
    r"(?:[a-zA-Z0-9]"
    r"(?:[a-zA-Z0-9-]{0,61}"
    r"[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,}$"
)


def validate_domain(
    domain: str,
) -> bool:
    """
    Validate domain name format.

    Args:
        domain: Domain string.

    Returns:
        True if valid.
    """

    return bool(
        DOMAIN_PATTERN.match(domain)
    )
