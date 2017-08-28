P = [i**5 for i in range(0,10)]
s = 0
for a in range(2,1000001):
	if sum([P[int(i)] for i in str(a)]) == a:
		s += int(a)
print(s)
