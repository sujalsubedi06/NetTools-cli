"""
Web inspection CLI commands.
"""

import typer
from rich.console import Console
from rich.table import Table

from portscout.web import WebClient


app = typer.Typer()
console = Console()


@app.command()
def inspect(
    target: str,
) -> None:
    """
    Inspect a website.
    """

    console.print(
        f"Inspecting {target}"
    )

    client = WebClient()

    result = client.fetch(
        target
    )

    if result is None:
        console.print(
            "[red]Unable to fetch target[/red]"
        )
        raise typer.Exit(1)

    table = Table(
        title=f"Web Info: {target}"
    )

    table.add_column(
        "FIELD"
    )
    table.add_column(
        "VALUE"
    )

    rows = [
        ("URL", result.url),
        ("Status", str(result.status_code)),
        ("Title", str(result.title)),
        ("Server", str(result.server)),
        ("Content-Type", str(result.content_type)),
        ("HTTPS", str(result.https)),
        ("Redirects", str(result.redirects)),
        (
            "Response Time",
            f"{result.response_time:.3f}s",
        ),
    ]

    for key, value in rows:
        table.add_row(
            key,
            value,
        )

    console.print(
        table
    )

    if result.security_headers:
        console.print(
            "\nSecurity Headers:"
        )

        for key, value in result.security_headers.items():
            console.print(
                f"{key}: {value}"
            )
