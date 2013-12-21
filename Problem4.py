import math

def isPalindrome(num):
	length = len(str(num))
	#print "Length: ", length
	half_length = int(math.ceil(len(str(num))/float(2)))
	#print "Half Length: ", half_length
	for i in range(0,half_length):
		#print "Comparing: ", str(num)[i], " and ", str(num)[length-i-1]
		if str(num)[i] != str(num)[length-i-1]:
			return False
	return True
	
largest = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		if isPalindrome(i*j):
			if (i*j) > largest:
				largest = i*j
print largest
