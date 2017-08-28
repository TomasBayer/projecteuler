import primeCache as pc

k = 1
for p in pc.primes():
	k *= p
	if k > 1000000:
		print(k//p);
		break
