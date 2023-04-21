from chess.controllers.controller import Controller

routes = {
    "main_menu_controller": Controller.main_menu,
    "players_menu_controller": Controller.players_menu,
    "players_list_menu_controller": Controller.players_list_menu,
    "players_list_controller": Controller.players_list,
    "player_create_menu_controller": Controller.player_create_menu,
    "player_remove_menu_controller": Controller.player_remove_menu,
    "player_submenu_controller": Controller.player_submenu,
    "player_update_controller": Controller.player_update,
    "search_player_controller": Controller.search_player,

    "tournaments_menu_controller": Controller.tournaments_menu,
    "create_tournament_controller": Controller.create_tournament,
    "sub_menu_tournament_controller": Controller.sub_menu_tournament,
    "started_tournament_controller": Controller.started_tournament,
    "not_continue_round_controller": Controller.not_continue_round,
    "cancel_round_controller": Controller.cancel_round,
    "scores_round_controller": Controller.scores_round,
    "end_tournament_controller": Controller.end_tournament,
    "next_round_controller": Controller.next_round,
    "search_tournaments_controller": Controller.search_tournaments,
    "search_submenu_tournaments_controller":
        Controller.search_submenu_tournaments,
    "searched_tournament_submenu_controller":
        Controller.searched_tournament_submenu,
    "search_tournament_score_controller":
        Controller.search_tournament_score,
    "select_tournament_controller": Controller.select_tournament,

}


def main():
    """ """
    payload = {}
    controller_key, payload = Controller.main_menu(payload)
    while True:
        controller = routes[controller_key]
        controller_key, payload = controller(payload)


if __name__ == "__main__":
    main()
