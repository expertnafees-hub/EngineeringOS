import typer
from rich import print

from engineeringos.commands.init import init
from engineeringos.commands.note import app as note_app

app = typer.Typer(help="EngineeringOS")


@app.command()
def hello():
    """Test command."""
    print("[green]EngineeringOS Running[/green]")


app.command()(init)

app.add_typer(note_app, name="note")


if __name__ == "__main__":
    app()
