from zth import zahlen
import primeCache as pc

Cache = []
def candidates(n,m):
	global Cache
	if n:
		for i in Cache[n-1][0]:
			yield i
		h = []
		for p in pc.primesFrom(Cache[n-1][1]+1):
			if m != None and p > m:
				break
			sp = str(p)
			for C in candidates(n-1,p-1):
				b = True
				for c in C:
					sc = str(c)
					if not pc.isPrime(int(sp+sc)) or not pc.isPrime(int(sc+sp)):
						b = False
						break
				if b:
					yield C + [p]
					h.append(C + [p])
		Cache[n-1] = (Cache[n-1][0] + h, m)
	else:
		yield []

n=5
Cache = [ ([],0) for i in range(0,n) ] 
for i in candidates(n,None):
	print(sum(i))
	break
