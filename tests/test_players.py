from chess.models.players import Player
import secrets


p = Player(secrets.token_hex(2), secrets.token_hex(
    2), '', secrets.token_hex(2))
