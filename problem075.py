# u,v  u > v, u!==v (2), (u,v)=1
# x = u^2-v^2, y = 2uv, z = u^2+v^2
# d = 2u(u+v)
from zth import rp, fsqrt
N = 1500000
L = [0] * (N+1) 
for u in range(1,fsqrt(N//2+1)):
	for v in range(1,u):
		if rp(u,v) and (u & 1 == 0 or v & 1 == 0):
			d = 2*u*(u+v)
			if d > N:
				continue
			for i in range(d,N+1,d):
				L[i] += 1
print(len([1 for i in L if i == 1]))
