from zth import collatz

n = 1000000
cache = {1:1}

def get(n):
	global cache
	if n not in cache:
		if n % 2 == 0:
			cache[n] = 1 + get(n >> 1)
		else:
			cache[n] = 1 + get(3*n + 1)
	return cache[n]

p, m = 1, 1
for i in range(n//2,n):
	l = get(i)
	if l > m:
		p, m = i, l 

print(p)
