import typer
from rich import print

from engineeringos.services.note_service import NoteService

app = typer.Typer(help="Create engineering notes")


@app.command("create")
def create(title: str):
    """
    Create a new engineering note.
    """
    service = NoteService()

    filepath = service.create_note(title)

    print(f"[bold green]✓ Note created:[/bold green] {filepath}")
