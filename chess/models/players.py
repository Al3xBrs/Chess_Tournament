from tinydb import Query
from chess.models.conf import DATA_PLAYERS


class Player:
    """
    Joueur.
    """

    table = DATA_PLAYERS

    def __init__(
            self,
            nom: str,
            prenom: str,
            date_naissance: str,
            ine: str,
            score: int = 0,

    ) -> None:
        """Initialisation du joueur.

        Args:
            nom (str): nom du joueur
            prenom (str): prenom du joueur
            date_naissance (int): age du joueur
            ine (str): Identification National d'échec
            score(int): Point du joueur, 0 par défaut
        """

        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.ine = ine
        self.score = score

    def create(self):
        """
        Creation de la fiche du joueur dans la db.
        """

        self.table.insert(self.__dict__)

    @classmethod
    def find_all(cls):
        """Charge la db de tous les joueurs.

        Returns:
            list_instance: Liste des joueurs.
        """

        list_doc = cls.table.all()
        list_dict = [dict(doc) for doc in list_doc]
        list_instance = [Player(**p_dict) for p_dict in list_dict]

        return list_instance

    @classmethod
    def find_one(cls, data, value):
        """Charge la db d'un joueur.

        Args:
            data (str): Nom de la donnée du joueur.
            value (any): Valeur de la donnée du joueur.

        Returns:
            list: Données du joueurs trouvé. [] si aucun trouvé.
        """

        # query
        User = Query()
        p_list = cls.table.search(User[data] == value)

        p_list = [Player(**i) for i in p_list]

        # we want only 1 player
        if len(p_list) != 1:
            raise AttributeError("more than 1 player")

        return p_list[0]

    def remove(self):
        """Suppression du joueur."""

        User = Query()
        self.table.remove(User.ine == self.ine)

    @classmethod
    def remove_all(cls):
        """
        Supprime toute la db.
        """

        cls.table.truncate()

    def update(self, user_value, value_to_change):
        """Update la fiche joueur.

        Args:

            user_value (any): Valeur du joueur à changer.
            value_to_change (any): Nouvelle valeur.
        """

        User = Query()
        self.table.update({user_value: value_to_change}, User.ine == self.ine)
