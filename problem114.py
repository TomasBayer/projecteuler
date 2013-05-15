len = 50

cache = [0] * (len + 1)
def anz(n):
    if cache[n]:
        return cache[n]
    elif n < 0:
        return 0
    elif n < 3:
        return 1
    else:
        a = 1 + anz(n-1) # Alle rot + erster schwarz
        for i in range(3,n):
            a += anz(n-i-1) # Vorne rotes Teil der Laenge i
        cache[n] = a
        return a

print anz(len)
