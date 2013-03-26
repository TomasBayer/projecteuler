import primeCache as pc

def candidates(n):
	if n:
		for k in candidates(n-1):
			for i in ['1','3','7','9']:
				yield (k + i)
	else:
		yield ''

def rotations(s):
	for i in range(0,len(s)):
		n = s[i:] + s[:i]
		if s == n and i > 0:
			break
		yield n
s = 4
for i in range(2,7):
	for n in candidates(i):
		b = True
		for i in rotations(n):
			if not pc.isPrime(int(i)):
				b = False
				break
		if b:
			s += 1
print(s)
