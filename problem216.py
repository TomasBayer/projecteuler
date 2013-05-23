from zth import integersModulo, isProbablePrime

max = 10000

c = 0
n = 1
a = 1
h = 6
while n < max:
    if isProbablePrime(a):
        c += 1
    a += h
    h += 4
    n += 1
print c
