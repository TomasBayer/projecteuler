from zth import polygonalZahlen

# Fülle Cache
P = []
N = 6
for i in range(3,N+3):
	h = []
	for n in polygonalZahlen(i):
		if n > 999:
			h.append(n)
		if n > 9999:
			break
	P.append(h)

def candidates(k, s):
	if s < 10:
		return
	a,b = s*100,(s+1)*100 
	for i in P[k-3]:
		if i >= b:
			break	
		if i >= a:
			yield i


def chains(s,l):
	if len(l):
		for i in range(0,len(l)):
			for k in candidates(l[i],s):
				for C in chains(k % 100, l[:i] + l[i+1:]):
					yield [k] + C
	else:
		yield []
		
	

for i in P[N-1]:
	for C in chains(i % 100,list(range(3,N+2))):
		if C[-1] % 100 == i // 100:
			print( i + sum(C) )
