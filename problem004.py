def isPalindrom(n):
	s = str(n)
	return s[0] == s[5] and s[1] == s[4] and s[2] == s[3]

m = 0
for i in range(1,1000):
	for j in range(1,1000):
		if 100000 < i*j > m and isPalindrom(i*j):
			m = i*j
print(m)
