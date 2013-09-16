from random import randrange

m = {}

def c(a):
    s = str(a)
    if s in m:
        return m[s]
    else:
        if len(a) == 1:
            if a[0] == 5:
                r = 0
            else:
                r = 1 + c(range(a[0] + 1, 6))
        else:
            d = 0
            for x in range(len(a)):
                b = a[:x] + a[x+1:] + range(a[x] + 1, 6)
                d += c(b)
            r = float(d) / len(a)
        m[s] = r
        return r

print round(c([1]) - 1, 6)
