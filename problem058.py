from zth import arithmFolge, isProbablePrime
p, n = 0, 1

for i in arithmFolge(3,2):
	n += 4
	for k in range(i*i,i*i-3*i+2,1-i):
		if(isProbablePrime(k)):
			p += 10
	if p < n:
		print(i)
		exit()
