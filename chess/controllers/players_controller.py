from chess.views.player_view import *
from chess.views.main_view import *
from chess.views.tournament_view import *
from chess.models.players import Player
from chess.controllers.tournaments import *
from chess.controllers.main_controler import *

table = Player.find_all()


# TODO : Trier les listes d'instance


def players_menu_controler():
    choice = players_menu_view()

    if choice == 1:
        return players_list_menu_controler()
    elif choice == 2:
        return player_create_menu_controler()
    elif choice == 4:
        return main_menu_controller()


def players_list_menu_controler():
    choice = players_list_menu_view()

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        return players_menu_controler()


def player_create_menu_controler():
    choice = player_create_menu_view()
    player = Player(choice)
