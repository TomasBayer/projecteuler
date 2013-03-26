def isBinaryPalindrom(n):
	s = bin(n)[2:]
	return s[:len(s)//2] == s[:(len(s)-1)//2:-1]

r = 0
for n in range(1,1000):
	s = str(n)
	k = int(s + s[::-1])
	if isBinaryPalindrom(k):
		r += k
	k = int(s[:-1] + s[::-1])
	if isBinaryPalindrom(k):
		r += k

print(r)
