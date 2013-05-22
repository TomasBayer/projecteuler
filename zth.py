import itertools as it
from functools import reduce
from random import randint
from tools import allTrue

# Generatorobjekte fuer Zahlenfolge
def fibonacci():
	a, b = 1, 1
	while True:
		yield b
		a, b = a+b, a 

def arithmFolge(a,k):
	while True:
		yield a
		a += k

def geomFolge(a,k):
	while True:
		yield a
        a *= k

def integersModulo(L, m):
    if isinstance(L, list):
        L.sort()
    else:
        L = [L]
    l = len(L)
    S = []
    for i in range(1, l):
        S.append(L[i]-L[i-1])
    S.append(m+L[0]-L[-1])

    k = 0
    n = L[0]
    while True:
        yield n
        n += S[k]
        k += 1
        if k == l:
            k = 0

def zahlen(a):
	while True:
		yield a
		a += 1

def powers(k):
	a = []
	for i in range(0,k):
		h, t = 0, i
		for n in binomReihe(i):
			if t&1 == i&1:
				h += n * (t**k)
			else:
				h -= n * (t**k)
			t -= 1 
		a.append(h)
	f = fac(k)
	while True:
		for i in range(0,k-1):
			a[i] += a[i+1]
		a[k-1] += f
		yield a[0]

def polygonalZahlen(k):
	n,i,m = 1, k-2, 1
	while True:
		yield n
		m += i
		n += m	

def distinctPowers(a,b):
	C = [list(range(2,b+1))]
	for l in range(2,a.bit_length()):
		h = [] 
		for k in range(2,b+1):
			if allTrue([k*l > b * i or (k*l) % i != 0 for i in range(1,l)]):
				h.append(k) 
		C.append(h)
	for i in range(2,a+1):
		h, t = 1, 0
		for c in C[maxPot(i)-1]:
			h *= i**(c-t)
			t = c
			yield h	

def collatz(n):
	while True:
		yield n
		if n == 1:
			return
		elif n % 2 == 0:
			n >>= 1
		else:
			n = 3*n + 1

def erathostenes():
    D = { 9: 3, 25: 5 } 
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2), 
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q 
            yield q
        else:
            x = q + 2*p 
            while x in D or (x%30) not in MODULOS:
                x += 2*p 
            D[x] = p   

def numberOfIntegerPartitions():
	C = [1]
	def coeff(n):
		l = len(C)
		for i in C:
			if i > n:
				return
			yield i
		m = (l+1)//2
		while True:
			if l % 2:
				C.append(C[-1]+m)			
			else: 
				C.append(C[-1]+2*m+1)
				m += 1
			if C[-1] > n:
				break
			yield C[-1]
			l += 1
	P = [1,1]
	yield 1
	yield 1
	for n in zahlen(2):
		s, h = 0,0
		for k in coeff(n):	
			if h < 2:
				s += P[n-k]
			else:
				s -= P[n-k]
			h = (h+1) % 4
		yield s
		P.append(s)

# abgerundete reellwertige Funktionen 
def froot(n,k):
	a,b = 0,n
	while b >= a:
		m = (b+a) >> 1
		t = m**k
		if t == n:
			return m
		elif t < n:
			a = m+1
		else:
			b = m-1
	return a-1

def fsqrt(n):
	return froot(n,2)

## Kettenbruchentwicklung
def generatorFromPeriod(L,F=-1):
	if F == -1:
		L, F = L[0], L[1]
	for i in L:
		yield i
	while True:
		for i in F:
			yield i

def continuedFractions(gen):
	P1, P2, Q1, Q2 = 1, 0, 0, 1
	for n in gen:
		P1, P2 = n * P1 + P2, P1
		Q1, Q2 = n * Q1 + Q2, Q1
		yield (P1,Q1)

def continuedFractionOfRoot(N):
	w = fsqrt(N)
	if w**2 == N:
		return ([w],[])
	a, m, s = w, 0, 1
	A = [(a,m,s)]
	while True:
		m = s*a - m
		s = (N - m**2) // s
		a = (w + m) // s
		T = (a,m,s)
		h = T in A
		A.append(T)	
		if h:
			break
	L, F, h = [], [], False
	for i in A[:-1]:
		if A[-1] == i:
			h = True
		if h:
			F.append(i[0])
		else:
			L.append(i[0])
	return (L,F)
	
# Effizientes Rechnen in Zp
def ggt(a,b):
	if b:
		return ggt(b, a % b)
	else:
		return a

def rp(a,b):
	return ggt(a,b) == 1

