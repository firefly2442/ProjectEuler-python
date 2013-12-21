
def getNameScore(name):
	score = 0	
	for i in range(0, len(name)):
		score = score + (ord(name[i])-96)
	return score


names = []

file = open("names.txt", "r")
line = file.readline()
line = line.replace('\"', '')
names = line.split(",")

names.sort()

total_score = 0
index = 1
for name in names:
	total_score += getNameScore(name.lower()) * index
	index += 1

print total_score
