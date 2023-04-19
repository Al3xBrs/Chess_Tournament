from chess.views.tournaments import tournaments_menu_view, \
    search_tournaments_view, search_submenu_tournaments_view, \
    searched_tournament_submenu_view, searched_tournament_score_view, \
    tournaments_create_view, sub_menu_tournament_view, \
    started_tournament_view, select_tournament_view, not_continue_round_view, \
    scores_round_view, next_round_view, end_tournament_view, cancel_round_view
from chess.models.tournaments import Tournament
from chess.models.players import Player
from chess.models.round import Round
import logging


def tournaments_menu_controller(payload: dict) -> tuple[str, dict]:
    """ """

    tournaments_list = Tournament.find_all()

    tournament_running_list = []
    for tournament in tournaments_list:

        for key, value in tournament.items():
            if key == "status" and value == "running":
                tournament_running_list.append(tournament)

    n_tournament_running = len(tournament_running_list)
    choice = tournaments_menu_view(n_tournament_running)
    if choice == "1":
        return "create_tournament_controller", payload
    elif choice == "2":
        return "search_tournaments_controller", payload
    elif choice == "3" and n_tournament_running == 1:

        tournament = Tournament.get_instance(tournament_running_list[0])
        round_id = tournament.rounds_list[-1]
        round_find = Round.find_one("round_id", round_id)
        rounde = Round.get_instance(round_find)
        payload["last_tournament"] = tournament
        payload["last_round"] = rounde
        return "started_tournament_controller", payload

    elif choice == "3" and n_tournament_running > 1:
        payload["running_tournaments"] = tournament_running_list
        return "select_tournament_controller", payload
    elif choice == "3" and n_tournament_running == 0:
        logging.warning("Aucun tournois en cours")
        return "tournaments_menu_controller", payload
    elif choice == "4":
        return "main_menu_controller", payload


def select_tournament_controller(payload: dict) -> tuple[str, dict]:
    """ """
    tournaments_list = payload["running_tournaments"]
    choice = select_tournament_view(tournaments_list)
    tournament_choice = Tournament.find_one("name", choice)
    tournament = Tournament.get_instance(tournament_choice)
    round_id = tournament.rounds_list[-1]
    round_find = Round.find_one("round_id", round_id)
    rounde = Round.get_instance(round_find)
    payload["last_tournament"] = tournament
    payload["last_round"] = rounde

    return "started_tournament_controller", payload


def search_tournaments_controller(payload: dict) -> tuple[str, dict]:
    """ """
    tournaments_list = Tournament.find_all()
    choice = search_tournaments_view(tournaments_list)

    if choice == "1":
        return "search_submenu_tournaments_controller", payload

    elif choice == "2":

        with open("./data/Rapports/tournois/tournois.txt", "w") as f:
            for dict_obj in tournaments_list:

                rounds_list = dict_obj["rounds_list"]
                last_round = rounds_list[-1]
                rounde = Round.find_one("round_id", last_round)
                scores = rounde.matchs_list

                for key, value in dict_obj.items():
                    f.write(f"{key.upper()} : {value}")
                    f.write("\n")
                f.write(f"SCORES : {scores}")
                f.write("\n")
                f.write("_____________________________________")
                f.write("\n")

        logging.warning("Rapport généré")
        return "search_tournaments_controller", payload

    elif choice == "4":
        return "tournaments_menu_controller", payload

    elif choice == "q":
        return "main_menu_controller", payload


def search_submenu_tournaments_controller(payload):
    """"""
    choice = search_submenu_tournaments_view()
    data = choice[0]
    value = choice[1]
    tournament = Tournament.find_one(data, value)
    payload["tournament_search"] = tournament

    return "searched_tournament_submenu_controller", payload


def searched_tournament_submenu_controller(payload: dict) -> tuple[str, dict]:
    """ """

    tournament = payload["tournament_search"]

    tournament_list_dict = dict(tournament)

    rounds_list = tournament["rounds_list"]

    last_round = []
    if len(rounds_list) > 0:
        last_round = rounds_list[-1]

    elif len(rounds_list) == 0:

        tournament = Tournament.get_instance(tournament)
        tournament.start_tournament()
        tournament.create_first_round()
        last_round = tournament.rounds_list

    rounde = Round.find_one("round_id", last_round)
    scores = rounde.matchs_list

    choice = searched_tournament_submenu_view(tournament)
    if choice == "1":
        with open(f'./data/Rapports/tournois/{tournament["name"]}.txt',
                  "w") as f:
            for key, value in tournament_list_dict.items():
                f.write(f"{key.upper()} : {value}")
                f.write("\n")
            f.write(f"SCORES : {scores}")

        logging.warning("Tournois enregistré dans 'data/Rapports'")
        return "searched_tournament_submenu_controller", payload
    elif choice == "2":

        payload["scores_tournament"] = scores

        return "search_tournament_score_controller", payload
    elif choice == "4":

        return "search_submenu_tournaments_controller", payload
    elif choice == "q":

        return "main_menu_controller", payload


def search_tournament_score_controller(payload: dict) -> tuple[str, dict]:
    """ """

    tournament = payload["tournament_search"]
    scores = payload["scores_tournament"]
    choice = searched_tournament_score_view(tournament, scores)
    if choice == "4":
        return "searched_tournament_submenu_controller", payload
    elif choice == "q":
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
    tournament = Tournament(name, place, start_date, end_date,
                            players_list=list_players,
                            rounds_number=rounds_number,
                            description=desc)
    tournament.create()
    payload[f"tournament_{name}"] = tournament
    payload["last_tournament"] = tournament

    return "sub_menu_tournament_controller", payload


def sub_menu_tournament_controller(payload: dict) -> tuple[str, dict]:
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


def started_tournament_controller(payload: dict) -> tuple[str, dict]:
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


def scores_round_controller(payload: dict) -> tuple[str, dict]:
    """ """

    tournament = payload["last_tournament"]

    while int(tournament.current_round) < int(tournament.rounds_number):
        rounde_id = tournament.rounds_list[tournament.current_round]
        rounde = Round.find_one("round_id", rounde_id)
        scores_dict = tournament.scores
        scores_list = [[p1, score] for p1, score in scores_dict.items()]
        matchs_list = [scores_list[i:i + 2] for i in
                       range(0, len(scores_list), 2)]

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


def next_round_controller(payload: dict) -> tuple[str, dict]:
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
        return "not_continue_round_controller", payload

    else:
        logging.warning("Wrong key ! n or y")
        return "next_round_controller", payload


def not_continue_round_controller(payload: dict) -> tuple[str, dict]:
    """ """

    choice = not_continue_round_view()
    if choice == "1":
        return "main_menu_controller", payload
    elif choice == "2":
        return "players_menu_controller", payload
    elif choice == "3":
        return "tournaments_menu_controller", payload
    elif choice == "4":
        return "next_round_controller", payload


def end_tournament_controller(payload: dict) -> tuple[str, dict]:
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


def cancel_round_controller(payload: dict) -> tuple[str, dict]:
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
