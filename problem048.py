from zth import sqm
r = 0
m = 10**10

for i in range(1,1001):
	r = (r + sqm(i,i,m)) % m;

print(r)
