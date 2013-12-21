
def collatz(n):
	if n % 2 == 0:
		return n/2
	else:
		return (3*n)+1

def returnChain(i):
	chain = []
	chain.append(i)
	while True:
		val = collatz(chain[-1])
		chain.append(val)
		if val == 1:
			return chain

starting = 0
longest = 0
for i in range(1, 1000000):
	chain = returnChain(i)
	if len(chain) > longest:
		longest = len(chain)
		starting = chain[0]

print "Longest: ", longest
print "Starting value: ", starting
