
class MainMenu:
    """Créer un menu principal"""

    def afficher_main_menu():
        print("---------------")
        print("Choisissez une option :")
        print("(1) Créer un joueur")
        print("(2) Voir liste des joueurs")
        print("(3) Créer un tournois")
        print("(4) Gérer un match")
        print("(5) Tableau des scores")
        print("---------------")
        option = input("Votre choix :")

        return option


option = MainMenu.afficher_main_menu()
print(option)
