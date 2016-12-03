# langsam!
from primeCache import primes
from zth import chinaRest

# In Z_p^k sind nur 0 und 1 idempotent, dann chinesischer Restsatz.

M = 10**7

idem = coprimeFuncTable(M, lambda p, e: [0, 1], lambda p, q, a, b: chinaRest({ p: a, q: b })[0])

s = 0
for i in range(2,M+1):
    s += max(idem[i])
print s
