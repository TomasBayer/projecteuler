from zth import isRoot
from tools import genRange

def digitsOfRoot(n):
	c, p = n, 0
	while True:
		y, x = 0, 0
		while y <= c:
			y += 20*p + 2*x + 1
			x += 1
		y -= 20*p + 2*x - 1
		x -= 1
		yield x
		p = 10*p + x
		c = (c - y) * 100 

print(sum([ sum(genRange(digitsOfRoot(i),0,100)) for i in range(2,100) if not isRoot(i,2) ]))
