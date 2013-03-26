from zth import arithmFolge, erathostenes, ggt
import primeCache as pc 

N = 999999

sDivs = [0] * (N+1)
for p in erathostenes():
	if p > N:
		break;
	for k in arithmFolge(p,p):
		if k > N:
			break;
		sDivs[k] = p

Phi = [0,1]
C = (0,3)

for n in range(2,N+1):
	k = sDivs[n]
	if k == n:
		Phi.append(k-1)
	else:
		d = n//k
		g = ggt(k,d)
		d = Phi[k] * Phi[d] * g // Phi[g]
		Phi.append(d)
		if sorted(str(d)) == sorted(str(n)):
			C = min(C,(n,n/d),key=lambda x: x[1])

print(C[0])
