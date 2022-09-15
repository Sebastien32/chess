import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean, stdev
import numpy as np
sns.set_theme(style="dark")


input_vals = []
lichess_ratings = {}
guessed_ratings = {}

with open('PuzzleRatings.txt') as f:
	for line in f.read().splitlines():
		(puzz_id, rtg, guess) = line.split(',')
		lichess_ratings[int(puzz_id)] = int(rtg)
		guessed_ratings[int(puzz_id)] = int(guess)

#for rating in lichess_ratings.keys():
#	print(rating, lichess_ratings[rating], guessed_ratings[rating])

lichess_desc = (mean(lichess_ratings.values()), stdev(lichess_ratings.values()))
guess_desc = (mean(guessed_ratings.values()), stdev(guessed_ratings.values()))

x, y = list(lichess_ratings.values()), list(guessed_ratings.values())

fig, axs = plt.subplots(2, 2)

sns.histplot(x, ax = axs[0, 0], kde = True)
sns.histplot(y, ax = axs[0, 1], kde = True)

sns.scatterplot(x = y, y = x, s = 10, ci = 'sd', ax = axs[1, 1])
sns.histplot(x=y, y=x, bins=20, pthresh=.1, cmap="rocket_r", ax = axs[1, 0], cbar = True)
axs[0, 0].set_title('Lichess Rating Distribution')
axs[0, 1].set_title('Guessed Rating Distribution')
axs[1, 1].set_title('Guessed Rating vs. Lichess Rating')
axs[1, 0].set(xlabel = 'Guessed Rating', ylabel = 'Lichess Rating')
axs[1, 1].set(xlabel = 'Guessed Rating', ylabel = 'Lichess Rating')

z = np.polyfit(x, y, 1)
print(z)

plt.show()