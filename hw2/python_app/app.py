import pathlib
import os

from rich.console import Console
from rich.prompt import Prompt, FloatPrompt
from rich.table import Table

from db import DBManager, Boardgame, Designer

def display_designers(title: str, designers: list[Designer]) -> None:
    """
    Display a list of designers in an easy to read table. Parameters:
        title: str                      Title of table for display. designers:
        list[Designer]           List of Designer objects.

    Returns: Nothing, prints output to screen.
    """

    console = Console()

    table = Table(show_header=True, header_style="bold green", title=title)
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Country")
    
    for designer in designers:
        table.add_row(
            str(designer.id),
            str(designer.name),
            str(designer.country)
        )

    console.print(table)



def display_games(title: str, games: list[Boardgame], 
                  includes_designer: bool =False) -> None:
    """
    Display a list of boardgames in an easy to read table.

    Parameters:
        title: str                Title of table for display. games:
        list[Boardgame]    List of Boardgame objects. includes_designer: bool
        Whether to include the designer in the table.

    Returns: Nothing, prints output to screen.
    """
    console = Console()

    table = Table(show_header=True, header_style="bold magenta", title=title)
    table.add_column("ID")
    table.add_column("Name")
    if includes_designer:
        table.add_column("Designer")
    table.add_column("Average Score", justify="right")
    table.add_column("Min Players", justify="right")
    table.add_column("Max Players", justify="right")
    table.add_column("Min Playtime", justify="right")
    table.add_column("Max Playtime", justify="right")
    
    for game in games:
        row_data = []
        row_data.append(str(game.id))
        row_data.append(str(game.name))
        if includes_designer:
            row_data.append(str(game.designer))
        row_data.append(str(game.avgscore))
        row_data.append(str(game.minplayers))
        row_data.append(str(game.maxplayers))
        row_data.append(str(game.minplaytime))
        row_data.append(str(game.maxplaytime))

        table.add_row(*row_data)

    console.print(table)


def main():
    
    # TODO: Set up the DB connection here
    db_manager = DBManager(None, None, None, None)

    which = Prompt.ask(
            "Show all [bold]\[g][/]ames, [bold]\[d][/]esigners, or [bold]\[s][/]search? (Or E[bold]\[x][/]it.)",
            choices=["g", "d", "s", "x"],
        )

    if which == "x":
        db_manager.close()
        exit()
    elif which == "g":
        games = db_manager.get_all_games()
        display_games("All Boardgames", games)
    elif which == "d":
        designers = db_manager.get_all_designers()
        display_designers("All Designers", designers)
    elif which == "s":
        while True:
            search_type = Prompt.ask("Search by game [bold]\[n][/]ame, [bold]\[d][/]esigner (Or go [bold]\[b][/]ack.)", choices=["n", "d", "b"])
            if search_type == "n":
                name = Prompt.ask("Enter a game name to search for")
                games = db_manager.get_games_by_name(name)
                display_games("Games by Name", games)
            elif search_type == "d":
                designer = Prompt.ask("Enter a designer name to search for")
                games = db_manager.get_games_by_designer(designer)
                display_games("Games by Designer", games, includes_designer=True)
            elif search_type == "b":
                break
            

if __name__ == "__main__":
    main()
