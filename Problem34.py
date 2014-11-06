#Problem34.py

import math

grand_sum = 0
for i in range(3, 100000):
	total = 0
	for a in str(i):
		total += math.factorial(int(a))
	if total == i:
		print "Found: ", i
		grand_sum += i

print grand_sum
