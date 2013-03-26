n = 100

# Pascalsches Dreieck Bauen
C = [ [0] * n for n in range(1,n+2) ]
C[0][0] = 1
c = 0
for n in range(1,n+1):
	C[n][0] = C[n][n] = 1
	for k in range(1,n):
		C[n][k] = C[n-1][k] + C[n-1][k-1]
		if C[n][k] > 1000000:
			c += 1	
print(c)
