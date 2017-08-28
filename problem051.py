from zth import zahlen
import primeCache as pc

def sterne(s,a):
	if a:
		for h in sterne(s,a-1):
			for i in range(0,len(h)+1):
				if i == 0 or h[i-1] != "*":
					yield h[:i] + "*" + h[i:]
	else:
		yield s

def prototypen(l):
	for k in range(3,l,3):
		for i in range(10**(l-k-1),10**(l-k)):
			for s in sterne(str(i),k):
				yield s


for n in zahlen(4):
	for s in prototypen(n):
		k = 0
		for i in ['1','2','3','4','5','6','7','8','9']:
			if pc.isPrime(int(s.replace("*",i))):
				k += 1
		if k >= 8:
			print(s)
			exit()
