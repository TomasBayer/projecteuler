from zth import zahlen
from math import log10

k = 7

max = k * 81

ends = [0] * (max + 1)
ends[1] = 1
ends[89] = 89

sq = map(lambda x: x*x, range(0,10))
def sumsq(n):
    a = 0
    while n:
        (n, r) = divmod(n, 10)
        a += sq[r]
    return a

def end(n):
    if ends[n]:
        return ends[n]
    else:
        b = end(sumsq(n))
        ends[n] = b
        return b

count = [1] + [0] * max
for _ in range(1, k+1):
    ncount = [0] * (max + 1)
    for i in xrange(0,max+1):
        if count[i]:
            for r in xrange(0,10):
                ncount[i+sq[r]] += count[i]
    count = ncount

c = 0
for i in xrange(1,max+1):
    if end(i) == 89:
        c += count[i]
print c
