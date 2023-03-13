from chess.controllers.players_controller import *

from chess.views.main_view import *


def main_menu_controller():
    """main_menu_controller"""

    choice = main_menu_view()

    if choice == "1":
        return players_menu_controler()
    elif choice == "2":
        pass
    elif choice == "4":
        pass
    elif choice == "q":
        raise KeyboardInterrupt("Bye Bye")

    return main_menu_controller()
