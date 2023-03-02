import json

# TODO : 1 fichier db json pour tous les joueurs
# TODO : Retravailler method load : @classmethod -- cls


class Player:
    """ Gestion du joueur """
    file = "./data/players/players.json"

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

    @classmethod
    def load(self):
        """ Charge la fiche d'un joueur """

        # with open(f"./data/players/{player.ine}.json", "r") as f:
        #     json_player = json.load(f)
        # print(json_player)
        return [Player("BRISE", "ALEXANDRE", "25555", "AB15578"),]

    def delete(player):
        pass
