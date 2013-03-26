def isPalindrom(n):
	s = str(n)
	k = len(s)
	for i in range(0,k//2):
		if s[i] != s[k-i-1]:
			return False
	return True 

def isLychrel(n):
	for i in range(0,50):
		n = n + int(str(n)[::-1])
		if isPalindrom(n):
			return False
	return True

print(len([i for i in range(1,10000) if isLychrel(i)]))
