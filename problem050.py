import primeCache as pc

m, n, a, b, c, Mc, Mn = 999999, 2, 2, 2, 1, 0, 0
while True:
	if n > m:
		n -= a
		c -= 1
		a = pc.nextPrime(a)
		while n > m:
			n -= b
			c -= 1
			b = pc.prevPrime(b)
	if pc.isPrime(n) and Mc < c:
		Mn, Mc = n, c
	b = pc.nextPrime(b)
	c += 1
	if b >= m:
		break
	n += b
	
print(Mn)
