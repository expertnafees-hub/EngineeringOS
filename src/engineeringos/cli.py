import typer
from rich import print

from engineeringos.commands.init import init

app = typer.Typer(help="EngineeringOS")


@app.command()
def hello():
    """Test command."""
    print("[green]EngineeringOS Running[/green]")


app.command()(init)


if __name__ == "__main__":
    app()
