from pprint import pprint


def players_menu_view() -> str:
    """Menu joueur

    Returns:
        int: 1 = Affiche menu liste joueur, 2 = Affiche menu création joueur, 4 = View précédente
    """
    print("""
        ------- Menu joueur -------
    (1) Afficher liste des joueurs
    (2) Créer un joueur
    (4) Retour
        ------- Menu joueur -------
    """)

    return input("Choix :")


def players_list_menu_view() -> str:
    """Menu liste joueurs

    Returns: int: 1 = List sorted Alphabétique, 2 = List sorted INE, 3 = List sorted nombre de point actuel,
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


def players_list_view(players_list: list[dict]):
    """Affiche la liste des joueurs

    Args:
        players_list: liste des joueurs

    Returns:
        Any: 4 = View précédente, sinon = donnée et valeur du joueur à retrouver
    """

    print("""
        ------- Liste joueurs -------
        """)
    pprint(players_list)
    print("""
    (3) Chercher un joueur
    (4) Retour
    (q) Menu principal
        ------- Liste joueurs -------
    """)

    return input("Choix : ")


def search_player_view():
    print("""
        ------- Chercher joueur -------
    """)

    inp1 = input("Entrer la donnée du joueur à chercher : ")
    inp2 = input("Entrer la valeur de cette donnée : ")
    return [inp1, inp2]


def player_create_menu_view():
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


def player_submenu_view(player: dict) -> str:
    """Menu joueur

    Args:
        player_dict (dict): Donnée du joueur


    Returns:
        Int: 1 = view update player, 2 = view delete player, 4 = View précédente
    """
    print(f"""
        ------- Menu joueur -------
    {player}
    (1) Mettre à jour le profil
    (2) Supprimer le joueur
    (4) Retour
    (q) Menu principal
        ------- Menu joueur -------
    """)

    return input("Choix : ")


def player_update_view(player: dict) -> list:
    """Menu update joueur

    Args:
        player_dict (dict): Donnée du joueur


    Returns:
        any: View précédente si 4, maj du joueur si données.
    """
    print(f"""
        ------- Menu joueur -------
    {player}
    
    \x1B[3m(Taper en premier la donnée à mettre à jour, puis la nouvelle valeur de cette donnée.)\x1B[0m
    (4) Retour
        ------- Menu joueur -------
    """)
    inp1 = input("Entrer la donnée à modifier : ")
    inp2 = input("Entrer la nouvelle valeur : ")
    return [inp1, inp2]


def player_delete_view() -> str:
    """Suppression du joueur




    Returns:
        bool: True if "y", False if "n"
    """
    print(f"""
        ------- Menu joueur -------
    (4) Retour
        ------- Menu joueur -------
    """)

    inp = input("Souhaitez-vous vraiment supprimer le joueur ? (y/n) : ")

    return inp
