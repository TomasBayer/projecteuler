import primeCache as pc

def candidates():
	global L
	for i in range(1000,9999):
		if pc.isPrime(i) and i != 1487:
			for k in range(2,(10000-i)//2,2):
				if pc.isPrime(i+k) and pc.isPrime(i+2*k):
					yield (i,i+k,i+2*k)

for (a,b,c) in candidates():
	if set(str(a)) == set(str(b)) == set(str(c)):
		print(str(a)+str(b)+str(c))
