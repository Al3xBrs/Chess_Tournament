import logging


def tournaments_menu_view():
    """
    Affiche le menu des tournois
    """
    print("""
        ------- Menu Tournois -------
    (1) Créer un tournois
    (2) Accéder à un tournois
    (3) 
    (4) Retour 
        ------- Menu Tournois -------
    """)

    return int(input("Choix : "))


def tournaments_create_view():
    """
    Affiche le menu des tournois
    """
    print("""
        ------- Création Tournois -------
    (4) Retour 
    (q) Menu principal
        ------- Création Tournois -------
    """)
    name = input("Entrer le nom du tournois : ")
    place = input("Entrer le lieu du tournois : ")
    start_place = input("Entrer la date du début du tournois : ")
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
    return name, place, start_place, end_date, desc, rounds_number


def add_players_tournaments_view(tournament):
    """"""

    print(f"""
        ------- Création Tournois -------
    {tournament}
    (1) Commencer le tournois
    (2) Modifier le tournois
    (3) Mettre fin au tournois
    (4) Retour
    (q) Menu principal 
        ------- Création Tournois --------
    """)
    return input("Choix : ")


def started_tournament_view(tournament, round):
    """"""

    print(f"""
        ------- Tournois en cours -------
    {tournament}
    {round}
    (1) Rentrer les scores pour ce round
    (2) Annuler le round
    (3) Terminer le tournois
    (4) Retour
    (q) Menu principal 
        ------- Tournois en cours -------
    """)
    return input("Choix : ")


def end_tournament_view(tournament):
    """"""

    print(f"""
        ------- Fin du tournois -------
    {tournament}
    Tournois terminé !
    
    (4) Retour
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


def scores_round_view(players_list):
    """"""
    print(f"""
        ------- Scores -------
        {players_list}
        (1) Joueur 1 à gagné
        (2) Joueur 2 à gagné 
        (3) Match nul
        (4) Retour
        (q) Menu principal 
        ------- Scores -------
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
