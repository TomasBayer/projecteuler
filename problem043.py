P = [2,3,5,7,11,13,17]
def permutationen(n):
	global p
	if n > 9:
		S = str(n)
		l = len(S)
		for i in range(0,l):
			N = list(S)
			a = int(N.pop(i))
			for p in permutationen(int(''.join(N))):
				k = 10*p + a
				if l < 4 or (k % 1000) % P[l-4] == 0:
					yield k
	elif n > 0:
		yield n		
	else:
		yield 0

print(sum(permutationen(9876543210)))
