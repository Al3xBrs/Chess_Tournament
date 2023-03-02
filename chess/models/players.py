import json
from chess.models.conf import DATA_PLAYERS

# TODO : 1 fichier db json pour tous les joueurs
# TODO : Retravailler method load : @classmethod -- cls
# TODO : TinyDB au lieu de json


class Player:
    """ Gestion du joueur """

    def __init__(self, nom, prenom, date_naissance, ine):
        """ Description du joueur """

        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.ine = ine

    def create(self):
        """ Créer un dictionnaire du joueur et le save dans la bd """

        data_players = DATA_PLAYERS
        player_dict = {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "ine": self.ine,
        }
        player_json = json.dumps(player_dict)
        with open(data_players, "a") as f:
            f.write(player_json)

    @classmethod
    def find_all(cls):
        """ Charge la fiche d'un joueur """
        data_players = DATA_PLAYERS
        # with open(f"./data/players/{player.ine}.json", "r") as f:
        #     json_player = json.load(f)
        # print(json_player)

    def delete(player):
        pass
