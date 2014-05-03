#Problem36.py

def isPalindrome(n):
	n = str(n)
	start = 0
	end = len(n)-1
	while start != end and start < end:
		if n[start] != n[end]:
			return False
		start += 1
		end -= 1
	return True


sum = 0
for i in range(0, 1000000):
	if isPalindrome(i) and isPalindrome(bin(i)[2:]):
		sum += i
		
print sum
