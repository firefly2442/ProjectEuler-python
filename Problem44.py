import math, sys

all_pentagons = []
dictionary = {}

def calcPentagon(n):
	pent = n*(3*n-1)/2
	return pent

#seed pentagon values in dictionary
num_to_seed = 1000000
for i in xrange(1,num_to_seed):
	pent = calcPentagon(i)
	all_pentagons.append(pent)
	dictionary[pent] = True

answers = []
num_to_try = 10000
#these loops could be pruned since we're duplicating checks (it's symmetric)
#and make it so the indices are closer together (since this is what we're trying to minimize)
for j in xrange(1,num_to_try):
	for k in xrange(1,num_to_try):
		difference = all_pentagons[j] - all_pentagons[k]
		summation = all_pentagons[j] + all_pentagons[k]
		try:
			#instead of storing all these, we could also use this: https://en.wikipedia.org/wiki/Pentagonal_number#The_perfect_square_test
			if dictionary[difference] and dictionary[summation]:
				d = all_pentagons[j] - all_pentagons[k]
				answers.append((j, k, d))
		except KeyError:
			None
	print "%.0f%%" % (100.0 * j/num_to_try)
print answers


