i = 0
while True:
	for j in range(0,i+1):
		a = i**2 - j**2
		b = 2 * i * j
		c = i**2 + j**2
		if a+b+c == 1000:
			print(a*b*c)
			exit()
	i += 1
