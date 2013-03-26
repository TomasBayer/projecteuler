from functools import reduce

def allTrue(L):
	for i in L:
		if not i:
			return False
	return True

def oneTrue(L):
	for i in L:
		if i:
			return True
	return False

def next(g):
	return g.__next__()

def genObject(g, n): 
	for i in range(1,n):
		next(g)
	return next(g)

def genRange(g,a,b):
	for i in range(0,a):
		next(g)
	for i in range(a,b):
		yield next(g)

def concat(l):
	return ''.join(l)

def printMatrix(l):
	m = [0] * len(l[0])
	for i in l:
		for k in range(0,len(i)):
			m[k] = max(m[k], len(str(i[k])))
	for i in l:
		s = ""
		for k in range(0,len(i)):
			s += str(i[k]).rjust(m[k]+1," ")
		print(s)

def tupel(L,k):
	if k:
		for i in L:
			for T in tupel(L,k-1):
				yield [i] + T
	else:
		yield []
