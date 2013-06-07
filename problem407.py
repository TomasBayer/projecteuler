# langsam!
from primeCache import primes
from zth import chinaRest

# In Z_p^k sind nur 0 und 1 idempotent, dann chinesischer Restsatz.

M = 10**7

fact = [None] * (M + 1)

def zerlege(n, p):
    f = 1
    while n % p == 0:
        n, f = n // p, f * p
    return (f, n)

for n in primes():
    if n > M:
        break
    for i in range(n, M+1, n): 
        fact[i] = zerlege(i, n)

idem = [None] * (M + 1)
idem[1] = [0]

def gidem(i):
    if idem[i] != None:
        return idem[i]
    (p, r) = fact[i]
    if r == 1:
        idem[i] = [0,1]
    else:
        idem[i] = chinaRest({ p: [0,1], r: gidem(r) })[0]
    return idem[i]

s = 0
for i in range(1,M+1):
    s += max(gidem(i))
print s
