import chess
import chess.pgn

pgn = open("../src/moves_wow.pgn")

game = chess.pgn.read_game(pgn)

base64_mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

thing = ""

for move in game.mainline_moves():
    thing += base64_mapping[move.to_square]

import base64
print(base64.b64decode(thing))