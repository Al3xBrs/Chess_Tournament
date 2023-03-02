import json


class Player:
    """ Gestion du joueur """

    def __init__(self, nom, prenom, date_naissance, ine):
        """ Description du joueur """

        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.ine = ine

    def create(self):
        """ Créer un dictionnaire du joueur """

        player_dict = {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "ine": self.ine,
        }
        player_json = json.dumps(player_dict)
        with open(f"./data/players/{player_dict['ine']}.json", "w") as f:
            f.write(player_json)

    def load(player):
        with open(f"./data/players/{player.ine}.json", "r") as f:
            json_player = json.load(f)
        print(json_player)
