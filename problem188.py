from zth import sqm

def hyper(a,k,m):
    r = 1
    for _ in range(k):
        r = sqm(a, r, m)
    return r

print hyper(1777,1855,10**8)
