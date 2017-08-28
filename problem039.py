from zth import ggt, fsqrt

n = 1000

d = [0] * (n+1)
for i in range(0,fsqrt(2*n+1)-1)//2+1):
	for j in range(1,i):
		if i % 2 != j % 2 and ggt(i,j) == 1:
			h = 2*i*(i+j)
			for k in range(h,1000,h):
				d[k] += 1

print(max(list(range(0,1001)),key=lambda x: d[x]))
