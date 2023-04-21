from chess.models.players import Player
from chess.views.view import UserView
import logging
from chess.models.tournaments import Tournament
from chess.models.round import Round


class Controller:
    @classmethod
    def main_menu(cls, payload: dict) -> tuple[str, dict]:
        """ main_menu_controller for the main menu view
        1 : menu joueur
        2 : menu tournois
        q : quitter
        """

        choice = UserView.main_menu()

        if choice == "1":
            return "players_menu_controller", payload
        elif choice == "2":
            return "tournaments_menu_controller", payload
        elif choice == "q":
            raise KeyboardInterrupt("Bye Bye")

        return "main_menu_controller", payload

    @classmethod
    def players_menu(cls, payload: dict) -> tuple[str, dict]:
        """
        1: liste des joueurs
        2: création joueur
        4: menu principal
        """

        choice = UserView.players_menu()

        if choice == "1":
            return "players_list_menu_controller", payload
        elif choice == "2":
            return "player_create_menu_controller", payload
        elif choice == "4":
            return "main_menu_controller", payload

    @classmethod
    def players_list_menu(cls, payload: dict) -> tuple[str, dict]:
        """
        liste joueurs :

        1: triée par nom
        2: triée par ine du joueur
        4: retour -> menu joueur
        q: menu principal
        """

        choice = UserView.players_list_menu()

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

    @classmethod
    def players_list(cls, payload: dict) -> tuple[str, dict]:
        """
        2: génère un rapport de la liste .txt
        3: menu de recherche d'un joueur
        4: retour -> tris liste
        q: menu principal
        """
        players_list = payload["players_list"]
        choice = UserView.players_list(players_list)
        if choice == "4":
            return "players_list_menu_controller", payload
        elif choice == "q":
            return "main_menu_controller", payload
        elif choice == "3":
            return "search_player_controller", payload
        elif choice == "2":
            logging.warning("Rapport généré")
            with open("./data/Rapports/joueurs/joueurs.txt", "w") as f:
                f.write("Liste de joueurs :\n")
                for player in players_list:
                    for key, value in player.items():
                        f.write(f"{key.upper()} : {value}")
                        f.write("\n")
                    f.write("\n")
            return "players_list_controller", payload

    @classmethod
    def search_player(cls, payload: dict) -> tuple[str, dict]:
        """
        utilise la fonction find_one de la class Player pour le chercher.
        l'user rentre d'abord l'attribut à chercher, puis sa valeur:
        ex: choix 1: nom, choix 2: JEAN
        """
        choice = UserView.search_player()  # Renvoi une liste [data, value]
        player = Player.find_one(choice[0], choice[1])
        payload["player"] = player.ine
        return "player_submenu_controller", payload

    @classmethod
    def player_submenu(cls, payload: dict) -> tuple[str, dict]:
        """
        sous menu joueur
        1: maj de la fiche joueur
        2: suppression du joueur
        3: génère un rapport ine_du_joueur.txt
        4: retour liste joueur
        q: menu principal
        """
        player_ine = payload["player"]
        player = Player.find_one("ine", player_ine)
        player_dict = player.__dict__
        choice = UserView.player_submenu(player_dict)
        if choice == "1":
            return "player_update_controller", payload
        elif choice == "2":
            return "player_remove_menu_controller", payload
        elif choice == "3":
            with open(f"./data/Rapports/joueurs/{player_ine}.txt", "w") as f:
                f.write("Données joueur :\n")
                for key, value in player_dict.items():
                    f.write(f"{key.upper()} : {value}")
                    f.write("\n")
            logging.warning("Rapport généré")
            return "player_submenu_controller", payload
        elif choice == "4":
            return "players_list_menu_controller", payload
        elif choice == "q":
            return "main_menu_controller", payload

    @classmethod
    def player_create_menu(cls, payload: dict) -> tuple[str, dict]:
        """
        création du joueur
        """

        choice = UserView.player_create_menu()  # renvoi[nom,prenom,
        # date_naissance,ine]
        player = Player(choice[0], choice[1], choice[2], choice[3])
        player.create()
        logging.warning("Joueur créé")
        payload["player"] = player.ine
        return "player_submenu_controller", payload
        # sous menu du joueur créé à l'instant

    @classmethod
    def player_remove_menu(cls, payload: dict) -> tuple[str, dict]:
        """
        suppression du joueur
        y: suppr
        n: annul
        4: retour
        q: menu principal
        """
        choice = UserView.player_delete()
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

    @classmethod
    def player_update(cls, payload: dict) -> tuple[str, dict]:
        """
        menu maj joueur
        """
        player_ine = payload["player"]
        player = Player.find_one("ine", player_ine)  # on recherche le joueur
        player_dict = player.__dict__
        choice = UserView.player_update(player_dict)
        player.update(choice[0], choice[1])  # data, value
        logging.warning("Joueur mis à jour")

        return "players_list_menu_controller", payload

    # Tournament
    @classmethod
    def tournaments_menu(cls, payload: dict) -> tuple[str, dict]:
        """ """

        tournaments_list = Tournament.find_all()

        tournament_running_list = []
        for tournament in tournaments_list:

            for key, value in tournament.items():
                if key == "status" and value == "running":
                    tournament_running_list.append(tournament)

        n_tournament_running = len(tournament_running_list)
        choice = UserView.tournaments_menu(n_tournament_running)
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

    @classmethod
    def select_tournament(cls, payload: dict) -> tuple[str, dict]:
        """ """
        tournaments_list = payload["running_tournaments"]
        choice = UserView.select_tournament(tournaments_list)
        tournament_choice = Tournament.find_one("name", choice)
        tournament = Tournament.get_instance(tournament_choice)
        round_id = tournament.rounds_list[-1]
        round_find = Round.find_one("round_id", round_id)
        rounde = Round.get_instance(round_find)
        payload["last_tournament"] = tournament
        payload["last_round"] = rounde

        return "started_tournament_controller", payload

    @classmethod
    def search_tournaments(cls, payload: dict) -> tuple[str, dict]:
        """ """
        tournaments_list = Tournament.find_all()
        choice = UserView.search_tournaments(tournaments_list)

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

    @classmethod
    def search_submenu_tournaments(cls, payload):
        """"""
        choice = UserView.search_submenu_tournaments()
        data = choice[0]
        value = choice[1]
        tournament = Tournament.find_one(data, value)
        payload["tournament_search"] = tournament

        return "searched_tournament_submenu_controller", payload

    @classmethod
    def searched_tournament_submenu(cls, payload: dict) -> tuple[str, dict]:
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

        choice = UserView.searched_tournament_submenu(tournament)
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

    @classmethod
    def search_tournament_score(cls, payload: dict) -> tuple[str, dict]:
        """ """

        tournament = payload["tournament_search"]
        scores = payload["scores_tournament"]
        choice = UserView.searched_tournament_score(tournament, scores)
        if choice == "4":
            return "searched_tournament_submenu_controller", payload
        elif choice == "q":
            return "main_menu_controller", payload

    @classmethod
    def create_tournament(cls, payload):
        """ """

        data_tournament = UserView.tournaments_create()
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

    @classmethod
    def sub_menu_tournament(cls, payload: dict) -> tuple[str, dict]:
        tournament = payload["last_tournament"]
        choice = UserView.sub_menu_tournament(tournament)
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

    @classmethod
    def started_tournament(cls, payload: dict) -> tuple[str, dict]:
        """ """
        tournament = payload["last_tournament"]
        if tournament.status == "created" and tournament.current_round == -1:
            tournament.start_tournament()

        elif tournament.current_round == -1 and tournament.status == "running":
            tournament.create_first_round()

        rounde = tournament.current_round

        choice = UserView.started_tournament(tournament, rounde)
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

    @classmethod
    def scores_round(cls, payload: dict) -> tuple[str, dict]:
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

                choice = UserView.scores_round(match)
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

    @classmethod
    def next_round(cls, payload: dict) -> tuple[str, dict]:
        """ """
        matchs_list = payload["new_matchs"]
        tournament = payload["last_tournament"]
        round_number = tournament.current_round

        choice = UserView.next_round(matchs_list, round_number)
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

    @classmethod
    def not_continue_round(cls, payload: dict) -> tuple[str, dict]:
        """ """

        choice = UserView.not_continue_round()
        if choice == "1":
            return "main_menu_controller", payload
        elif choice == "2":
            return "players_menu_controller", payload
        elif choice == "3":
            return "tournaments_menu_controller", payload
        elif choice == "4":
            return "next_round_controller", payload

    @classmethod
    def end_tournament(cls, payload: dict) -> tuple[str, dict]:
        """ """

        tournament = payload["last_tournament"]
        last_round = Round.find_one("round_id", tournament.rounds_list[-1])
        player_1 = last_round.matchs_list[0][0]
        player_2 = last_round.matchs_list[0][1]
        player_3 = last_round.matchs_list[1][0]
        choice = UserView.end_tournament(tournament, player_1, player_2,
                                         player_3)

        if choice == "q":
            tournament.end_tournament()
            return "main_menu_controller", payload

    @classmethod
    def cancel_round(cls, payload: dict) -> tuple[str, dict]:
        """ """

        tournament = payload["last_tournament"]
        rounde_id = tournament.rounds_list[tournament.current_round]
        rounde = Round.find_one("round_id", rounde_id)
        choice = UserView.cancel_round(rounde.__dict__)
        if choice == "y":
            rounde.remove_one()
            logging.warning("Round annulé !")
            return "started_tournament_controller", payload
        elif choice == "n":
            return "started_tournament_controller", payload
