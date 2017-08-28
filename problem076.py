from zth import numberOfIntegerPartitions

def sophisticated(N):
	n = 0
	for i in numberOfIntegerPartitions():
		if n == N:
			return i-1
		n += 1

def bruteforceCaching(N):
	# C[n][m] =  Number of possibilities to write n as a sum of integers <= m 
	C = [[0],[1]]

	def c(a,b):
		if b > a:
			return c(a,a)
		else:
			return C[a][b-1]

	for n in range(2,N+1):
		t = []
		k = 0
		for m in range(1,n):
			k += c(n-m,m)
			t.append(k)
		t.append(k+1)
		C.append(t)

	return C[-1][-1]-1

N = 100
print(bruteforceCaching(N))
print(sophisticated(N))
