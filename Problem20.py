#Problem20.py

import math

def sumDigits(n):
	sum = 0
	for i in range(0, len(str(n))):
		sum += int(str(n)[i])
	return sum
	

print sumDigits(math.factorial(100))
