import glicko2
import matplotlib.pyplot as plt
p1 = glicko2.Player()
p1.setRating(2073)
p1.setRd(73)

opp_rds = range(45, 101)
results = [0 for rd in opp_rds]

for rd in opp_rds:
	p1.update_player([1563], [rd],[0])
	results[rd - 45] = p1.getRating()
	p1 = glicko2.Player()
	p1.setRating(2073)
	p1.setRd(73)

plt.plot(opp_rds, results)
plt.show()