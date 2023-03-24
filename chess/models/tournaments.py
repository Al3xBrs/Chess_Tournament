import logging, random

from chess.models.conf import DATA_TOURNAMENTS
from tinydb import Query

from chess.models.round import Round


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
            current_round=-1,
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
        self.current_round = current_round
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description
        self.status = status

    def create(self):
        """ """
        self.table.insert(self.__dict__)

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
        """ Chercher un tournois """
        Obj = Query()
        t_list = cls.table.search(Obj[data] == value)

        if len(t_list) != 1:
            raise AttributeError("More than 1 tournament")
        return t_list[0]

    @classmethod
    def find_all(cls):
        """ """
        list_doc = cls.table.all()
        list_dict = [dict(doc) for doc in list_doc]

        return list_dict

    def add_player(self, ine_player: str):

        if (self.status == "created") and (self.n_players < self.MAX_PLAYERS):

            if ine_player not in self.players_list:
                self.players_list.append(ine_player)
                self.table.update({'players_list': self.players_list}, Query().name == self.name)
                logging.warning("Joueur inscrit")

            else:
                logging.warning(" Attention : joueur déjà inscrit")

        elif self.n_players >= self.MAX_PLAYERS:
            logging.warning("Maximum de joueurs atteint")

        else:
            logging.warning("Attention : tournois non créé")

    def add_players(self, players_list: list):
        """ """
        for player in players_list:
            self.add_player(player)

    def start_tournament(self):
        if (self.status == "created") and (self.n_players == self.MAX_PLAYERS):
            self.status = "running"
            # TODO: Voir avec Alex que status ne doit pas être un attribut public.

        elif self.status != "created":
            logging.error(f"Erreur de status {self.status}")
        else:
            logging.error("problème nombre de players")

    def create_new_round(self):
        if self.current_round == -1 and self.status == "running":
            self.current_round += 1
            shuffled_list = self.players_list
            random.shuffle(shuffled_list)
            match_1 = shuffled_list[0], shuffled_list[1]
            match_2 = shuffled_list[2], shuffled_list[3]
            matchs_list = [match_1, match_2]
            # pour le ppremier round, pas besoin de checker les socre donc osef. Que 4 perso.
            r = Round("1", matchs_list)
            r.create()
            self.rounds_list.append(r.name)
            return r.name
        pass

    def compute_scores(self, current_round):

        pass

    def next_round(self):
        self.current_round += 1
        pass

    @property
    def n_players(self):
        return len(self.players_list)

    def __repr__(self):
        rep = 'Tournois(' + self.name + ',' + self.place + str(self.players_list) + ')'
        return rep
