from zth import rp
from math import ceil
N = 12000

k = 0
for d in range(2,N+1):
	for n in range(d//3+1,ceil(d/2)):
		if rp(d,n):
			k += 1

print(k)
