def builder(n):
	def builderh(L,k):
		if len(L):
			for i in range(0,len(L)):
				N = list(L)
				a = N.pop(i)
				if len(L) % 2 == 1 and len(L) < 2*n-1 and a <= k:
					break
				for p in builderh(N,k):
					yield [a] + p 
		else:
			yield []
	for i in range(n+1,0,-1):
		for k in builderh(list(range(2*n,i,-1))+list(range(i-1,0,-1)),i):
			yield [i] + k

def isValid(A):
	s = sum(A[:3])
	if s != A[-1] + A[-2] + A[1]:
		return False
	for i in range(4,len(A),2):
		if s != sum(A[i-2:i+1]):
			return False
	return True	

def toString(A):
	s = A[:3]
	for i in range(4,len(A),2):
		s += [A[i-1], A[i-2], A[i]]
	s += [A[-1], A[-2], A[1]]
	return ''.join([str(i) for i in s])

n = 5
for k in builder(n):
	if isValid(k):
		print(toString(k))
		break
