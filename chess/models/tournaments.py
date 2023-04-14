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

    def end_tournament(self):
        """ """
        Obj = Query()
        self.table.update({"status": "closed"}, Obj.name == self.name)

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
            self.table.update({"status": self.status}, Query().name == self.name)

        elif self.status != "created":
            logging.error(f"Erreur de status {self.status}")
        else:
            logging.error("problème nombre de players")

    def create_first_round(self):
        """ """
        if self.current_round == -1 and self.status == "running":
            self.current_round += 1
            self.table.update({"current_round": self.current_round}, Query().name == self.name)

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

    @classmethod
    def get_instance(cls, document):
        return Tournament(document)

    @property
    def scores(self):
        """ """
        if not self.n_players:
            return {}

            # no score before 1st round

        scores = {id_player: 0 for id_player in self.players_list}
        if self.current_round < 1:
            return scores

        # else
        for round_id in self.rounds_list:
            ronde = Round.find_one("round_id", round_id)
            matchs_list = ronde.matchs_list
            for match in matchs_list:
                scores[match[0][0]] += match[0][1]
                scores[match[1][0]] += match[1][1]

        return scores

    @property
    def classement(self):
        """ """
        classement = [(i, j) for i, j in self.scores.items()]

        classement = sorted(classement, key=lambda i: i[1], reverse=True)

        classement = [i[0] for i in classement]
        self.players_list = classement
        self.table.update({"players_list": self.players_list}, Query().name == self.name)

        return classement

    def have_already_played(self, player_x, player_0):
        """"""
        flatten_match_list = []
        for round_id in self.rounds_list:
            rounde = Round.find_one("round_id", round_id)

            matchs_list = rounde.matchs_list

            for match in matchs_list:
                m = (match[0][0], match[1][0])
                flatten_match_list.append(m)

        cand_match = (player_0, player_x)

        for match in flatten_match_list:

            if match == cand_match:
                return True

        cand_match = (player_x, player_0)
        for match in flatten_match_list:

            if match == cand_match:
                return True

        return False

    def compute_round(self):
        """define the roundes"""

        logging.warning("_compute_ronde  called")

        # seulement si c'est la 1er la current_round 0
        if self.current_round == 0:
            logging.warning("not self._current_round:")

            # we need 3 object storage
            match_list = []
            players_choisis = []
            players_non_choisis = [i for i in self.players_list]

            while len(players_non_choisis) != 0:
                # just to be more readable
                p1 = players_non_choisis[0]
                p2 = players_non_choisis[1]

                # match and match list
                match = [(p1, 0), (p2, 0)]
                match_list.append(match)

                # update players_choisis & non choisis
                players_choisis.extend([p1, p2])

                players_non_choisis.remove(p1)
                players_non_choisis.remove(p2)

            return match_list

        # else
        match_list = []
        players_choisis = []
        self.players_list = self.classement
        players_non_choisis = [i for i in self.players_list]

        i = 0
        while len(players_non_choisis) != 0:
            p1 = players_non_choisis[i]

            if p1 in players_choisis:
                continue

            for p_id in self.players_list:
                if p1 == p_id:
                    continue

                if p_id in players_choisis:
                    continue

                already_played = self.have_already_played(p1, p_id)
                if not already_played:
                    break

                # match and match list
            match = [(p1, 0), (p_id, 0)]
            match_list.append(match)

            # update players_choisis & non choisis
            players_choisis.extend([p1, p_id])

            if p_id in players_non_choisis:
                players_non_choisis.remove(p_id)
            players_non_choisis.remove(p1)

        return match_list

    def next_round(self):
        """ """
        previous_round = Round.find_one("round_id", f"{self.rounds_list[self.current_round]}")
        previous_round.end()

        self.current_round += 1
        self.table.update({"current_round": self.current_round}, Query().name == self.name)

        if int(self.current_round) >= int(self.rounds_number):
            self.status = "closed"
            self.table.update({"status": self.status}, Query().name == self.name)

            return logging.warning("Tournois terminé !")
        new_match_list = self.compute_round()

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
