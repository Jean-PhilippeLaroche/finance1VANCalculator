from calculateur_van import CalculateurVAN
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def main():
    console.print(Panel("[bold cyan]Calculateur de VAN[/bold cyan]", expand=False))

    van = CalculateurVAN()

    # Créer un tableau pour les étapes
    table = Table(title="Valeur Actualisée par Étape", show_lines=True)
    table.add_column("Étape", justify="center", style="bold yellow")
    table.add_column("Valeur", justify="right", style="bold green")

    table.add_row("Étape 1", f"{van.valeur_etape_1():.2f}")
    table.add_row("Étape 2", f"{van.valeur_etape_2():.2f}")
    table.add_row("Étape 3", f"{van.valeur_etape_3():.2f}")
    table.add_row("Étape 4-5", f"{van.valeur_etape_4_5():.2f}")
    table.add_row("Étape 6", f"{van.valeur_etape_6():.2f}")
    table.add_row("Étape 7-8", f"{van.valeur_etape_7_8() if van.valeur_etape_7_8() is not None else 'N/A':.2f}")
    table.add_row("Valeur Totale", f"{van.valeur_totale():.2f}")

    console.print(table)

    input("\nAppuyez sur Entrée pour quitter...")


if __name__ == "__main__":
    main()