
fib = [1, 2]
i = 2
while True:
	val = fib[i-2] + fib[i-1]
	if val >= 4000000:
		break
	fib.append(val)
	i += 1

sum = 0
for f in fib:
	if f % 2 == 0:
		sum += f

print "Sum: ", sum
