import logging


def tournaments_menu_view(n_tournament_running):
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


def select_tournament_view(tournaments_list, padding=15, sep="|"):
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


def search_tournaments_view(tournaments_list, padding=15, sep="|"):
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


def search_submenu_tournaments_view():
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


def searched_tournament_submenu_view(tournament, padding=15, sep="|"):
    """ """

    print(
        f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
        f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} {sep} "
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


def searched_tournament_score_view(tournament, scores, padding=15, sep="|"):
    """ """
    print(
        f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
        f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} {sep} "
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


def tournaments_create_view():
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


def sub_menu_tournament_view(tournament, padding=15, sep="|"):
    """"""
    print(
        f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
        f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} {sep} "
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


def started_tournament_view(tournament, rounde, padding=15, sep="|"):
    """ """
    print(
        f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
        f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} {sep} "
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


def end_tournament_view(tournament, player_1, player_2, player_3, padding=15,
                        sep="|"):
    """"""
    print(
        f"{'name'.ljust(padding)} {sep} {'place'.ljust(padding)} {sep} "
        f"{'start date'.ljust(padding)} {sep} {'status'.ljust(padding)} {sep} "
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


def update_tournament_view(tournament, padding=15, sep="|"):
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


def scores_round_view(match, padding=15, sep="|"):
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


def next_round_view(matchs_list, round_number, padding=15, sep="|"):
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


def not_continue_round_view():
    """ """

    print("""
    (1) Menu principal
    (2) Menu joueur
    (3) Menu tournois
    (4) Retour / reprendre le tournois
    """)
    return input("Choix : ")


def cancel_round_view(round):
    """"""
    print(f"""
        ------- Annulation du round -------
    {round}
    (4) Retour
    (q) Menu principal
    """)

    return input("Souhaitez-vous annuler le round ? (y/n)")


def cancel_tournament_view(tournament, padding=15, sep="|"):
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
