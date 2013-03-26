import primeCache as pc

def candidates(n):
	if n > 1:
		for k in candidates(n-1):
			for i in ['1','3','7','9']:
				yield (k + i)
	else:
		for i in ['2','3','5','7']:
			yield i

def truncations(s):
	for i in range(0,len(s)):
		yield int(s[i:])
		if i > 1:
			yield int(s[:i])

r = 2
R = []
while len(R) < 11:
	for n in candidates(r):
		b = True
		for i in truncations(n):
			if not pc.isPrime(i):
				b = False
				break
		if b:
			R.append(int(n))
	r += 1
print(sum(R))
