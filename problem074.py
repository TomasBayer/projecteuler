N = 999999

# Caches
F, E, C = [1], {}, {}
for i in range(1,10):
	F.append(i*F[-1])

# Solution
def chain(n):
	L = []
	while n not in L:
		L.append(n)
		if n not in E:
			E[n] = sum([F[int(i)] for i in str(n)])
		n = E[n]
	return len(L)

k = 0
for i in range(1,N+1):
	if chain(i) == 60:
		k += 1
print(k)
