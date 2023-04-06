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

        elif self.status != "created":
            logging.error(f"Erreur de status {self.status}")
        else:
            logging.error("problème nombre de players")

    def create_first_round(self):
        """ """
        if self.current_round == -1 and self.status == "running":
            self.current_round += 1
            self.table.update({'current_round': self.current_round}, Query().name == self.name)

            shuffled_list = self.players_list
            random.shuffle(shuffled_list)
            match_1 = (f"{shuffled_list[0]}", 0), (f"{shuffled_list[1]}", 0)
            match_2 = (f"{shuffled_list[2]}", 0), (f"{shuffled_list[3]}", 0)
            matchs_list = [match_1, match_2]
            r = Round(matchs_list)
            r.create()
            self.rounds_list.append(r.round_id)
            self.table.update({"rounds_list": self.rounds_list}, Query().name == self.name)
            return r.round_id

    @property
    def scores(self):
        """ """
        if (self.status == "created") or (self.current_round == 0):
            scores_dict = {player_ine: 0 for player_ine in self.players_list}

            return scores_dict

        points_list = []

        for round_id in self.rounds_list:
            rounde = Round.find_one("round_id", round_id)
            for match in rounde.matchs_list:
                points_list.append(match[0])
                points_list.append(match[1])

        scores = {player_ine: 0 for player_ine in self.players_list}
        for k, val in points_list:
            scores[k] += val

        logging.warning(points_list)

        logging.warning(scores)

        return scores

    @classmethod
    def have_already_played(cls, player_x, player_0):
        previous_matchs_lists = Round.get_previous_matchs()
        print("previous matchs list :", previous_matchs_lists)
        if [[player_x, any], [player_0, any]] or [[player_0, any], [player_x, any]] in previous_matchs_lists:
            return True

    def next_round(self):
        """ """
        previous_round = Round.find_one("round_id", f"{self.rounds_list[self.current_round]}")
        previous_round.end()

        self.current_round += 1
        self.table.update({"current_round": self.current_round}, Query().name == self.name)

        if self.current_round >= self.rounds_number:
            self.status = "closed"
            self.table.update({"status": self.status}, Query().name == self.name)

            return logging.warning("Tournois terminé !")

        scores = self.scores
        sorted_list = sorted(scores.items(), key=lambda x: x[1])
        print("sorted_list: ", sorted_list)
        players_not_selected = [player for (player, score) in sorted_list]
        print("players not selected : ", players_not_selected)
        new_match_list = []
        while len(players_not_selected) > 0:

            player_0 = players_not_selected[0]

            for player_x in players_not_selected:
                print("player_x : ", player_x)
                # TODO : ATTENTION
                if self.have_already_played(player_x, player_0) or (player_x == player_0):
                    continue

                match_1 = ([player_x, 0], [player_0, 0])
                new_match_list.append(match_1)
                players_not_selected.remove(player_x)
                print("players not selected : ", players_not_selected)

            break

        new_round = Round(new_match_list)
        self.rounds_list.append(new_round.round_id)
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
