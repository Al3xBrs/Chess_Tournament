def main_menu_view() -> str:
    """
    Affiche le menu principal
    """

    print(
        """
    ------- Menu principal -------
    (1) Menu joueur
    (2) Menu tournois
    (q) Quit
    ------- Menu principal -------        
    """
    )

    return input("Choix : ")
