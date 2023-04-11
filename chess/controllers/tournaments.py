from chess.views.tournaments import *
from chess.models.tournaments import Tournament
from chess.models.players import Player
from chess.models.round import Round


def tournaments_menu_controller(payload):
    """ """

    tournament_running_list = Tournament.find_all()
    n_tournament_running = len(tournament_running_list)
    choice = tournaments_menu_view(n_tournament_running)
    if choice == "1":
        return "create_tournament_controller", payload
    elif choice == "2":
        return "find_tournament_controller", payload
    elif choice == "3" and n_tournament_running == 1:
        # TODO: tournament running
        tournament_running = Tournament.find_one("status", "running")

        return "started_tournament_controller", payload
    elif choice == "3" and n_tournament_running > 1:
        return "select_tournament_controller", payload
    elif choice == "4":
        return "main_menu_controller", payload


def create_tournament_controller(payload):
    """ """

    data_tournament = tournaments_create_view()
    name = data_tournament[0]
    place = data_tournament[1]
    start_date = data_tournament[2]
    end_date = data_tournament[3]
    desc = data_tournament[4]
    rounds_number = data_tournament[5]
    list_players = [player.ine for player in Player.find_all()]
    tournament = Tournament(name, place, start_date, end_date, players_list=list_players, rounds_number=rounds_number,
                            description=desc)
    tournament.create()
    payload[f"tournament_{name}"] = tournament
    payload["last_tournament"] = tournament

    return "sub_menu_tournament_controller", payload


def sub_menu_tournament_controller(payload):
    tournament = payload["last_tournament"]
    choice = sub_menu_tournament_view(tournament)
    if choice == "1":
        tournament.start_tournament()
        return "started_tournament_controller", payload
    elif choice == "2":
        return "update_tournament_controller", payload
    elif choice == "3":
        return "end_tournament_controller", payload
    elif choice == "4":
        return "create_tournament_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def started_tournament_controller(payload):
    """ """

    tournament = payload["last_tournament"]
    rounde = tournament.current_round
    if tournament.status == "created":
        tournament.start_tournament()
        tournament.update("status", "running")
    if tournament.current_round == -1:
        tournament.create_first_round()
        tournament.update("current_round", 0)
    choice = started_tournament_view(tournament, rounde)
    if choice == "1":
        return "scores_round_controller", payload
    elif choice == "2":
        return "cancel_round_controller", payload
    elif choice == "3":
        return "end_tournament_controller", payload
    elif choice == "4":
        return "sub_menu_tournament_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def scores_round_controller(payload):
    """ """

    tournament = payload["last_tournament"]
    rounde_id = tournament.rounds_list[tournament.current_round]
    rounde = Round.find_one("round_id", rounde_id)
    for match in rounde.matchs_list:
        players_list = match
        choice = scores_round_view(players_list)
        if choice == "1":
            pass
        if choice == "2":
            pass
        if choice == "3":
            pass
        if choice == "4":
            return "started_tournament_controller", payload
        if choice == "5":
            return "main_menu_controller", payload


def upadate_tournament_controller(payload):
    pass


def end_tournament_controller(payload):
    """ """

    tournament = payload["last_tournament"]
    choice = end_tournament_view(tournament)
    if choice == "4":
        return "tournaments_menu_controller", payload
    elif choice == "q":
        return "main_menu_controller", payload


def cancel_round_controller(payload):
    """ """

    tournament = payload["last_tournament"]
    rounde_id = tournament.rounds_list[tournament.current_round]
    rounde = Round.find_one("round_id", rounde_id)
    choice = cancel_round_view(rounde.__dict__)
    if choice == "y":
        rounde.remove_one()
        logging.warning("Round annulé !")
        return "started_tournament_controller", payload
    elif choice == "n":
        return "started_tournament_controller", payload


def cancel_tournament_controller(payload):
    pass
