from zth import prod
def nteStelle(n):
	n -= 1
	i = 0
	while n > 9 * 10 ** i * (i+1):
		n -= 9 * 10 ** i * (i+1)
		i += 1
	return int(str(10**i + n//(i+1))[n % (i+1)])

print(prod([nteStelle(10**i) for i in range(0,7)]))
