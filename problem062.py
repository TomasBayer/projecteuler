from zth import powers
M = {}
L = {}
for n in powers(3):
	s = ''.join(sorted(str(n)))
	if s in M:
		M[s] += 1
		if M[s] == 5:
			print(L[s])
			break 
	else:
		M[s] = 1
		L[s] = n
	
