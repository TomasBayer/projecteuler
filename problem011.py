from fget import fgetIntMat
from zth import prod
M = fgetIntMat("problem011")

p = 0
d = len(M)

for i in range(0,d):
	for j in range(0,d):
		if i < d-3:
			p = max(p,prod([M[i+k][j] for k in range(0,4)]))
		if j < d-3:
			p = max(p,prod([M[i][j+k] for k in range(0,4)]))
		if i < d-3 and j < d-3:
			p = max(p,prod([M[i+k][j+k] for k in range(0,4)]))
		if i >= 3 and j < d-3:
			p = max(p,prod([M[i-k][j+k] for k in range(0,4)]))

print(p)
