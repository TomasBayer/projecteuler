from fget import fgetIntMat
from tools import printMatrix

def solve(A):
	d = len(A)
	H = [ [None] * d for i in range(0,d) ]
	H[0][0] = A[0][0]
	Q = set([(0,0,A[0][0])])
	F = []
	def relax(x,y,ax,ay):
		if 0 <= ax < d and 0 <= ay < d and (ax,ay) not in F:
			a = H[x][y] + A[ax][ay]
			if H[ax][ay] == None or a < H[ax][ay]:
				H[ax][ay] = a
				Q.add((ax,ay,a))
	while len(Q):
		(x,y,v) = min(list(Q),key=lambda x: x[2])
		relax(x,y,x-1,y)
		relax(x,y,x,y-1)
		relax(x,y,x+1,y)
		relax(x,y,x,y+1)
		Q.remove((x,y,v))
		F.append((x,y))
	return H[-1][-1]

print(solve(fgetIntMat("problem081")))
