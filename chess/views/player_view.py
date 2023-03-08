from chess.models.players import Player
from pprint import pprint


def players_menu_view():
    """Menu joueur

    Returns:
        int: 1 = Affiche menu liste joueur, 2 = Affiche menu création joueur, 4 = View précédente
    """
    print("------- Menu joueur -------")
    print("(1) Afficher liste des joueurs")
    print("(2) Créer un joueur")
    print("(4) Retour")
    print("------- Menu joueur -------")

    return input("Choix : ")


def players_list_menu_view():
    """Menu liste joueurs

    Returns:
        int: 1 = List sorted Alphabétique, 2 = List sorted INE, 3 = List sorted nombre de point actuel, 4 = View précédente
    """
    print("------- Menu liste joueurs -------")
    print("(1) Trier par ordre alphabétique")
    print("(2) Trier par INE")
    print("(3) Trier par nombre de point")
    print("(4) Retour")
    print("------- Menu liste joueurs -------")

    return input("Choix : ")


def players_list_view(i):
    """Affiche la liste des joueurs

    Args:
        i (int): 1 = List sorted Alphabétique, 2 = List sorted INE, 3 = List sorted par nombre de point en cours)

    Returns:
        Any: 4 = View précédente, sinon = donnée et valeur du joueur à retrouver
    """
    print("------- Liste joueurs -------")
    print("(4) Retour")
    print("(\x1B[3mTaper ’nom’, ’prenom’, ’date_naissance’ ou ’ine’ suivi de ‘, valeur’ à retrouver pour chercher un joueur en particulier.\x1B[0m)")
    list_players = Player.find_all().__dict__
    print(list_players)
    if i == 1:
        sorted(list_players.items(), key=lambda t: t[0])
    if i == 2:
        sorted(list_players, key=lambda t: t[3])
    if i == 3:
        sorted(list_players, key=lambda t: t[4])

    print("------- Liste joueurs -------")

    return input("Choix : ")


def player_create_menu_view():
    """Menu création joueur

    Returns:
        any: Return données et valeurs du joueur à créer
    """
    print("------- Menu création joueur -------")
    print("(4) Retour")
    print("\x1B[3m(Taper les informations du joueur)\x1B[0m]")
    print("'nom', 'prenom', 'date de naissance, 'INE'")
    print("------- Menu création joueur -------")

    return input("Choix : ")


def player_menu_view(data, value):
    """Menu joueur

    Args:
        data (str): Donnée du joueur
        value (any): Valeur de la donnée joueur

    Returns:
        Int: 1 = view update player, 2 = view delete player, 4 = View précédente
    """
    print("------- Menu joueur -------")
    pprint(Player.find_one(data, value), sort_dicts=False)
    print("(1) Mettre à jour le profil")
    print("(2) Supprimer le joueur")
    print("(4) Retour")
    print("------- Menu joueur -------")

    return input("Choix : ")


def player_update_view(data, value):
    """Menu update joueur

    Args:
        data (str): Donnée du joueur
        value (any): Valeur de la donnée joueur

    Returns:
        any: View précédente si 4, maj du joueur si données.
    """
    print("------- Menu joueur -------")
    pprint(Player.find_one(data, value), sort_dicts=False)
    print("\x1B[3m(Taper ’nom’, ’prenom’, ’date_naissance’ ou ’ine’ suivi de ’, valeur’ comme nouvelle valeur à renseigner.)\x1B[0m")
    print("(4) Retour")
    print("------- Menu joueur -------")

    return input("Choix : ")


def player_delete_view(data, value):
    """Suppression du joueur

    Args:
        data (str): Donnée du joueur
        value (any): Valeur de la donnée joueur

    Returns:
        bool: True if "y", False if "n"
    """
    print("------- Menu joueur -------")
    pprint(Player.find_one(data, value), sort_dicts=False)
    print("(4) Retour")
    print("------- Menu joueur -------")

    inp = input("Souhaitez-vous vraiment supprimer le joueur ? (y/n) : ")
    if inp == "y":

        return True
    if inp == "n":

        return False
