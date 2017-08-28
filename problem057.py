P = [0,1,1]
Q = [1,0,1]

s = 0
for i in range(0,1000):
	p = 2*P[-1]+P[-2]
	q = 2*Q[-1]+Q[-2]
	P.append(p)
	Q.append(q)
	if len(str(p)) > len(str(q)):
		s += 1	
print(s)
