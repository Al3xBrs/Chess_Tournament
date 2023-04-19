from chess.views.main import main_menu_view


def main_menu_controller(payload: dict) -> tuple[str, dict]:
    """ main_menu_controller for the main menu view
    1 : menu joueur
    2 : menu tournois
    q : quitter
    """

    choice = main_menu_view()

    if choice == "1":
        return "players_menu_controller", payload
    elif choice == "2":
        return "tournaments_menu_controller", payload
    elif choice == "q":
        raise KeyboardInterrupt("Bye Bye")

    return "main_menu_controller", payload
