from zth import zahlen, powers
## unfertig

Q = []
g = powers(2)
def isRoot(t):
	global Q
	a,b = 0, len(Q)-1
	while True:
		if b < a:
			return False
		m = (a + b) // 2
		if Q[m] < t:
			a = m + 1
		elif Q[m] > t:
            		b = m - 1
		else:
			return True

r, N = 0, 2000
for a in zahlen(1):
	while len(Q) <= 3*a:
		Q.append(g.__next__())
	for b in range(1,a+1):
		for c in range(1,b+1):
			if isRoot(a**2+(b+c)**2):
				r += 1
				if r >= N:
					print(a)
					exit()
