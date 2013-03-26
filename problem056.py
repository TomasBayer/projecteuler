from zth import distinctPowers, quersumme

m = 0
for n in distinctPowers(100,100):
	m = max(m,quersumme(n))
print(m)
