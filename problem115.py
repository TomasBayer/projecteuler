from zth import zahlen
m = 50

cache = []
def anz(n):
    if n < len(cache) and cache[n]:
        return cache[n]
    elif n < 0:
        return 0
    elif n < m:
        return 1
    else:
        a = 1 + anz(n-1) # Alle rot + erster schwarz
        for i in range(m,n):
            a += anz(n-i-1) # Vorne rotes Teil der Laenge i
        while n >= len(cache):
            cache.append(0);
        cache[n] = a
        return a

for i in zahlen(50):
    if anz(i) > 1000000:
        print i
        break
