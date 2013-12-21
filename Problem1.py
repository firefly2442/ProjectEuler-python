
def checkNum(num):
	if num % 3 == 0 or num % 5 == 0:
		return True
	return False

sum_num = 0
for i in range(1,1000):
	if checkNum(i):
		sum_num += i

print sum_num
