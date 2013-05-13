len = 50

cache = [ [0] * (len + 1) for _ in range(0,5) ]
def anz(k, n):
    if cache[k][n]:
        return cache[k][n]
    elif n < k:
        return 1
    else:
        a = anz(k, n-1) + anz(k, n-k)
        cache[k][n] = a
        return a

print sum(map(lambda k: anz(k, len) - 1, [2,3,4]))
