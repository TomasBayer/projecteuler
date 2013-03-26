fac = [1]
for i in range(1,10):
	fac.append(i*fac[i-1])

s = 0
for n in range(3,7*fac[9]+1):
	if sum([fac[int(i)] for i in str(n)]) == n:
		s += n
print(s)
