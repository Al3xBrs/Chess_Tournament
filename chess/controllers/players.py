from chess.models.conf import DATA_PLAYERS
from chess.models.players import Player
from chess.views.players import (
    players_menu_view,
    players_list_menu_view,
    player_create_menu_view,
    player_submenu_view,
    players_list_view,
    player_delete_view,
)
from collections import OrderedDict


def players_menu_controller(payload: dict):
    """ """

    choice = players_menu_view()

    if choice == "1":
        return "players_list_menu_controller", payload
    elif choice == "2":
        return "player_create_menu_controller", payload
    elif choice == "4":
        return "main_menu_controller", payload


def players_list_menu_controller(payload: dict):
    """ """

    choice = players_list_menu_view()

    table = Player.find_all()

    players_list = [player.__dict__ for player in table]

    if choice == "1":
        payload["players_list"] = sorted(players_list, key=lambda t: t["nom"])
        return "players_list_controller", payload
    elif choice == "2":
        payload["players_list"] = sorted(players_list, key=lambda t: t["ine"])
        return "players_list_controller", payload
    elif choice == "4":
        return "players_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def players_list_controller(payload: dict):
    """ """

    players_list = payload["players_list"]

    choice = players_list_view(players_list)

    if choice == "4":
        return "players_list_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload
    else:
        find_player = Player.find_one(choice[0], choice[1])

        player_ine = find_player.ine
        payload["player_ine"]

        return "player_submenu_controller", payload


def player_submenu_controller(payload):
    """ """

    p_ine = payload["player_ine"]
    player_dict = Player.find_one("ine", p_ine).__dict__

    choice = player_submenu_view(player_dict)
    if choice == "1":
        return "player_create_menu", payload
    elif choice == "2":
        return player_remove_menu_controller(find_player)
    elif choice == "4":
        return "players_list_menu"
    elif choice == "q":
        return "main_menu"


def player_create_menu_controller(payload: dict):
    """ """

    choice = player_create_menu_view()

    player = Player(choice[0], choice[1], choice[2], choice[3])
    player.create()
    print("Joueur créé")
    return player_submenu_controller(player)
    # go back player menu


def player_remove_menu_controller(find_player):
    choice = player_delete_view()
    if choice == "4":
        return player_submenu_controller(find_player)
    if choice == "q":
        return "main_menu"
    if choice == "y":
        find_player.remove()
        print("Joueur supprimé")
        return "players_list_menu"
    if choice == "n":
        print("Joueur non supprimé")
        return player_submenu_controller(find_player)
