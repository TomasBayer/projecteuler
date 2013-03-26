from zth import isAbundant
m = 28124
A = [isAbundant(i) for i in range(12,m-11)]
B = [i for i in range(12,m-11) if A[i-12]]

def isSum(n):
	global A, B
	for i in B:
		if 2*i > n:
			return False
		elif A[n-i-12]:
			return True
	return False

print(sum((i for i in range(1,m) if not isSum(i))))
