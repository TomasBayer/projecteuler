from zth import summeTeiler, teiler
d = {}
def tsum(n):
	global d
	if n not in d:
		d[n] = summeTeiler(n)
	return d[n]

s = 0
for i in range(2,10000):
	if tsum(tsum(i)) == i != tsum(i):
		s += i

print(s)
