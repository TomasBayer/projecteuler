from fget import fgetIntMat

def solve(A):
	d = len(A)
	H = [ [0] * d for i in range(0,d) ]
	H[-1][-1] = A[-1][-1]
	for i in range(d-2,-1,-1):
		H[d-1][i] = A[d-1][i] + H[d-1][i+1]
		H[i][d-1] = A[i][d-1] + H[i+1][d-1]
	for i in range(d-2,-1,-1):
		for j in range(d-2,-1,-1):
			H[i][j] = A[i][j] + min(H[i+1][j],H[i][j+1])
	return H[0][0]

print(solve(fgetIntMat("problem081")))
