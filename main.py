from chess.controllers.main import main_menu_controller
from chess.controllers.players import *
from chess.controllers.tournaments import *

routes = {
    "main_menu": main_menu_controller,
    "players_menu": players_menu_controller,
    "players_list_menu": players_list_menu_controller,
    "player_create_menu": player_create_menu_controller,
    "tournaments_menu": tournaments_menu_controler,
    "player_remove_menu": player_remove_menu_controller,
    "player_submenu": player_submenu_controller,
}


def main():
    """ """

    controller_key = main_menu_controller()
    while True:
        controller = routes[controller_key]
        controller_key = controller()


if __name__ == "__main__":
    main()
