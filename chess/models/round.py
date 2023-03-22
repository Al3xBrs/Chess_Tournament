from datetime import datetime
from chess.models.conf import DATA_ROUNDS
from tinydb import Query


class Round:
    """ """
    table = DATA_ROUNDS

    def __init__(self, name, date_hour_start="", date_hour_end=""):
        self.name = name
        self.date_hour_start = date_hour_start
        self.date_hour_end = date_hour_end

    def create(self):
        self.table.insert(self.__dict__)
        self.table.update({"date_hour_start": str(datetime.now())}, Query().name == self.name)
