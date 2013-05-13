len = 50

cache = [0] * (len + 1)
def anz(n):
    if cache[n]:
        return cache[n]
    elif n < 0:
        return 0
    elif n < 2:
        return 1
    else:
        a = anz(n-1) + anz(n-2) + anz(n-3) + anz(n-4)
        cache[n] = a
        return a

print anz(len)
