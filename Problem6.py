#Problem6.py

import math

sum_squares = 0

for i in range(1, 101):
	sum_squares += int(math.pow(i, 2))
print "Sum of squares: ", sum_squares

square_sum = 0
for i in range(1, 101):
	square_sum += i
square_sum = int(math.pow(square_sum, 2))
print "Square of the sum: ", square_sum

print "Difference: ", square_sum - sum_squares
