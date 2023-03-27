from chess.models.tournaments import Tournament
from chess.models.round import Round

Tournament.remove_all()
Round.remove_all()
t1 = Tournament("Tournois_1", "DAX", "27/03/23", "28/03/23")
t1.create()
list_players = ["AB12345", "AL54321", "JL45678", "AB87654"]
t1.add_players(list_players)
t1.start_tournament()
t1.create_new_round()
t1.next_round()
