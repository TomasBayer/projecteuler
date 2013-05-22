from zth import inv, rk
from primeCache import primes
from tools import next
from math import log10

max = 1000000

def s(p1,p2):
    k = 10 ** (int(log10(p1)) + 1)
    return k * rk( -1 * p1 * inv(k, p2), p2) + p1

p1 = 5
res = 0
a = primes()
for p in a:
    if p == 5:
        break
for p2 in a: 
    if p1 > max:
        break
    res += s(p1,p2)
    p1 = p2

print res
