from chess.models.players import Player
from chess.views.players import players_menu_view, players_list_menu_view, \
    player_create_menu_view, player_submenu_view, \
    players_list_view, player_delete_view, player_update_view, \
    search_player_view
import logging


class Controller:
    @classmethod
    def players_menu_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        1: liste des joueurs
        2: création joueur
        4: menu principal
        """

        choice = players_menu_view()

        if choice == "1":
            return "players_list_menu_controller", payload
        elif choice == "2":
            return "player_create_menu_controller", payload
        elif choice == "4":
            return "main_menu_controller", payload

    @classmethod
    def players_list_menu_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        liste joueurs :

        1: triée par nom
        2: triée par ine du joueur
        4: retour -> menu joueur
        q: menu principal
        """

        choice = players_list_menu_view()

        table = Player.find_all()

        players_list = [player.__dict__ for player in table]

        if choice == "1":
            players_list = sorted(players_list, key=lambda t: t["nom"])
            payload["players_list"] = players_list
            return "players_list_controller", payload
        elif choice == "2":
            players_list = sorted(players_list, key=lambda t: t["ine"])
            payload["players_list"] = players_list
            return "players_list_controller", payload
        elif choice == "4":
            return "players_menu_controller", payload
        elif choice == "q":
            return "main_menu_controller", payload

    @classmethod
    def players_list_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        2: génère un rapport de la liste .txt
        3: menu de recherche d'un joueur
        4: retour -> tris liste
        q: menu principal
        """
        players_list = payload["players_list"]
        choice = players_list_view(players_list)
        if choice == "4":
            return "players_list_menu_controller", payload
        elif choice == "q":
            return "main_menu_controller", payload
        elif choice == "3":
            return "search_player_controller", payload
        elif choice == "2":
            logging.warning("Rapport généré")
            with open("./data/Rapports/joueurs/joueurs.txt", "w") as f:
                f.write("Liste de joueurs :\n")
                for player in players_list:
                    for key, value in player.items():
                        f.write(f"{key.upper()} : {value}")
                        f.write("\n")
                    f.write("\n")
            return "players_list_controller", payload

    @classmethod
    def search_player_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        utilise la fonction find_one de la class Player pour le chercher.
        l'user rentre d'abord l'attribut à chercher, puis sa valeur:
        ex: choix 1: nom, choix 2: JEAN
        """
        choice = search_player_view()  # Renvoi une liste [data, value]
        player = Player.find_one(choice[0], choice[1])
        payload["player"] = player.ine
        return "player_submenu_controller", payload

    @classmethod
    def player_submenu_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        sous menu joueur
        1: maj de la fiche joueur
        2: suppression du joueur
        3: génère un rapport ine_du_joueur.txt
        4: retour liste joueur
        q: menu principal
        """
        player_ine = payload["player"]
        player = Player.find_one("ine", player_ine)
        player_dict = player.__dict__
        choice = player_submenu_view(player_dict)
        if choice == "1":
            return "player_update_controller", payload
        elif choice == "2":
            return "player_remove_menu_controller", payload
        elif choice == "3":
            with open(f"./data/Rapports/joueurs/{player_ine}.txt", "w") as f:
                f.write("Données joueur :\n")
                for key, value in player_dict.items():
                    f.write(f"{key.upper()} : {value}")
                    f.write("\n")
            logging.warning("Rapport généré")
            return "player_submenu_controller", payload
        elif choice == "4":
            return "players_list_menu_controller", payload
        elif choice == "q":
            return "main_menu_controller", payload

    @classmethod
    def player_create_menu_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        création du joueur
        """

        choice = player_create_menu_view()  # renvoi[nom,prenom,
        # date_naissance,ine]
        player = Player(choice[0], choice[1], choice[2], choice[3])
        player.create()
        logging.warning("Joueur créé")
        payload["player"] = player.ine
        return "player_submenu_controller", payload
        # sous menu du joueur créé à l'instant

    @classmethod
    def player_remove_menu_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        suppression du joueur
        y: suppr
        n: annul
        4: retour
        q: menu principal
        """
        choice = player_delete_view()
        player_ine = payload["player"]
        player = Player.find_one("ine", player_ine)
        if choice == "4":
            return "player_submenu_controller", payload
        if choice == "q":
            return "main_menu_controller", payload
        if choice == "y":
            player.remove()
            logging.warning("Joueur supprimé")
            return "players_list_menu_controller", payload
        if choice == "n":
            logging.warning("Joueur non supprimé")
            return "player_submenu_controller", payload

    @classmethod
    def player_update_controller(cls, payload: dict) -> tuple[str, dict]:
        """
        menu maj joueur
        """
        player_ine = payload["player"]
        player = Player.find_one("ine", player_ine)  # on recherche le joueur
        player_dict = player.__dict__
        choice = player_update_view(player_dict)
        player.update(choice[0], choice[1])  # data, value
        logging.warning("Joueur mis à jour")

        return "players_list_menu_controller", payload
