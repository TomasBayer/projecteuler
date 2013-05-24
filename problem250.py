from zth import sqm

N, m, M = 250250, 250, 10**16

res = [0] * m
for i in range(1,N+1):
    res[sqm(i,i,m)] += 1

subsets = [0] * m
subsets[0] = 1
for j in range(m):
    for _ in range(res[j]):
        subsets = [(subsets[k] + subsets[k-j]) % M for k in range(m)]

print subsets[0]-1
