#Problem16.py

import math

power = 1000
val = str(int(math.pow(2,power)))
sum = 0


for i in range(0, len(val)):
	sum += int(val[i])
	
print "Sum: ", sum
