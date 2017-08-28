from zth import isPentagonal, polygonalZahlen
from tools import next
		
P = [0]
g = polygonalZahlen(5)
def nthPen(n):
	global P, g
	for i in range(len(P),n+1):
		P.append(next(g))
	return P[n]

i = 1
while True:
	d = nthPen(i)	
	k, h = 1, 1
	while h > 0:
		h = 2*d-3*k*k+k
		if h > 0 and h % (6 * k) == 0:
			n = h // (6*k)
			if isPentagonal(nthPen(n+k)+nthPen(n)):
				print(d)
				exit()
		k += 1
	i += 1
