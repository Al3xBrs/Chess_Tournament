from chess.controllers.main import main_menu_controller
from chess.controllers.players import *
from chess.controllers.tournaments import *

routes = {
    "main_menu_controller": main_menu_controller,
    "players_menu_controller": players_menu_controller,
    "players_list_menu_controller": players_list_menu_controller,
    "players_list_controller": players_list_controller,
    "player_create_menu_controller": player_create_menu_controller,
    "player_remove_menu_controller": player_remove_menu_controller,
    "player_submenu_controller": player_submenu_controller,
    "player_update_controller": player_update_controller,
    "search_player_controller": search_player_controller,

    "tournaments_menu_controller": tournaments_menu_controller,
    "create_tournament_controller": create_tournament_controller,
    "sub_menu_tournament_controller": sub_menu_tournament_controller,
    "started_tournament_controller": started_tournament_controller,
    "cancel_round_controller": cancel_round_controller,
    "scores_round_controller": scores_round_controller,
    "end_tournament_controller": end_tournament_controller,
    "next_round_controller": next_round_controller,

}


def main():
    """ """
    payload = {}
    controller_key, payload = main_menu_controller(payload)
    while True:
        controller = routes[controller_key]
        controller_key, payload = controller(payload)


if __name__ == "__main__":
    main()
