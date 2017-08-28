from fget import fgetLines
def getTriangle(filename):
	t = []
	for l in fgetLines(filename):
		n = []
		for i in l.split(' '):
			n.append(int(i))
		t.append(n)
	return t

def maxSum_bruteforce(t):
	def bfh(t,i,j):
		if i == len(t) - 1:
			return t[i][j]
		else:
			return max(bfh(t,i+1,j),bfh(t,i+1,j+1)) + t[i][j]
	return bfh(t,0,0)

def maxSum_caching(t):
	m = [ [0] * i for i in range(1,len(t)) ] + [t[-1]]
	for i in range(len(t)-2,-1,-1):
		for j in range(0,i+1):
			m[i][j] = max(m[i+1][j],m[i+1][j+1]) + t[i][j] 
	return m[0][0]

print(maxSum_caching(getTriangle("problem067")))
