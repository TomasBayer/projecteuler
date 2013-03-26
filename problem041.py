from zth import isProbablePrime

def permutationen(L):
	if len(L):
		for i in range(0,len(L)):
			N = list(L)
			a = N.pop(i)
			for p in permutationen(N):
				yield [a] + p
	else:
		yield []

for i in permutationen([str(i) for i in range(7,0,-1)]):
	k = int(''.join(i))
	if isProbablePrime(k):
		print(k)
		exit()

