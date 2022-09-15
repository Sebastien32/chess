import itertools as it
import matplotlib.pyplot as plt
def sim_4545_match(win_probs):
	# win_probs = 6 lists of [white, draw, black] percentages
	assert isinstance(win_probs, list)
	assert isinstance(win_probs[0], list)
	assert len(win_probs) == 6
	assert len(win_probs[0]) == 3
	for board in range(6):
		assert (sum(win_probs[board]) - 1) < .0001, print(sum(win_probs[board]))
		for result in range(3):
			win_probs[board][result] = int(round(win_probs[board][result] * (10 ** 4), 0))
		assert (sum(win_probs[board])) == 10000, print(sum(win_probs[board]))
	results = it.product(range(3), repeat = 6)
	final_probabilites = [0] * 13
	likelihood = 1
	for result in results:
		for board in range(6):
			likelihood *= win_probs[board][result[board]]
		final_probabilites[sum(result)] += likelihood
		likelihood = 1
	print(final_probabilites)
	plt.plot(range(13), final_probabilites,)
	#plt.show()

random_odds = [[0.3333, 0.3334, 0.3333] for i in range(6)]
sim_4545_match(random_odds)