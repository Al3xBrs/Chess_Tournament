from chess.controllers.players import *

from chess.views.main import *


def main_menu_controller():
    """main_menu_controller"""

    choice = main_menu_view()

    if choice == "1":
        return "players_menu"
    elif choice == "2":
        pass
    elif choice == "q":
        raise KeyboardInterrupt("Bye Bye")

    return "main_menu"
