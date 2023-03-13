from chess.views.player_view import *
from chess.views.main_view import *

from chess.models.players import Player

from chess.controllers.main_controler import *


# table = Player.find_all()


# TODO : Trier les listes d'instance


def players_menu_controler():
    """ """

    choice = players_menu_view()

    if choice == 1:
        return players_list_menu_controler()
    elif choice == 2:
        return player_create_menu_controler()
    elif choice == 4:
        pass

    return main_menu_controller()


def players_list_menu_controler():
    """ """

    choice = players_list_menu_view()

    # query ensemble des datas de player
    # deserialise la liste des players (list de ditc)
    # map choice vs clé 1/alpha, 2/ine etc etc

    # tri de la liste en fonction de la clé
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        return players_menu_controler()

    # call players_list_view()

    # player_submenu_view()

    # soit player_update_view
    # soit player_delete_view

    # go back player menu generique


def player_create_menu_controler():
    """ """

    choice = player_create_menu_view()

    # transform string to dict

    player = Player(**choice)
    player.create()

    # go back player menu
