#Problem9.py

import math, sys

#brute force it, not really ideal but it works
for a in range(0, 1000):
	for b in range(a, 1000):
		for c in range(b, 1000):
			if a+b+c == 1000 and a < b and b < c:
				if math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
					print (a*b*c)
					sys.exit(0)
