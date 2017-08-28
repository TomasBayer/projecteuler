from zth import ggt
from math import ceil
N = 1000000

m = (0,1,0)
for d in range(2,N+1):
	for n in range(d*m[0]//m[1]+1,ceil(d*3/7)):
		g = ggt(d,n)
		m = max((n//g,d//g,n/d),m,key=lambda x: x[2])

print(m)
