'''
Sei T(m,n) = Anzahl der Wegen in m x n - Gitter
Dann ist:
	T(m,0) = T(0,n) = 1	T(m,n) = T(m-1,n)+T(n-1,m)
'''

n = 20
t = [[1] * (n+1)] + [[1] + [0] * n for k in range(0,n)]

def get(m,n):
	global t
	if t[m][n] == 0:
		t[m][n] = get(m-1,n) + get(m,n-1)
	return t[m][n]

print(get(n,n))
