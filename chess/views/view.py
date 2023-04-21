import logging
from pprint import pprint


class UserView:
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
                f'{d["name"].ljust(padding)} {sep} '
                f'{d["place"].ljust(padding)} '
                f'{sep} {d["start_date"].ljust(padding)}')
        return input("Nom du tournois à continuer : ")

    @classmethod
    def char_replace(cls, value):
        char = ["[", "]"]
        for k in char:
            value = str(value).replace(k, "")
        return value

    @classmethod
    def search_tournaments(cls, tournaments_list, padding=15, sep="|"):
        """ """

        print(
            f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
            f"{'start date'.ljust(padding)} {sep} "
            f"{'status'.ljust(padding)} {sep}"
            f"{cls.char_replace('players'.ljust(60))} "
        )
        print("----------------------------------------------")
        for d in tournaments_list:
            print(
                f'{d["name"].ljust(padding)} {sep} '
                f'{d["place"].ljust(padding)} '
                f'{sep} {d["start_date"].ljust(padding)} {sep} '
                f'{d["status"].ljust(padding)} {sep}'
                f'{cls.char_replace(str(d["players_list"]).ljust(60))}'
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
            f'{cls.char_replace(str(tournament["players_list"]).ljust(60))}'
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
    def searched_tournament_score(cls, tournament, scores,
                                  padding=15, sep="|"):
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
            f'{cls.char_replace(str(scores).ljust(80))}'
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
            f'{cls.char_replace(str(tournament.players_list).ljust(80))}'
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
            f'{cls.char_replace(str(tournament.players_list).ljust(80))}'
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
            f'{cls.char_replace(str(tournament.players_list).ljust(80))}'
            f'')
        print(f"""
            ------- Fin du tournois -------

        Tournois terminé !

        Voici le podium :
        {cls.char_replace(player_1)}
        {cls.char_replace(player_2)}
        {cls.char_replace(player_3)}

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
            f'{cls.char_replace(str(tournament.players_list).ljust(80))}'
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
            f"{'joueur 1'.ljust(padding)} {sep} {'score'.ljust(padding)} "
            f"{sep} "
            f"{'joueur 2'.ljust(padding)} {sep} {'score'.ljust(padding)}")
        print("----------------------------------------------")
        print(
            f"{cls.char_replace(match[0][0]).ljust(padding)} {sep} "
            f"{cls.char_replace(str(match[0][1])).ljust(padding)} {sep} "
            f"{cls.char_replace(match[1][0]).ljust(padding)} {sep}"
            f"{cls.char_replace(str(match[1][1])).ljust(padding)}")
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
                    f"{cls.char_replace(str(player[0])).ljust(padding)} {sep} "
                    f"{cls.char_replace(str(player[1])).ljust(padding)}")
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
            f'{cls.char_replace(str(tournament.players_list).ljust(80))}'
        )
        print("""
            ------- Annulation du tournois -------
        (4) Retour
        (q) Menu principal
        """)
        return input("Souhaitez-vous annuler le tournois ? (y/n)")
