import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean, stdev
import scipy
import numpy as np
sns.set_theme(style="darkgrid")


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


#h = sns.jointplot(x=x, y= y, kind="reg", joint_kws = {'ci': None, 'scatter_kws':{'s':5}})
h = sns.jointplot(x=y, y= x, kind="reg", joint_kws = {'ci': None, 'scatter_kws':{'s':5}})

h.set_axis_labels('Random Normal Distribution', 'Lichess Ratings', fontsize=16)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(y, x)


#z1 = np.polyfit(x, y, 1)
z2 = np.polyfit(y, x, 1)

residuals = []

for guess, value in zip(y, x):
	pred = intercept + slope * guess
	residuals.append(pred - x)

print(np.mean(np.abs(residuals)))
plt.show()