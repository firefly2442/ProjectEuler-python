import sys

def checkPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True
	

num_primes = 0
i = 2
while True:
	if checkPrime(i):
		num_primes += 1
		print i, num_primes
		if num_primes == 10001:
			sys.exit(0)
	i += 1
