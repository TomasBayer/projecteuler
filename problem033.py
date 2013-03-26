from zth import ggt
n,z = 1,1
for a in range(1,10):
	for b in range(1,10):
		for c in range(a,10):
			if (9*a + b) * c == 10 * a * b and not a == b == c:
				n *= 10*b + c
				z *= 10*a + b
print(n//ggt(n,z))
