
def isBouncy(num):
	if len(str(num)) == 1:
		return False

	#check increasing
	increasing = True
	for i in range(0,len(str(num))-1):
		if int(str(num)[i]) < int(str(num)[i+1]):
			increasing = False
			break

	#check decreasing
	decreasing = True
	for i in range(0,len(str(num))-1):
		if int(str(num)[i]) > int(str(num)[i+1]):
			decreasing = False
			break

	if not increasing and not decreasing:
		return True
	else:
		return False

bouncy_count = 0
tried_count = 0
while True:
	if isBouncy(tried_count):
		bouncy_count += 1
		if float(bouncy_count)/float(tried_count) >= 0.99:
			break
	tried_count += 1

print "Bouncy count: ", bouncy_count
print "Tried count: ", tried_count
print "Ratio: ", float(bouncy_count)/float(tried_count)
