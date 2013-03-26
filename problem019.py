from other import wochentag
s = 0
for j in range(1901,2001):
	for m in range(1,13):
		if wochentag(1,m,j) == 0:
			s += 1
print(s)