def rk(a,m):
    a = a % m
    if a < 0:
        return a + m
    else:
        return a

def kgv(a,b):
	return a * b // ggt(a,b)

def sqm(a,b,m):
	res = 1
	while b:
		if b % 2 == 1:
			res = (res * a) % m
		a = (a**2) % m
		b >>= 1
	return res

def _inv(a,b):
    if b == 0:
        return (a,1,0)
    else:
        tmp = _inv(b,a%b)
        return (tmp[0],tmp[2],tmp[1] - a // b * tmp[2])

def inv(a,m):
    r = _inv(a,m)
    if r[0] != 1:
        return None
    else:
        return rk(r[1], m)

def chinaRest(cong):
    M = reduce(lambda x,y: x*y, cong.keys())
    s = 0
    res = [0]
    for m in cong:
        mm = M // m
        t = _inv(m, mm)[2] * mm
        neu = []
        if not isinstance(cong[m], list):
            cong[m] = [cong[m]]
        for a in cong[m]:
            for s in res:
                neu.append(s + a * t)
        res = neu
    return (map(lambda s: rk(s,M), res), M)

# Primfaktorenzerlegung
def factorize(n):
	if n < 2:
		return
	while True:
		o = n
		for i in range(2,fsqrt(n)+1):
			if n % i == 0:
				yield i
				n //= i
				break
		if o == n:
			yield n
			return 

def factorization(n):
	if n < 2:
		return
	a, m = 1, 1
	for i in factorize(n):
		if i != a:
			if a != 1:
				yield (a,m)
			a, m = i, 1
		else:
			m += 1
	yield (a,m)

def phi(n):
	r = 1
	for p, e in factorization(n):
		r *= p ** (e-1) * (p-1)
	return r


def teiler(n): ## nicht sortiert
	t = {1:[1]}
	yield 1
	for p,e in factorization(n):
		t[p] = []
		for a in t:
			if p != a:
				for k in t[a]:
					h = k * p
					for i in range(0,e):
						yield h
						t[p].append(h)
						h *= p

def anzahlTeiler(n):
	return prod([e+1 for p,e in factorization(n)])

def summeTeiler(n):
	return sum(list(teiler(n))) - n

def isAbundant(n):
	return summeTeiler(n) > n

def isDeficient(n):
	return summeTeiler(n) < n

def isPerfect(n):
	return summeTeiler(n) == n

# Primzahltests
def isProbablePrime(n, rounds=20):
	s, d = 0, n-1
	if n < 2:
		return False
	while d % 2 == 0:
		d >>= 1
		s += 1
	if not s:
		return n == 2
	for _ in xrange(rounds):
		a = randint(2,n-1)
		if not rp(a,n):
			return False
		m = sqm(a,d,n)	
		if m == 1 or m == n-1:
			continue
		h = False
		for r in range(1,s):
			m = sqm(m,2,n)
			if m == n-1:
				h = True
				break
		if not h:
			return False
	return True

# Ganzzahliges Wurzeln und Tests auf echte Potenz
def intRoot(n,k):
	a,b = 0,n
	while b >= a:
		m = (b+a) >> 1
		t = m**k
		if t == n:
			return m
		elif t < n:
			a = m+1
		else:
			b = m-1
	return None

def isRoot(n,k):
	return intRoot(n,k) != None

def maxPot(n):
	for i in range(n.bit_length(),0,-1):
		if isRoot(n,i):
			return i

# Test auf Polygonalzahlen
def isPolygonal(n,k):
	h = intRoot(8*(k-2)*n+(k-4)**2)
	if h == None:
		return False
	return (h+k-4) % (2*(k-2)) == 0

def isPentagonal(n):
	h = intRoot(24*n+1,2)
	if h == None:
		return False
	return h % 6 == 5

def isTriangle(n):
	return isRoot(8*n+1,2)


# Sonstige
def binomReihe(n):
	a = 1
	yield a
	for k in range(0,n):
		a = ( a * (n-k) ) // (k+1)
		yield a

def ord(n,p): ## Ordnung von n in Z*p
	k,r = 1, n % p
	while r > 1:
		k += 1
		r = (r * n) % p
	return k

def maxDiv(n,l):
	if type(l) != type(list()):
		l = [l]
	for p in l:
		while n % p == 0:
			n //= p
	return n

def quersumme(n):
	r = 0
	for i in str(n):
		r += int(i) 	
	return r

def fac(n):
	r = 1
	for i in range(1,n+1):
		r *= i
	return r

def prod(l):
	return reduce(lambda x,y: x*y, l, 1)
