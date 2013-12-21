import sys

def checkNum(num):
	for i in range(1,21):
		if num % i != 0:
			return False
	return True
	

i = 1
while True:
	if checkNum(i):
		print i
		sys.exit(0)
	i += 1
