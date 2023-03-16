from chess.models.players import Player
from chess.views.players import players_menu_view, players_list_menu_view, player_create_menu_view, player_submenu_view, \
    players_list_view, player_delete_view, player_update_view, search_player_view


def players_menu_controller(payload: None):
    """ """

    choice = players_menu_view()

    if choice == "1":
        return "players_list_menu_controller", payload
    elif choice == "2":
        return "player_create_menu_controller", payload
    elif choice == "4":
        return "main_menu_controller", payload


def players_list_menu_controller(players_list: list):
    """ """
    payload = {}
    choice = players_list_menu_view()

    table = Player.find_all()

    players_list = [player.__dict__ for player in table]

    if choice == "1":
        players_list = sorted(players_list, key=lambda t: t["nom"])
        return "players_list_controller", players_list
    elif choice == "2":
        players_list = sorted(players_list, key=lambda t: t["ine"])
        return "players_list_controller", players_list
    elif choice == "4":
        return "players_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def players_list_controller(players_list):
    """ """
    payload = {}
    choice = players_list_view(players_list)
    if choice == "4":
        return "players_list_menu_controller", players_list
    elif choice == "q":
        return "main_menu_controller", payload
    elif choice == "3":
        return "search_player_controller", payload


def search_player_controller(payload):
    """ """
    choice = search_player_view()
    player = Player.find_one(choice[0], choice[1])
    return "player_submenu_controller", player


def player_submenu_controller(player):
    """ """
    payload = {}
    player_dict = player.__dict__
    choice = player_submenu_view(player_dict)
    if choice == "1":
        return "player_update_controller", player
    elif choice == "2":
        return "player_remove_menu_controller", player
    elif choice == "4":
        return "players_list_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def player_create_menu_controller(player):
    """ """

    choice = player_create_menu_view()

    player = Player(choice[0], choice[1], choice[2], choice[3])
    player.create()
    print("Joueur créé")
    return "player_submenu_controller", player
    # go back player menu


def player_remove_menu_controller(player):
    """ """
    choice = player_delete_view()
    payload = {}
    if choice == "4":
        return "player_submenu_controller", player
    if choice == "q":
        return "main_menu_controller", payload
    if choice == "y":
        player.remove()
        print("Joueur supprimé")
        return "players_list_menu_controller", payload
    if choice == "n":
        print("Joueur non supprimé")
        return "player_submenu_controller", player


def player_update_controller(player):
    """ """
    players_list = {}
    player_dict = player.__dict__
    choice = player_update_view(player_dict)
    player.update(choice[0], choice[1])
    print("Joueur mis à jour")

    return "players_list_menu_controller", players_list
