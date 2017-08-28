from other import isPandiagonal
R = set()

def pNum(a,b):
	for i in range(a,b+1):
		if isPandiagonal(str(i)):
			yield i

for i in pNum(1,99):
	si = str(i)
	for k in pNum(101,9999):
		p = i*k
		s = si + str(k) + str(p)
		l = len(s) - 9
		if l > 0:
			break
		elif l == 0 and isPandiagonal(s):
			R.add(p)

print(sum(list(R)))
