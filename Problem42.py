#Problem42.py


triangle_numbers = []

def returnTriangleNumber(n):
	return 0.5*n*(n+1)
	
def getWordScore(word):
	score = 0
	for i in range(0, len(word)):
		score += (ord(word[i])-96)
	return score

	
def checkWord(word):
	score = getWordScore(word)
	while score > triangle_numbers[-1]:
		triangle_numbers.append(returnTriangleNumber(len(triangle_numbers)+1))
	if score in triangle_numbers:
		return True
	else:
		return False
	
#seed the triangle numbers a little
for i in range(1, 10):
	triangle_numbers.append(returnTriangleNumber(i))


file = open("words.txt", "r")
line = file.readline()
line = line.replace('\"', '')
words = line.split(",")

counter = 0
for word in words:
	word = word.lower()
	if checkWord(word):
		counter += 1
print "Triangle Words in List: ", counter
