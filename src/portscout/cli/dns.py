"""
DNS CLI command.
"""

from __future__ import annotations

import typer
from rich.table import Table

from portscout.core.console import console
from portscout.dns import DNSResolver


def dns(
    domain: str = typer.Argument(
        ...,
        help="Domain name to query.",
    ),
) -> None:
    """
    Lookup DNS records for a domain.
    """

    resolver = DNSResolver()

    console.print(
        f"[cyan]Querying DNS records for[/cyan] {domain}"
    )

    records = resolver.lookup_basic(domain)

    if not records:
        console.print(
            "[yellow]No DNS records found.[/yellow]"
        )
        raise typer.Exit(code=0)

    table = Table(
        title=f"DNS Records: {domain}",
    )

    table.add_column(
        "TYPE",
        style="cyan",
    )

    table.add_column(
        "VALUE",
    )

    table.add_column(
        "TTL",
    )

    for record in records:
        table.add_row(
            record.record_type,
            record.value,
            str(record.ttl)
            if record.ttl
            else "-",
        )

    console.print(table)
