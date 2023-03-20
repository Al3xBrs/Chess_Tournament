from chess.models.players import Player
from chess.views.players import players_menu_view, players_list_menu_view, player_create_menu_view, player_submenu_view, \
    players_list_view, player_delete_view, player_update_view, search_player_view
import logging


def players_menu_controller(payload: dict) -> tuple[str, dict]:
    """ """

    choice = players_menu_view()

    if choice == "1":
        return "players_list_menu_controller", payload
    elif choice == "2":
        return "player_create_menu_controller", payload
    elif choice == "4":
        return "main_menu_controller", payload


def players_list_menu_controller(payload):
    """ """

    choice = players_list_menu_view()

    table = Player.find_all()

    players_list = [player.__dict__ for player in table]

    if choice == "1":
        players_list = sorted(players_list, key=lambda t: t["nom"])
        payload["players_list"] = players_list
        return "players_list_controller", payload
    elif choice == "2":
        players_list = sorted(players_list, key=lambda t: t["ine"])
        payload["players_list"] = players_list
        return "players_list_controller", payload
    elif choice == "4":
        return "players_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def players_list_controller(payload):
    """ """
    players_list = payload["players_list"]
    choice = players_list_view(players_list)
    if choice == "4":
        return "players_list_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload
    elif choice == "3":
        return "search_player_controller", payload


def search_player_controller(payload):
    """ """
    choice = search_player_view()
    player = Player.find_one(choice[0], choice[1])
    payload["player"] = player.ine
    return "player_submenu_controller", payload


def player_submenu_controller(payload):
    """ """
    player_ine = payload["player"]
    player = Player.find_one("ine", player_ine)
    player_dict = player.__dict__
    choice = player_submenu_view(player_dict)
    if choice == "1":
        return "player_update_controller", payload
    elif choice == "2":
        return "player_remove_menu_controller", payload
    elif choice == "4":
        return "players_list_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def player_create_menu_controller(payload):
    """ """

    choice = player_create_menu_view()
    player = Player(choice[0], choice[1], choice[2], choice[3])
    player.create()
    logging.warning("Joueur créé")
    payload["player"] = player.ine
    return "player_submenu_controller", payload
    # go back player menu


def player_remove_menu_controller(payload):
    """ """
    choice = player_delete_view()
    player_ine = payload["player"]
    player = Player.find_one("ine", player_ine)
    if choice == "4":
        return "player_submenu_controller", payload
    if choice == "q":
        return "main_menu_controller", payload
    if choice == "y":
        player.remove()
        logging.warning("Joueur supprimé")
        return "players_list_menu_controller", payload
    if choice == "n":
        logging.warning("Joueur non supprimé")
        return "player_submenu_controller", payload


def player_update_controller(payload):
    """ """
    player_ine = payload["player"]
    player = Player.find_one("ine", player_ine)
    player_dict = player.__dict__
    choice = player_update_view(player_dict)
    player.update(choice[0], choice[1])
    logging.warning("Joueur mis à jour")

    return "players_list_menu_controller", payload
