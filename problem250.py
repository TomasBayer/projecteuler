from zth import sqm

N = 250250
m = 250

res = [0] * m
for i in range(1,N+1):
    res[sqm(i,i,m)] += 1
print res

subsets = [0] * m
subsets[0] = 1
for j in range(m):
    neu = [i for i in subsets]
    for k in range(m):
        neu[(j+k)%m] += res[j] * subsets[k]
    subsets = neu

print str(subsets[0]-1)[-16:]
