import logging

from chess.models.conf import DATA_TOURNAMENTS
from tinydb import Query


class Tournament:
    """ """

    MAX_PLAYERS = 4
    table = DATA_TOURNAMENTS

    def __init__(
            self,

            name,
            place="",
            start_date="",
            end_date="",
            rounds_number=4,
            round=-1,
            rounds_list=[],
            players_list=[],
            description="",
            status="created",  # créé, en cours, terminé,

    ) -> None:
        """ """
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_number = rounds_number
        self.round = round
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description
        self.status = status

    def create(self):
        """ """
        self.table.insert(self.__dict__)

    def generate_matchs(self):
        pass

    def remove_one(self):
        """ """
        Obj = Query()
        self.table.remove(Obj.name == self.name)

    @classmethod
    def remove_all(cls):
        """ """
        cls.table.truncate()

    def update(self, tournament_value, value_to_change):
        """ """
        Obj = Query()
        self.table.update({tournament_value: value_to_change}, Obj.name == self.name)

    @classmethod
    def find_one(cls, data, value):
        """ """
        Obj = Query()
        t_list = cls.table.search(Obj[data] == value)

        t_list = [Tournament(**i) for i in t_list]

        if len(t_list) != 1:
            raise AttributeError("More than 1 tournament")
        return t_list[0]

    @classmethod
    def find_all(cls):
        """ """
        list_doc = cls.table.all()
        list_dict = [dict(doc) for doc in list_doc]
        list_instance = [Tournament(**t_dict) for t_dict in list_dict]

        return list_instance

    def add_player(self, ine_player: str):

        if self.status == "created":

            if not ine_player in self.players_list:
                self.players_list.append(ine_player)
                return logging.warning("Joueur inscrit")

            else:
                return logging.warning(" Attention : joueur déjà inscrit")

        elif len(self.players_list) == self.MAX_PLAYERS:
            return logging.warning("Maximum de joueurs atteint")

        else:
            return logging.warning("Attention : tournois non créé")

    def add_players(self, players_list: list):
        """ """
        if self.status == "created":

            if len(players_list) <= self.MAX_PLAYERS - len(self.players_list):
                [self.players_list.append(p) for p in players_list]
                return logging.warning("Joueurs inscrits")

            else:
                return logging.warning("Attention : Maximum de joueurs atteint")

        else:
            return logging.warning("Attention : tournois non créé")

    def __repr__(self):
        pass
