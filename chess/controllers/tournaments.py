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
    if tournament.status == "created" and tournament.current_round == -1:
        tournament.start_tournament()

    elif tournament.current_round == -1 and tournament.status == "running":
        tournament.create_first_round()

    rounde = tournament.current_round

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

    while int(tournament.current_round) < int(tournament.rounds_number):
        rounde_id = tournament.rounds_list[tournament.current_round]
        rounde = Round.find_one("round_id", rounde_id)
        scores_dict = tournament.scores
        scores_list = [[p1, score] for p1, score in scores_dict.items()]
        matchs_list = [scores_list[i:i + 2] for i in range(0, len(scores_list), 2)]
        print(matchs_list)
        # TODO : Mettre à jour score à chaque round
        for match in matchs_list:

            choice = scores_round_view(match)
            if choice == "1":
                match[0][1] += 1

            if choice == "2":
                match[1][1] += 1

            if choice == "3":
                match[0][1] += 0.5
                match[1][1] += 0.5

        rounde.update("matchs_list", matchs_list)
        payload["new_matchs"] = matchs_list
        return "next_round_controller", payload

    return "end_tournament_controller", payload


def next_round_controller(payload):
    """ """
    matchs_list = payload["new_matchs"]
    tournament = payload["last_tournament"]
    round_number = tournament.current_round

    choice = next_round_view(matchs_list, round_number)
    if choice == "y":
        round_id = tournament.rounds_list[round_number]
        rounde = Round.find_one("round_id", round_id)
        rounde.update("matchs_list", matchs_list)
        tournament.next_round()
        return "scores_round_controller", payload

    elif choice == "n":
        return "scores_round_controller", payload

    else:
        logging.warning("Wrong key ! n or y")
        return "next_round_controller", payload


def upadate_tournament_controller(payload):
    pass


def end_tournament_controller(payload):
    """ """

    tournament = payload["last_tournament"]
    last_round = Round.find_one("round_id", tournament.rounds_list[-1])
    player_1 = last_round.matchs_list[0][0]
    player_2 = last_round.matchs_list[0][1]
    player_3 = last_round.matchs_list[1][0]
    choice = end_tournament_view(tournament, player_1, player_2, player_3)

    if choice == "q":
        tournament.end_tournament()
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
