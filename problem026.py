from zth import ord, maxDiv
def cycle(n):
	n = maxDiv(n,[2,5])
	if n == 1:
		return 0
	else:
		return ord(10,n)

p, m = 1, 0
for i in range(1,1000):
	h = cycle(i)
	if h > m:
		p, m = i, h
print(p,m)
