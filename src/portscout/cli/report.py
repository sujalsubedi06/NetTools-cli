"""
Report generation CLI command.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

from portscout.report import ReportGenerator


console = Console()


def report(
    input_file: Path = typer.Argument(
        ...,
        help="JSON input file.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output HTML report path.",
    ),
) -> None:
    """
    Generate an HTML assessment report.
    """

    generator = ReportGenerator()

    if output is None:
        output = (
            Path("output")
            / "reports"
            / "security-report.html"
        )

    try:
        saved = generator.generate(
            input_file,
            output,
        )

    except Exception as exc:
        console.print(
            Panel(
                f"[red]{exc}[/red]",
                title="Report Error",
                border_style="red",
            )
        )
        raise typer.Exit(code=1) from exc

    console.print(
        Panel(
            f"""
[green]Report generated successfully[/green]

Input:
{input_file}

Output:
{saved}
            """.strip(),
            title="PortScout Report",
            border_style="cyan",
        )
    )