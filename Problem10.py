#Problem10.py

import math

bounds = 2000000

A = [True] * bounds

#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
for i in range(2, int(math.sqrt(bounds))+1):
	if A[i]:
		j = int(math.pow(i,2))
		counter = 1
		while j < bounds:
			A[j] = False
			j = int(math.pow(i,2)+(counter*i))
			counter += 1

total = 0
for i in range(2, len(A)):
	if A[i]:
		total += i
		
print "Total: ", total
