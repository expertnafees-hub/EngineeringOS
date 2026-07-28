from pathlib import Path
import typer
from rich import print

def init():
    """
    Initialize EngineeringOS Vault.
    """

    vault = Path.home() / "EngineeringOS" / "Knowledge" / "EngineeringVault"

    folders = [
        "01_Cloud",
        "02_Linux",
        "03_Docker",
        "04_Kubernetes",
        "05_Terraform",
        "06_Python",
        "07_Git",
        "08_Networking",
        "09_SystemDesign",
        "Daily",
        "Labs",
        "Projects",
        "Research",
        "Flashcards",
        "Templates",
        "Assets",
    ]

    vault.mkdir(parents=True, exist_ok=True)

    for folder in folders:
        (vault / folder).mkdir(exist_ok=True)

    dashboard = vault / "Dashboard.md"

    if not dashboard.exists():
        dashboard.write_text(
            "# Engineering Dashboard\n\nWelcome to EngineeringOS 🚀\n"
        )

    print(f"[green]✓ Vault initialized:[/green] {vault}")
