from other import isPandiagonal

m = 0
for i in range(6,9999):
	c,k = str(i), 2
	while len(c) < 9:
		c += str(k*i)
		k += 1
	if len(c) > 9:
		continue
	if isPandiagonal(c):
		m = max(int(c),m)	
print(m)
