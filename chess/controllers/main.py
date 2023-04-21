from chess.views.main import main_menu_view


class Main:

    @classmethod
    def main_menu(cls, payload: dict) -> tuple[str, dict]:
        """ main_menu_controller for the main menu view
        1 : menu joueur
        2 : menu tournois
        q : quitter
        """

        choice = main_menu_view()

        if choice == "1":
            return "players_menu_controller", payload
        elif choice == "2":
            return "tournaments_menu_controller", payload
        elif choice == "q":
            raise KeyboardInterrupt("Bye Bye")

        return "main_menu_controller", payload


class Controller:
    @classmethod
    def players_menu(cls, payload: dict) -> tuple[str, dict]:
        """
        1: liste des joueurs
        2: création joueur
        4: menu principal
        """

        choice = players_menu_view()

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

        choice = players_list_menu_view()

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
        choice = players_list_view(players_list)
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
        choice = search_player_view()  # Renvoi une liste [data, value]
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
        choice = player_submenu_view(player_dict)
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

        choice = player_create_menu_view()  # renvoi[nom,prenom,
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
        choice = player_delete_view()
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
        choice = player_update_view(player_dict)
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

    @classmethod
    def select_tournament(cls, payload: dict) -> tuple[str, dict]:
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

    @classmethod
    def search_tournaments(cls, payload: dict) -> tuple[str, dict]:
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

    @classmethod
    def search_submenu_tournaments(cls, payload):
        """"""
        choice = search_submenu_tournaments_view()
        data = choice[0]
        value = choice[1]
        tournament = Tournament.find_one(data, value)
        payload["tournament_search"] = tournament

        return "searched_tournament_submenu_controller", payload

    @classmethod
    def searched_tournament_submenu(cls, payload: dict) -> tuple[
        str, dict]:
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

    @classmethod
    def search_tournament_score(cls, payload: dict) -> tuple[str, dict]:
        """ """

        tournament = payload["tournament_search"]
        scores = payload["scores_tournament"]
        choice = searched_tournament_score_view(tournament, scores)
        if choice == "4":
            return "searched_tournament_submenu_controller", payload
        elif choice == "q":
            return "main_menu_controller", payload

    @classmethod
    def create_tournament(cls, payload):
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

    @classmethod
    def sub_menu_tournament(cls, payload: dict) -> tuple[str, dict]:
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

    @classmethod
    def started_tournament(cls, payload: dict) -> tuple[str, dict]:
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

    @classmethod
    def next_round(cls, payload: dict) -> tuple[str, dict]:
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

    @classmethod
    def not_continue_round(cls, payload: dict) -> tuple[str, dict]:
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

    @classmethod
    def end_tournament(cls, payload: dict) -> tuple[str, dict]:
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

    @classmethod
    def cancel_round(cls, payload: dict) -> tuple[str, dict]:
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


