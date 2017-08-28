# C[n][m] =  Number of possibilities to write n as a sum of primes <= m 
from zth import zahlen
import primeCache as pc

N = 5000
C = [{0:1},{1:0}]

def c(a,b):
	if b > a:
		b = a
	global C
	return C[a][b]

for n in zahlen(2):
	t = {}
	k = 0
	for m in pc.primesUpTo(n):
		k += c(n-m,m)
		t[m] = k
	t[n] = k
	if k >= N:
		print(n)
		break;
	C.append(t)
