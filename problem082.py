from fget import fgetIntMat

def solve(A):
	d = len(A)
	H = [ [ [None, None] for i in range(0,d) ] for i in range(0,d) ]
	for i in range(0,d):
		H[i][d-1] = A[i][d-1]
	for j in range(d-2,-1,-1):
		H[d-1][j][0] = A[d-1][j] + H[d-1][j+1]
		H[0][j][1] = A[0][j] + H[0][j+1]
		for i in range(d-2,-1,-1):
			H[i][j][0] = A[i][j] + min(H[i+1][j][0],H[i][j+1])
		for i in range(1,d):
			H[i][j][1] = A[i][j] + min(H[i-1][j][1],H[i][j+1])
		for i in range(0,d):
			H[i][j] = min(H[i][j])
	return min([H[i][0] for i in range(0,d)]) 

print(solve(fgetIntMat("problem081")))
