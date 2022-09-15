import random
import itertools as it
import time
def single_round_robin(num_players, odds_of_winning, number_of_simulations):
	'''
	Number of players = Number of players in a single round robin
	Odds of winning = A 2D array of tuples that represent W/L probability of
	when the first player (row number) is white
	Number of simulations = Simulations of full tournament to run
	'''
	assert isinstance(num_players, int), "Number of players must be an integer"
	assert num_players > 1, "Number of players must be greater than 1"
	assert num_players < 20, "Number of players should be less than 20"
	assert isinstance(odds_of_winning, list), "Odds of winning should be a 2D array"
	assert isinstance(odds_of_winning[0], list), "Odds of winning should be a 2D array"
	assert isinstance(odds_of_winning[0][0], tuple), "Entries in odds of winning should be tuples of W/L probability as white"
	assert number_of_simulations > 0, "Number of simulations should be positive"
	assert number_of_simulations < 10 ** 9, "Running more than a billion simulations may take too long"
	tournament_wins = [0] * num_players
	games_list = list(it.combinations(range(num_players), 2))
	total_games = num_players * (num_players - 1) // 2
	for sim in range(number_of_simulations):
		player_wins = [0] * num_players
		player_losses = [0] * num_players
		for game in range(total_games):
			if (game % 2 == 1):
				white, black = reversed(games_list[game])
			else:
				white, black = games_list[game]
			#print(white, black)
			result = random.random()
			if (result < odds_of_winning[white][black][0]):
				player_wins[white] += 1
				player_losses[black] += 1
			elif (result > (1 - odds_of_winning[white][black][1])):
				player_wins[black] += 1
				player_losses[white] += 1
		player_scores = [2 * player_wins[player] + (num_players - 1 - player_wins[player] - player_losses[player]) for player in range(num_players)]
		for player in range(num_players):
			if(player_scores[player] == max(player_scores)):
				tournament_wins[player] += 1
	return tournament_wins

def gen_even_odds(num_players):
	return [[(0.4, 0.3) for a in range(num_players)] for b in range(num_players)]

for i in range(2, 20):
	players = i
	before = time.time()
	b = single_round_robin(players, gen_even_odds(players), 10 ** 5)
	after = time.time()
	time_taken = after - before
	time_taken *= 1000
	total_games = (players * (players - 1) // 2)
	normalized = time_taken / total_games
	print("{0:02d}".format(players), "{0:0.3f}".format(time_taken), total_games, "{0:0.3f}".format(normalized), b, sum(b))





