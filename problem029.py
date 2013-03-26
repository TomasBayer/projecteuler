from tools import allTrue
from zth import maxPot

def sophisticated(n):
	C = [n-1]
	for l in range(2,n.bit_length()):
		h = 0 
		for k in range(2,n+1):
			if allTrue([k*l > n * i or (k*l) % i != 0 for i in range(1,l)]):
				h += 1
		C.append(h)
	return sum([C[maxPot(a)-1] for a in range(2,n+1)])

def bruteforce(n):
	s = set()
	for a in range(2,n+1):
		h = a
		for b in range(2,n+1):
			h *= a
			s.add(h)
	return len(s)

n = 100
print(bruteforce(n))
print(sophisticated(n))
