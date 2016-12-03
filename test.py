from primeCache import primes
from zth import chinaRest

k = 9

def qNonRes(p):
    L = [0] * p
    for i in range(0,p//2+1):
        L[i*i%p] = 1
    A = []
    for i in range(0,p):
        if L[i] == 0:
            A.append(p-i)
    return A

def printSet(A):
    A = sorted(A)
    if len(A) > 10:
        A = A[:10]
        A.append("...")
    return str(A)

C = { 8: [3] }
g = primes()
p = next(g)

print "Ist -m < 7, dann gilt -m === [3] (mod 8)."

for p in g:
    if k == 0:
        break
    k -= 1
    C[p] = qNonRes(p)
    C = chinaRest(C)
    print "Ist -m < " + str(4*p - 1) + ", dann gilt -m === " + printSet(C[0]) + " (mod " + str(C[1]) + ")."
    C = { C[1]: C[0] }
