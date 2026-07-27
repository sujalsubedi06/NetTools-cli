"""
Main CLI application.
"""

from __future__ import annotations

import typer

from nettools import __version__
from nettools.cli.dns import dns
from nettools.cli.scan import scan
from nettools.cli.web import inspect
from nettools.cli.subdomains import subdomains
from nettools.core.console import console
from nettools.cli.report import report
from nettools.cli.assess import assess


app = typer.Typer(
    name="nettools",
    help=(
        "A modern Python network reconnaissance toolkit.\n\n"
        "Designed for authorized network diagnostics and discovery."
    ),
    no_args_is_help=True,
    add_completion=False,
)


app.command(name="scan")(scan)

app.command(name="dns")(dns)

app.command(name="subdomains")(subdomains)

app.command(name="web")(inspect)

app.command(name="assess")(assess)

app.command(name="report")(report)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="Show nettools version.",
    ),
) -> None:
    """
    nettools command line interface.
    """

    if version:
        console.print(f"[bold cyan]nettools[/bold cyan] [green]v{__version__}[/green]")
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())
        raise typer.Exit()


@app.command()
def version() -> None:
    """
    Display the current nettools version.
    """

    console.print(f"[bold cyan]nettools[/bold cyan] [green]v{__version__}[/green]")
