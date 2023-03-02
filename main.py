
from chess.models.players import Player


def main():
    """"""
    p = Player("BRISE", "ALEXANDRE", "03/04/1996", "AB15478",)
    p2 = Player("LATRILLE", "AMELIE", "11/08/1997", "AL15423")
    p2.find_all()


if __name__ == "__main__":
    main()