class View:
    @classmethod
    def main_menu(cls) -> str:
        """
        Affiche le menu principal
        """

        print(
            """
        ------- Menu principal -------
        (1) Menu joueur
        (2) Menu tournois
        (q) Quit
        ------- Menu principal -------
        """
        )

        return input("Choix : ")

    @classmethod
    def players_menu(cls) -> str:
        """Menu joueur

        Returns:
            int: 1 = Affiche menu liste joueur, 2 = Affiche menu création
            joueur,
             4 = View précédente
        """
        print("""
            ------- Menu joueur -------
        (1) Afficher liste des joueurs
        (2) Créer un joueur
        (4) Retour
            ------- Menu joueur -------
        """)

        return input("Choix :")

    @classmethod
    def players_list_menu(cls) -> str:
        """Menu liste joueurs

        Returns: int: 1 = List sorted Alphabétique, 2 = List sorted INE,
        3 = List
        sorted nombre de point actuel,
        4 = View précédente
        """
        print("""
            ------- Menu liste joueurs -------
        (1) Trier par ordre alphabétique
        (2) Trier par INE
        (4) Retour
        (q) Menu Princpal
            ------- Menu liste joueurs -------
        """)
        return input("Choix : ")

    @classmethod
    def players_list(cls, players_list: list[dict]):
        """
        """

        print("""
            ------- Liste joueurs -------
            """)
        pprint(players_list)
        print("""
        (2) Editer un rapport
        (3) Chercher un joueur
        (4) Retour
        (q) Menu principal
            ------- Liste joueurs -------
        """)

        return input("Choix : ")

    @classmethod
    def search_player(cls):
        print("""
            ------- Chercher joueur -------
        """)

        inp1 = input("Entrer la donnée du joueur à chercher : ")
        inp2 = input("Entrer la valeur de cette donnée : ")
        return [inp1, inp2]

    @classmethod
    def player_create_menu(cls):
        """Menu création joueur

        Returns:
            any: Return données et valeurs du joueur à créer
        """
        print("""
            ------- Menu création joueur -------
        (4) Retour
        (q) Menu principal
            ------- Menu création joueur -------
        """)
        nom = input("Taper le nom du joueur : ")
        prenom = input("Taper le prénom du joueur : ")
        date_naissance = input("Taper la date de naissance du joueur : ")
        ine = input("Taper l'INE du joueur : ")
        return [nom, prenom, date_naissance, ine]

    @classmethod
    def player_submenu(cls, player: dict) -> str:
        """
        """
        print(f"""
            ------- Menu joueur -------
        {player}
        (1) Mettre à jour le profil
        (2) Supprimer le joueur
        (3) Générer un rapport
        (4) Retour
        (q) Menu principal
            ------- Menu joueur -------
        """)

        return input("Choix : ")

    @classmethod
    def player_update(cls, player: dict) -> list:
        """
        """
        print(f"""
            ------- Menu joueur -------
        {player}

        (Taper en premier la donnée à mettre à jour, puis la nouvelle
        valeur de cette donnée.)
        (4) Retour
            ------- Menu joueur -------
        """)
        inp1 = input("Entrer la donnée à modifier : ")
        inp2 = input("Entrer la nouvelle valeur : ")
        return [inp1, inp2]

    @classmethod
    def player_delete(cls) -> str:
        """
        """
        print("""
            ------- Menu joueur -------
        (4) Retour
            ------- Menu joueur -------
        """)

        inp = input("Souhaitez-vous vraiment supprimer le joueur ? (y/n) : ")

        return inp

    @classmethod
    def tournaments_menu(cls, n_tournament_running):
        """
        Affiche le menu des tournois
        """
        print(f"""
            ------- Menu Tournois -------
        (1) Créer un tournois
        (2) Accéder à un tournois
        (3) Tournois en cours ({n_tournament_running})
        (4) Retour (Menu principal)
            ------- Menu Tournois -------
        """)

        return input("Choix : ")

    @classmethod
    def select_tournament(cls, tournaments_list, padding=15, sep="|"):
        """ """
        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)}")
        print("----------------------------------------------")
        for d in tournaments_list:
            print(
                f'{d["name"].ljust(padding)} {sep} {d["place"].ljust(padding)} '
                f'{sep} {d["start_date"].ljust(padding)}')
        return input("Nom du tournois à continuer : ")

    @classmethod
    def search_tournaments(cls, tournaments_list, padding=15, sep="|"):
        """ """

        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {sep} "
            f"{'status'.ljust(padding)} {sep}"
            f"{char_replace('players'.ljust(60))} "
        )
        print("----------------------------------------------")
        for d in tournaments_list:
            print(
                f'{d["name"].ljust(padding)} {sep} {d["place"].ljust(padding)} '
                f'{sep} {d["start_date"].ljust(padding)} {sep} '
                f'{d["status"].ljust(padding)} {sep}'
                f'{char_replace(str(d["players_list"]).ljust(60))}'
            )
        print("""
            ------- Accéder à un tournois ------
        (1) Rechercher par attribut / valeur
        (2) Générer un rapport de tous les tournois
        (4) Retour
        (q) Menu principal

            ------- Accéder à un tournois ------
    """)
        return input("Choix : ")

    @classmethod
    def search_submenu_tournaments(cls):
        """ """
        print("""
            ------- Accéder à un tournois ------
        """)
        data = input("Attribut à chercher : ")
        value = input("Valeur de l'attribut : ")
        return data, value

    def char_replace(value):
        char = ["[", "]"]
        for k in char:
            value = str(value).replace(k, "")
        return value

    @classmethod
    def searched_tournament_submenu(cls, tournament, padding=15, sep="|"):
        """ """

        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} "
            f"{sep} "
            f"{'players'.ljust(60)}"
        )
        print("----------------------------------------------")
        print(
            f'{tournament["name"].ljust(padding)} {sep} '
            f'{tournament["place"].ljust(padding)} '
            f'{sep} {tournament["start_date"].ljust(padding)} {sep} '
            f'{tournament["status"].ljust(padding)} {sep}'
            f'{char_replace(str(tournament["players_list"]).ljust(60))}'
        )

        print("""
            ------- Accéder à un tournois ------

        (1) Editer un rapport
        (2) Voir les scores
        (4) Retour
        (q) Menu principal

            ------- Accéder à un tournois ------
        """)
        return input("Choix : ")

    @classmethod
    def searched_tournament_score(cls, tournament, scores, padding=15, sep="|"):
        """ """
        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} "
            f"{sep} "
            f"{'score'.ljust(80)}"
        )
        print("----------------------------------------------")
        print(
            f'{tournament["name"].ljust(padding)} {sep} '
            f'{tournament["place"].ljust(padding)} '
            f'{sep} {tournament["start_date"].ljust(padding)} {sep} '
            f'{tournament["status"].ljust(padding)} {sep}'
            f'{char_replace(str(scores).ljust(80))}'
        )
        print("""
            ------- Accéder à un tournois ------

        (4) Retour
        (q) Menu principal

            ------- Accéder à un tournois ------
        """)
        return input("Choix : ")

    @classmethod
    def tournaments_create(cls):
        """
        Affiche le menu des tournois
        """
        print("""
            ------- Création Tournois -------
    """)
        name = input("Entrer le nom du tournois : ")
        place = input("Entrer le lieu du tournois : ")
        start_date = input("Entrer la date du début du tournois : ")
        end_date = input("Entrer la date de fin du tournois : ")
        desc_choice = input("Souhaitez-vous ajouter une description ? (y/n)")
        desc = ""
        rounds_number_choice = input(
            "Souhaitez-vous définir un nombre de tour ? (y/n) Par défaut : 4")
        rounds_number = "4"
        if desc_choice == "y":
            desc = input("Entrer une description : ")
        if rounds_number_choice == "y":
            rounds_number = input("Entrer le nombre de tour : ")

        logging.warning("Tournois créé")
        return name, place, start_date, end_date, desc, rounds_number

    @classmethod
    def sub_menu_tournament(cls, tournament, padding=15, sep="|"):
        """"""
        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} "
            f"{sep} "
            f"{'players'.ljust(60)}"
        )
        print("----------------------------------------------")
        print(
            f'{tournament.name.ljust(padding)} {sep} '
            f'{tournament.place.ljust(padding)} '
            f'{sep} {tournament.start_date.ljust(padding)} {sep} '
            f'{tournament.status.ljust(padding)} {sep} '
            f'{char_replace(str(tournament.players_list).ljust(80))}'
        )

        print("""
            ------- Création Tournois -------
        (1) Commencer le tournois
        (3) Mettre fin au tournois
        (4) Retour
        (q) Menu principal
            ------- Création Tournois --------
        """)
        return input("Choix : ")

    @classmethod
    def started_tournament(cls, tournament, rounde, padding=15, sep="|"):
        """ """
        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} "
            f"{sep} "
            f"{'players'.ljust(60)}"
        )
        print("----------------------------------------------")
        print(
            f'{tournament.name.ljust(padding)} {sep} '
            f'{tournament.place.ljust(padding)} '
            f'{sep} {tournament.start_date.ljust(padding)} {sep} '
            f'{tournament.status.ljust(padding)} {sep} '
            f'{char_replace(str(tournament.players_list).ljust(80))}'
        )
        print(f"""
            ------- Tournois en cours -------
        Round : {rounde}
        (1) Rentrer les scores pour ce round
        (2) Annuler le round
        (3) Terminer le tournois
        (4) Retour
        (q) Menu principal
            ------- Tournois en cours -------
        """)
        return input("Choix : ")

    @classmethod
    def end_tournament(cls, tournament, player_1, player_2, player_3,
                       padding=15,
                       sep="|"):
        """"""
        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} "
            f"{sep} "
            f"{'players'.ljust(60)}"
        )
        print("----------------------------------------------")
        print(
            f'{tournament.name.ljust(padding)} {sep} '
            f'{tournament.place.ljust(padding)} '
            f'{sep} {tournament.start_date.ljust(padding)} {sep} '
            f'{tournament.status.ljust(padding)} {sep} '
            f'{char_replace(str(tournament.players_list).ljust(80))}'
            f'')
        print(f"""
            ------- Fin du tournois -------

        Tournois terminé !

        Voici le podium :
        {char_replace(player_1)}
        {char_replace(player_2)}
        {char_replace(player_3)}

        (q) Menu principal
            ------- Fin du tournois -------
        """)
        return input("Choix : ")

    @classmethod
    def update_tournament(cls, tournament, padding=15, sep="|"):
        """"""
        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {'end date'.ljust(padding)} "
            f"{'description'.ljust(padding)} {'round number'.ljust(padding)} "
            f"{sep} {'status'.ljust(padding)} {sep} "
            f"{'players'.ljust(60)}"
        )
        print("----------------------------------------------")
        print(
            f'{tournament.name.ljust(padding)} {sep} '
            f'{tournament.place.ljust(padding)} '
            f'{sep} {tournament.start_date.ljust(padding)} '
            f'{tournament.end_date.ljust(padding)} '
            f'{tournament.description.ljust(padding)} '
            f'{tournament.rounds_number.ljust(padding)} {sep} '
            f'{tournament.status.ljust(padding)} {sep} '
            f'{char_replace(str(tournament.players_list).ljust(80))}'
        )
        print("""
            -------- Modification du tournois -------
        (Taper en premier la donnée à mettre à jour, puis la nouvelle
        valeur de cette donnée.)
        (4) Retour
            ------- Modification du tournois -------
        """)
        inp1 = input("Entrer la donnée à modifier : ")
        inp2 = input("Entrer la nouvelle valeur : ")

        return [inp1, inp2]

    @classmethod
    def scores_round(cls, match, padding=15, sep="|"):
        """"""
        print(
            f"{'joueur 1'.ljust(padding)} {sep} {'score'.ljust(padding)} {sep} "
            f"{'joueur 2'.ljust(padding)} {sep} {'score'.ljust(padding)}")
        print("----------------------------------------------")
        print(
            f"{char_replace(match[0][0]).ljust(padding)} {sep} "
            f"{char_replace(str(match[0][1])).ljust(padding)} {sep} "
            f"{char_replace(match[1][0]).ljust(padding)} {sep}"
            f"{char_replace(str(match[1][1])).ljust(padding)}")
        print("""
            ------- Scores -------
            (1) Joueur 1 à gagné
            (2) Joueur 2 à gagné
            (3) Match nul
            ------- Scores -------
            """)
        return input("Choix : ")

    @classmethod
    def next_round(cls, matchs_list, round_number, padding=15, sep="|"):
        """ """
        print(f"{'joueur'} {sep} {'score'}")
        print("----------------------------------------------")
        for match in matchs_list:
            for player in match:
                print(
                    f"{char_replace(str(player[0])).ljust(padding)} {sep} "
                    f"{char_replace(str(player[1])).ljust(padding)}")
        print(f"""
            ------- Scores -------

            Résultats round {round_number}:

            ------- Scores -------
            """)
        return input("Passer au round suivant ? (y/n) : ")

    @classmethod
    def not_continue_round(cls):
        """ """

        print("""
        (1) Menu principal
        (2) Menu joueur
        (3) Menu tournois
        (4) Retour / reprendre le tournois
        """)
        return input("Choix : ")

    @classmethod
    def cancel_round(cls, round):
        """"""
        print(f"""
            ------- Annulation du round -------
        {round}
        (4) Retour
        (q) Menu principal
        """)

        return input("Souhaitez-vous annuler le round ? (y/n)")

    @classmethod
    def cancel_tournament(cls, tournament, padding=15, sep="|"):
        """ """
        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {'end date'.ljust(padding)} "
            f"{'description'.ljust(padding)} {'round number'.ljust(padding)} "
            f"{sep} {'status'.ljust(padding)} {sep} "
            f"{'players'.ljust(60)}"
        )
        print("----------------------------------------------")
        print(
            f'{tournament.name.ljust(padding)} {sep} '
            f'{tournament.place.ljust(padding)} '
            f'{sep} {tournament.start_date.ljust(padding)} '
            f'{tournament.end_date.ljust(padding)} '
            f'{tournament.description.ljust(padding)} '
            f'{tournament.rounds_number.ljust(padding)} {sep} '
            f'{tournament.status.ljust(padding)} {sep} '
            f'{char_replace(str(tournament.players_list).ljust(80))}'
        )
        print("""
            ------- Annulation du tournois -------
        (4) Retour
        (q) Menu principal
        """)
        return input("Souhaitez-vous annuler le tournois ? (y/n)")
