top = 10

## Berechne Fakultäten
fac = [1]
for i in range(1,top + 1):
	fac.append(i*fac[i-1])

n = 0
v = 10**6 - 1
ar = [i for i in range(0,top)]

for i in range(top,0,-1):
	t = v // fac[i-1]
	v -= t * fac[i-1]
	n += 10**(i-1) * ar[t]
	ar.remove(ar[t])


print(v)
print(n)
