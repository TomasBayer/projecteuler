from zth import erathostenes, zahlen

L = []
P = []
e = erathostenes()

def _next():
	global e, L, P
	p = next(e)
	for i in range(len(L),p):
		L.append(False)
	L.append(True)
	P.append(p)
	return p

def primes():
	for k in zahlen(0):
		if k < len(P):
			yield P[k]
		else:
			yield _next()

def primesUpTo(n):
	for i in primes():
		if i > n:
			return
		yield i

def primesFrom(n):
	for i in primes():
		if i >= n:
			yield i
		
def primesBetween(a,b):
	for i in primes():
		if i > b:
			return
		if i >= a:
			yield i
def isPrime(n):
	if n < 2:
		return False
	global L
	k = len(L)
	while n >= k:
		k = _next() + 1	
	return L[n]

def prevPrime(n):
	global L
	for i in range(n-1,1,-1):
		if isPrime(i):
			return i
	return None

def nextPrime(n):
	global L
	for i in zahlen(n+1):
		if isPrime(i):
			return i

def nthPrime(i):
	global P
	for k in range(len(P),i):
		_next()
	return P[i-1]
