from zth import fsqrt,phi

N = 1000000

def teiler(n):
	for i in range(2,fsqrt(n)+1):
		if n%i == 0:
			return i
	return None

Phi = [ 0, 1 ]
for i in range(2,N+1):
	k = teiler(i)
	if k == None:
		Phi.append(i-1)
	else:
		r = i // k
		if r % k:
			Phi.append((k-1)*Phi[r])
		else:
			Phi.append(k*Phi[r])
print(sum(Phi)-1)
