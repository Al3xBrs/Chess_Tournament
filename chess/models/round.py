from datetime import datetime
from chess.models.conf import DATA_ROUNDS
from tinydb import Query
import random


class Round:
    """ """
    table = DATA_ROUNDS

    def __init__(self, name, matchs_list, date_hour_start="", date_hour_end=""):
        self.name = name
        self.matchs_list = matchs_list
        self.date_hour_start = date_hour_start
        self.date_hour_end = date_hour_end

    def create(self):
        self.table.insert(self.__dict__)
        self.table.update({"date_hour_start": str(datetime.now())}, Query().name == self.name)

    # def generate_match(self, players_list):
    #     if self.name == "1":
    #         i = 0
    #         score = "0"
    #         sorted_list = players_list
    #         random.shuffle(sorted_list)
    #         while i <= len(sorted_list):
    #             match = ([sorted_list[i], score], [sorted_list[i + 1], score])
    #             i += 2
    #             self.matchs.append(match)
    #
    #     else:
    #         sorted_list = sorted(players_list)
    #         return sorted_list

    # def generate_match(self, sorted_list):
    #     match = ([player, score], [player, score])
    #     self.matchs.append(match)
    #     return match

    @classmethod
    def winner(cls, player="both"):
        if player == "both":
            winner = None
        else:
            winner = player

        return winner

    @classmethod
    def remove_all(cls):
        cls.table.truncate()

    def end(self):
        self.table.update({"date_hour_end": str(datetime.now())}, Query().name == self.name)
