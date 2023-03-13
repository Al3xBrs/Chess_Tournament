from chess.controllers.players_controller import *
from chess.controllers.tournaments import *
from chess.views.main_view import *


def main_menu_controller():
    choice = main_menu()

    if choice == 1:
        return players_menu_controler()
    elif choice == 2:
        return tournaments_menu_controler()
    elif choice == 4:
        return main_menu_controller()
