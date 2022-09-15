import matplotlib.pyplot as plt

v0_buckets = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
v1_buckets = [9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11]
v2_buckets = [5, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19, 21]
v3_buckets = [7, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21, 23]
test_bucket = [7 + i for i in range(11)]
test_bucket.append(28)
print(test_bucket)

v1_buckets = [9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11]
v2_buckets = [5, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19, 21]
v3_buckets = [7, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21, 23]
def generate_averages(buckets):
	averages = []
	for i in range(len(buckets)):
		target_bucket = 1000 + 150 * i
		averages.extend([target_bucket + (150 / buckets[i]) * (j - (buckets[i] - 1)/2) for j in range(buckets[i])])
	return averages

#print(len(v0_buckets), sum(v0_buckets))
#print(len(v1_buckets), sum(v1_buckets))
#print(len(v2_buckets), sum(v2_buckets))
#print(len(v3_buckets), sum(v3_buckets))
print(len(test_bucket), sum(test_bucket))


for i in range(16):
	print(generate_averages(v3_buckets)[10 * i])

x = range(100)
y = range(100,200)
fig = plt.figure()
ax1 = fig.add_subplot(111)

#ax1.scatter(list(range(1, sum(v0_buckets) + 1)), generate_averages(v0_buckets), label = 'v0 - "Linear"')
#ax1.scatter(list(range(1, sum(v1_buckets) + 1)), generate_averages(v1_buckets), label = 'v1 - "Easy"')
#ax1.scatter(list(range(1, sum(v2_buckets) + 1)), generate_averages(v2_buckets), label = 'v2 - "Hard"')
ax1.scatter(list(range(1, sum(v3_buckets) + 1)), generate_averages(v3_buckets), label = 'v3 - "Current"')
ax1.set_ylabel("Average puzzle rating")
ax1.set_xlabel("Puzzle number")
ax1.legend(loc='upper left');

plt.show()
