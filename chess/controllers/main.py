from chess.controllers.players import *

from chess.views.main import *


def main_menu_controller(payload):
    """main_menu_controller"""

    choice = main_menu_view()

    if choice == "1":
        return "players_menu_controller", payload
    elif choice == "2":
        return "tournaments_menu_controller", payload
    elif choice == "q":
        raise KeyboardInterrupt("Bye Bye")

    return "main_menu_controller", payload
