from zth import zahlen

def nearest(m,N):
	a, h = N, N
	for n in range(1,m+1):
		a -= n * m * (m+1) // 2	
		if a < 0:
			if -a < h:
				return (m,n,-a)
			else:
				return (m,n-1,h)
		h = a
	return (m,m,a)


N = 2000000
b = (0,0,N+1)
for m in zahlen(1):
	n = nearest(m,N)
	if n[1] == 0:
		break
	b = min(n,b,key=lambda x: x[2])
print(b[0]*b[1])
