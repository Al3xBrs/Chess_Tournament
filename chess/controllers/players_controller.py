from chess.views.player_view import players_menu_view
from chess.views.main_view import main_menu
from chess.views.tournament_view import tournaments_menu


def show_main_menu_view():
    return main_menu()


def show_menu(i):
    if i == 1:
        return players_menu_view()
    if i == 2:
        return tournaments_menu()
