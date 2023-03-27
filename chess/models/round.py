from datetime import datetime
from chess.models.conf import DATA_ROUNDS
from tinydb import Query
from chess.models.players import Player
import random


class Round:
    """ """
    table = DATA_ROUNDS

    def __init__(self, name, matchs_list, date_hour_start="", date_hour_end=""):
        """ """
        self.name = name
        self.matchs_list = matchs_list
        self.date_hour_start = date_hour_start
        self.date_hour_end = date_hour_end

    def create(self):
        """ """
        self.table.insert(self.__dict__)
        self.table.update({"date_hour_start": str(datetime.now())}, Query().name == self.name)

    @classmethod
    def winner(cls, player=None):
        """ """
        if player is not None:
            winner = player
            return player
        else:
            return player

    @classmethod
    def remove_all(cls):
        """ """
        cls.table.truncate()

    @classmethod
    def find_one(cls, data, value):
        """ """
        User = Query()
        r_list = cls.table.search(User[data] == value)

        r_list = [Round(**i) for i in r_list]

        # we want only 1 player
        if len(r_list) != 1:
            raise AttributeError("more than 1 round")

        return r_list[0]

    def end(self):
        """ """
        self.table.update({"date_hour_end": str(datetime.now())}, Query().name == self.name)
