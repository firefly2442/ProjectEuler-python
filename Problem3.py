import math

#This will get easier to compute over time since "num" decreases
#we have less of a range to check.  Something like this might be useful
#in the future: #https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def isPrime(num):
	if num == 1:
		return False
	for i in xrange(2,num):
		if num % i == 0:
			return False
	return True

#we can limit the range here to the sqrt
r = int(math.floor(math.sqrt(600851475142)))
for i in xrange(r, 1, -1):
	if isPrime(i):
		if 600851475143 % i == 0:
			print "Largest prime: ", i
			break
	#this will not get to 100%, eventually we'll find the highest value
	print "%.0f%%" % (100.0 * (r-i)/r)

