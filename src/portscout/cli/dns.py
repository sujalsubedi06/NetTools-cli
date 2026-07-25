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
    reverse: str | None = typer.Option(
        None,
        "--reverse",
        "-r",
        help="Perform reverse lookup for an IP address.",
    ),
) -> None:
    """
    Lookup DNS records for a domain.
    """

    resolver = DNSResolver()

    if reverse:
        hostname = resolver.reverse_lookup(
            reverse
        )

        if hostname:
            console.print(
                f"[green]{reverse}[/green] "
                f"-> {hostname}"
            )
        else:
            console.print(
                "[yellow]No reverse DNS record found.[/yellow]"
            )

        return

    console.print(
        f"[cyan]Querying DNS records for[/cyan] {domain}"
    )

    records = resolver.lookup_all(domain)

    if not records:
        console.print(
            "[yellow]No DNS records found.[/yellow]"
        )
        raise typer.Exit()

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
            (
                str(record.ttl)
                if record.ttl
                else "-"
            ),
        )

    console.print(table)
