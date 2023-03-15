from chess.controllers.main import main_menu_controller
from chess.controllers.players import *
from chess.controllers.tournaments import *

routes = {
    # main
    "main_menu_controller": main_menu_controller,
    # players
    "players_menu_controller": players_menu_controller,
    "players_list_menu_controller": players_list_menu_controller,
    "player_create_menu_controller": player_create_menu_controller,
    "tournaments_menu_controler": tournaments_menu_controler,
    "player_remove_menu_controller": player_remove_menu_controller,
    "player_submenu_controller": player_submenu_controller,
    "players_list_controller": players_list_controller,
}


def main():
    """ """

    payload = {}
    controller_key, payload = main_menu_controller(payload)

    while True:
        # controler routes
        controller = routes[controller_key]

        # apply
        controller_key, payload = controller(payload)


if __name__ == "__main__":
    main()
