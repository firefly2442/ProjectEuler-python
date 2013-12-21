import sys

def isPrime(num):
	if num == 1:
		return False
	for i in range(2,num):
		if num % i == 0:
			return False
	return True


def stagePrime(num):
	for i in range(0, len(str(num))):
		#print i
		sub = int(str(num)[i:])
		#print "sub1: ", sub
		if not isPrime(sub):
			return False
			
	for i in range(1, len(str(num))):
		#print i
		sub = int(str(num)[:-i])
		#print "sub2: ", sub
		if not isPrime(sub):
			return False

	return True

	
primes = []
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
start = 8
while True:
	if stagePrime(start):
		primes.append(start)
		print primes
	if len(primes) == 11: #this 11th number takes awhile to generate
		total = 0
		print primes
		for i in range(0,len(primes)):
			total += primes[i]
		print "Total: ", total
		sys.exit(0)
	start += 1
