from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class NoteService:
    def __init__(self):
        self.vault = (
            Path.home()
            / "EngineeringOS"
            / "Knowledge"
            / "EngineeringVault"
        )

        self.template_dir = (
            Path(__file__).parent.parent / "templates"
        )

        self.env = Environment(
            loader=FileSystemLoader(self.template_dir)
        )

    def create_note(self, title: str):
        template = self.env.get_template("note.md.j2")

        content = template.render(title=title.replace("-", " ").title())

        notes_dir = self.vault / "Research"
        notes_dir.mkdir(parents=True, exist_ok=True)

        filename = title.lower().replace(" ", "-") + ".md"

        filepath = notes_dir / filename

        filepath.write_text(content, encoding="utf-8")

        return filepath
