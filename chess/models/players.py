from tinydb import Query
from chess.models.conf import DATA_PLAYERS


class Player:
    """
    Joueur.
    """

    def __init__(self, nom, prenom, date_naissance, ine):
        """Initialisation du joueur.

        Args:
            nom (str): nom du joueur
            prenom (str): prenom du joueur
            date_naissance (int): age du joueur
            ine (str): Identification National d'échec
        """

        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.ine = ine

    def create(self):
        """
        Creation de la fiche du joueur dans la db.
        """

        data_players = DATA_PLAYERS
        player_dict = {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "ine": self.ine,
        }
        data_players.insert(player_dict)

    @classmethod
    def find_all(cls):
        """Charge la db de tous les joueurs.

        Returns:
            dict: Liste des joueurs et leurs attributs. 
        """
        data_players = DATA_PLAYERS
        return data_players.all()

    def remove(ine):
        """Suppression du joueur.

        Args:
            player (ine): Identifiant National d'Echec
        """
        data_players = DATA_PLAYERS
        User = Query()
        data_players.remove(User.ine == ine)

    @classmethod
    def remove_all(cls):
        """
        Supprime toute la db.
        """
        data_players = DATA_PLAYERS
        data_players.truncate()

    @classmethod
    def find_one(cls, data, value):
        """Charge la db d'un joueur.

        Args:
            data (str): Nom de la donnée du joueur.
            value (any): Valeur de la donnée du joueur.

        Returns:
            list: Données du joueurs trouvé. [] si aucun trouvé.
        """

        data_players = DATA_PLAYERS
        User = Query()
        return data_players.search(User[data] == value)

    @classmethod
    def update(cls, user_data, user_value, value_to_change):
        """Update la fiche joueur.

        Args:
            user_data (str): Donnée du joueur à changer.
            user_value (any): Valeur du joueur à changer.
            value_to_change (any): Nouvelle valeur.
        """

        data_players = DATA_PLAYERS
        User = Query()
        data_players.update({user_data: value_to_change},
                            User[user_data] == user_value)
