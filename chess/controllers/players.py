from chess.models.conf import DATA_PLAYERS
from chess.models.players import Player
from chess.views.players import players_menu_view, players_list_menu_view, player_create_menu_view, player_submenu_view, \
    players_list_view, player_delete_view
from collections import OrderedDict


def players_menu_controller():
    """ """

    choice = players_menu_view()

    if choice == "1":
        return "players_list_menu"
    elif choice == "2":
        return "player_create_menu"
    elif choice == "4":
        return "main_menu"


def players_list_menu_controller():
    """ """

    choice = players_list_menu_view()

    table = Player.find_all()

    players_list = [player.__dict__ for player in table]

    if choice == "1":
        players_list = sorted(players_list, key=lambda t: t["nom"])
        return players_list_controller(players_list)
    elif choice == "2":
        players_list = sorted(players_list, key=lambda t: t["ine"])
        return players_list_controller(players_list)
    elif choice == "4":
        return "players_menu"
    elif choice == "q":
        return "main_menu"


def players_list_controller(players_list):
    """ """
    choice = players_list_view(players_list)
    if choice == "4":
        return "players_list_menu"
    elif choice == "q":
        return "main_menu"
    else:
        find_player = Player.find_one(choice[0], choice[1])

        return player_submenu_controller(find_player)


def player_submenu_controller(find_player):
    """ """
    player_dict = find_player.__dict__
    choice = player_submenu_view(player_dict)
    if choice == "1":
        return "player_create_menu"
    elif choice == "2":
        return player_remove_menu_controller(find_player)
    elif choice == "4":
        return "players_list_menu"
    elif choice == "q":
        return "main_menu"


def player_create_menu_controller():
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
