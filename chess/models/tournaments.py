import logging, random

from chess.models.conf import DATA_TOURNAMENTS
from tinydb import Query
from chess.models.players import Player
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
            current_round=0,
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
        """ """
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
        """ """
        if (self.status == "created") and (self.n_players == self.MAX_PLAYERS):
            self.status = "running"
            self.table.update({'status': self.status}, Query().name == self.name)

            # TODO: Voir avec Alex que status ne doit pas être un attribut public.

        elif self.status != "created":
            logging.error(f"Erreur de status {self.status}")
        else:
            logging.error("problème nombre de players")

    def create_new_round(self):
        """ """
        if self.current_round == 0 and self.status == "running":
            self.current_round += 1
            self.table.update({'current_round': self.current_round}, Query().name == self.name)

            shuffled_list = self.players_list
            random.shuffle(shuffled_list)
            match_1 = (f"{shuffled_list[0]}", 0), (f"{shuffled_list[1]}", 0)
            match_2 = (f"{shuffled_list[2]}", 0), (f"{shuffled_list[3]}", 0)
            matchs_list = [match_1, match_2]
            r = Round("1", matchs_list)
            r.create()
            self.rounds_list.append(r.name)
            self.table.update({"rounds_list": self.rounds_list}, Query().name == self.name)
            return r.name

    @property
    def scores(self):
        """ """
        if (self.status == "created") or (self.current_round == 1):
            scores_dict = {player_ine: 0 for player_ine in self.players_list}

            return scores_dict

        points_list = []

        for round_name in self.rounds_list:
            rounde = Round.find_one("name", round_name)
            for match in rounde.matchs_list:
                points_list.append(match[0])
                points_list.append(match[1])

        scores = {player_ine: 0 for player_ine in self.players_list}
        for k, val in points_list:
            scores[k] += val

        logging.warning(points_list)

        logging.warning(scores)

        return scores

    def next_round(self):
        """ """
        previous_round = Round.find_one("name", f"{self.current_round}")
        previous_round.end()

        self.current_round += 1
        self.table.update({"current_round": self.current_round}, Query().name == self.name)

        if self.current_round > self.rounds_number:
            self.status = "closed"
            self.table.update({"status": self.status}, Query().name == self.name)

            logging.warning("Tournois terminé !")

        else:

            scores = self.scores
            sorted_dict = sorted(scores.items(), key=lambda x: x[1])
            match_1 = sorted_dict[3], sorted_dict[2]
            match_2 = sorted_dict[1], sorted_dict[0]
            new_matchs_list = [match_1, match_2]
            previous_matchs_list = previous_round.matchs_list
            if previous_matchs_list == new_matchs_list:
                match_1 = sorted_dict[3], sorted_dict[1]
                match_2 = sorted_dict[2], sorted_dict[0]
                new_matchs_list = [match_1, match_2]

            new_round = Round(f"{self.current_round}", new_matchs_list)
            self.rounds_list.append(new_round.name)
            self.table.update({"rounds_list": self.rounds_list}, Query().name == self.name)
            new_round.create()

    @property
    def n_players(self):
        """ """
        return len(self.players_list)

    def __repr__(self):
        """ """
        rep = 'Tournois(' + self.name + ',' + self.place + str(self.players_list) + ')'
        return rep
