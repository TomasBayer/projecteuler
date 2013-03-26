import primeCache as pc

m,p = 0,0
for b in range(1,1001):
	if not pc.isPrime(b):
		continue
	for a in range(-999,1000,1):
		k = 0
		while pc.isPrime(k**2 + a*k + b):
			k += 1
		if k > m:
			m,p = k,a*b

print(p)
