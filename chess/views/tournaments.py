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
    rounds_number_choice = input("Souhaitez-vous définir un nombre de tour ? (y/n) Par défaut : 4")
    rounds_number = "4"
    if desc_choice == "y":
        desc = input("Entrer une description : ")
    if rounds_number_choice == "y":
        rounds_number = input("Entrer le nombre de tour : ")

    logging.warning("Tournois créé")
    return name, place, start_date, end_date, desc, rounds_number


def sub_menu_tournament_view(tournament):
    """"""

    print(f"""
        ------- Création Tournois -------
    {tournament}
    (1) Commencer le tournois
    (2) Modifier le tournois / les joueurs
    (3) Mettre fin au tournois
    (4) Retour
    (q) Menu principal 
        ------- Création Tournois --------
    """)
    return input("Choix : ")


def started_tournament_view(tournament, rounde):
    """"""

    print(f"""
        ------- Tournois en cours -------
    {tournament}
    Round : {rounde}
    (1) Rentrer les scores pour ce round
    (2) Annuler le round
    (3) Terminer le tournois
    (4) Retour
    (q) Menu principal 
        ------- Tournois en cours -------
    """)
    return input("Choix : ")


def end_tournament_view(tournament, player_1, player_2, player_3):
    """"""

    print(f"""
        ------- Fin du tournois -------
    {tournament}
    Tournois terminé !
    
    Voici le podium :
    {player_1}
    {player_2}
    {player_3}

    (q) Menu principal
        ------- Fin du tournois -------
    """)
    return input("Choix : ")


def update_tournament_view(tournament):
    """"""

    print(f"""
    -------- Modification du tournois -------
        {tournament}
    
    \x1B[3m(Taper en premier la donnée à mettre à jour, puis la nouvelle valeur de cette donnée.)\x1B[0m
    (4) Retour
        ------- Modification du tournois -------
    """)
    inp1 = input("Entrer la donnée à modifier : ")
    inp2 = input("Entrer la nouvelle valeur : ")

    return [inp1, inp2]


def scores_round_view(match):
    """"""
    print(f"""
        ------- Scores -------
        {match}
        (1) Joueur 1 à gagné
        (2) Joueur 2 à gagné 
        (3) Match nul
        ------- Scores -------
        """)
    return input("Choix : ")


def next_round_view(matchs_list, round_number):
    """ """
    print(f"""
        ------- Scores -------
        
        Résultats round {round_number}:
        {matchs_list}
        
        ------- Scores -------
        """)
    return input("Passer au round suivant ? (y/n) : ")


def cancel_round_view(round):
    """"""
    print(f"""
        ------- Annulation du round -------
    {round}
    (4) Retour
    (q) Menu principal
    """)

    return input("Souhaitez-vous annuler le round ? (y/n)")


def cancel_tournament_view(tournament):
    """ """
    print(f"""
        ------- Annulation du tournois -------
    {tournament}
    (4) Retour
    (q) Menu principal
    """)
    return input("Souhaitez-vous annuler le tournois ? (y/n)")
