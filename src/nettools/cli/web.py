"""
Web inspection CLI commands.
"""

import typer
from rich.console import Console
from rich.table import Table

from nettools.core.output import (
    to_json,
    write_json,
)
from nettools.web import WebClient, analyze_security


app = typer.Typer()
console = Console()


@app.command()
def inspect(
    target: str,
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Output results as JSON.",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save results as JSON file.",
    ),
) -> None:
    """
    Inspect a website.
    """

    console.print(f"Inspecting {target}")

    client = WebClient()

    result = client.fetch(target)

    if result is None:
        console.print("[red]Unable to fetch target[/red]")
        raise typer.Exit(1)

    report = analyze_security(
        result.url,
        result.security_headers,
    )

    data = {
        "web_info": result,
        "security": report,
    }

    if output:
        saved_path = write_json(
            data,
            output,
        )

        console.print(f"[green]Saved JSON output:[/green] {saved_path}")

    if json_output:
        console.print(to_json(data))
        raise typer.Exit()

    table = Table(title=f"Web Info: {target}")

    table.add_column("FIELD")
    table.add_column("VALUE")

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

    console.print(table)

    security = Table(title="Security Analysis")

    security.add_column("CHECK")
    security.add_column("RESULT")

    security.add_row(
        "Security Score",
        f"{report.score}/100",
    )

    security.add_row(
        "HTTPS",
        "Enabled" if report.https else "Disabled",
    )

    security.add_row(
        "Missing Headers",
        (", ".join(report.missing_headers) if report.missing_headers else "None"),
    )

    console.print(security)
