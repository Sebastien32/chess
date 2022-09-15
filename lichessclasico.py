import chess.pgn
from collections import Counter

pgn = open('allgames_teamlwseries.pgn')

all_games = []
for i in range(44506):
	all_games.append(chess.pgn.read_game(pgn))
	if i % 1000 == 0:
		print(i)

all_pairings = Counter()
count45 = 0
for game in all_games:
	if game.headers["TimeControl"] == '2700+45':
		count45 += 1
		players = (game.headers["White"], game.headers["Black"])
		all_pairings[tuple(sorted(players))] += 1

