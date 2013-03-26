from zth import arithmFolge, fsqrt
import primeCache as pc

for n in arithmFolge(9,2):
	b = False
	for i in range(0,fsqrt(n/2)+1):
		if pc.isPrime(n - 2 * i**2):
			b = True
			break
	if not b:
		print(n)
		break	
