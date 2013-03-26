from fget import fgetIntList

I, s, C = [], "", set()
for i in fgetIntList("problem079"):
	L = [int(k) for k in str(i)]
	C = C | set(L)
	I.append((L[0],L[1]))
	I.append((L[1],L[2]))
while len(C):
	for i in C:
		h = True
		for k in I:
			if k[1] == i:
				h = False
				break
		if h:
			s += str(i)
			C.remove(i)
			I = [ k for k in I if k[0] != i ]
			break
print(s)
