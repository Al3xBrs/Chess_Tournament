from datetime import datetime
from chess.models.conf import DATA_ROUNDS
from tinydb import Query
import uuid


class Round:
    """ """
    table = DATA_ROUNDS

    def __init__(self, matchs_list=[], date_hour_start="", date_hour_end="", round_id=None):
        """ """
        self.round_id = round_id or str(uuid.uuid4())
        self.matchs_list = matchs_list
        self.date_hour_start = date_hour_start
        self.date_hour_end = date_hour_end

    def create(self):
        """ """
        self.table.insert(self.__dict__)
        self.table.update({"date_hour_start": str(datetime.now())}, Query().round_id == self.round_id)

    @classmethod
    def remove_all(cls):
        """ """
        cls.table.truncate()

    def remove_one(self):
        """ """
        Obj = Query()
        self.table.remove(Obj.round_id == self.round_id)

    @classmethod
    def find_one(cls, data, value):
        """ """
        User = Query()
        r_list = cls.table.search(User[data] == value)

        r_list = [Round(**i) for i in r_list]

        if len(r_list) != 1:
            raise AttributeError("more than 1 round")

        return r_list[0]

    def update(self, data, value):
        self.table.update({data: value}, Query().round_id == self.round_id)

    def end(self):
        """ """
        self.table.update({"date_hour_end": str(datetime.now())}, Query().round_id == self.round_id)

    @classmethod
    def get_previous_matchs(cls):
        """
        Retourne tous les matchs des rounds précédents
        """
        matchs = []
        previous_rounds = cls.table.all()
        for round_dict in previous_rounds:
            round_obj = cls(**round_dict)
            matchs.extend(round_obj.matchs_list)
        return matchs
