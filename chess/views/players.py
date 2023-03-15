from pprint import pprint


# TODO : Changer print() --> print() """"""


def players_menu_view() -> str:
    """Menu joueur

    Returns:
        int: 1 = Affiche menu liste joueur, 2 = Affiche menu création joueur, 4 = View précédente
    """
    print(
        """
        ------- Menu joueur -------
    (1) Afficher liste des joueurs
    (2) Créer un joueur
    (4) Retour
        ------- Menu joueur -------
    """
    )

    return input("Choix :")


def players_list_menu_view() -> str:
    """Menu liste joueurs

    Returns: int: 1 = List sorted Alphabétique, 2 = List sorted INE, 3 = List sorted nombre de point actuel,
    4 = View précédente
    """
    print(
        """
        ------- Menu liste joueurs -------
    (1) Trier par ordre alphabétique
    (2) Trier par INE
    (4) Retour
    (q) Menu Princpal
        ------- Menu liste joueurs -------
    """
    )
    return input("Choix : ")


def players_list_view(players_list: list[dict]):
    """Affiche la liste des joueurs

    Args:
        players_list: liste des joueurs

    Returns:
        Any: 4 = View précédente, sinon = donnée et valeur du joueur à retrouver
    """
    pprint(players_list)
    print(
        """
        ------- Liste joueurs -------
    (4) Retour
    (q) Menu principal
    (\x1B[3mTaper ’nom’, ’prenom’, ’date_naissance’ ou ’ine’ suivi de ‘, valeur’ à retrouver pour chercher un
    joueur en particulier.\x1B[0m)
    
        ------- Liste joueurs -------
    """
    )
    inp1 = input("Donnée du joueur à chercher : ")
    inp2 = input("Valeur de la donnée à chercher : ")

    return [inp1, inp2]


def player_create_menu_view():
    """Menu création joueur

    Returns:
        any: Return données et valeurs du joueur à créer
    """
    print(
        """
        ------- Menu création joueur -------
    (4) Retour
    (q) Menu principal
        ------- Menu création joueur -------
    """
    )
    nom = input("Taper le nom du joueur : ")
    if nom == "q":
        return False

    prenom = input("Taper le prénom du joueur : ")
    if prenom == "q":
        return False

    date_naissance = input("Taper la date de naissance du joueur : ")
    if date_naissance == "q":
        return False

    ine = input("Taper l'INE du joueur : ")
    if ine == "q":
        return False

    data = [nom, prenom, date_naissance, ine]

    ans = input(f"vous allez creer ce playe : {data}, confirmez vous ? \n y/n")
    if ans == "n":
        return False

    return [nom, prenom, date_naissance, ine]


def player_submenu_view(player_dict: dict) -> str:
    """Menu joueur

    Args:
        player_dict (dict): Donnée du joueur


    Returns:
        Int: 1 = view update player, 2 = view delete player, 4 = View précédente
    """
    print(
        f"""
        ------- Menu joueur -------
    {player_dict}
    (1) Mettre à jour le profil
    (2) Supprimer le joueur
    (4) Retour
    (q) Menu principal
        ------- Menu joueur -------
    """
    )

    return input("Choix : ")


def player_update_view(player_dict: dict) -> str:
    """Menu update joueur

    Args:
        player_dict (dict): Donnée du joueur


    Returns:
        any: View précédente si 4, maj du joueur si données.
    """
    print(
        f"""
        ------- Menu joueur -------
    {player_dict}
    
    \x1B[3m(Taper ’nom’, ’prenom’, ’date_naissance’ ou ’ine’ suivi de ’, valeur’ comme nouvelle valeur à
    renseigner.)\x1B[0m
    (4) Retour
        ------- Menu joueur -------
    """
    )

    return input("Choix : ")


def player_delete_view() -> str:
    """Suppression du joueur




    Returns:
        bool: True if "y", False if "n"
    """
    print(
        f"""
        ------- Menu joueur -------
    (4) Retour
        ------- Menu joueur -------
    """
    )

    inp = input("Souhaitez-vous vraiment supprimer le joueur ? (y/n) : ")

    return inp
