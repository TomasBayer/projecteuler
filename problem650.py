#!/usr/bin/env python3
from functools import reduce
from itertools import takewhile
from sympy import factorint, primerange

N = 20000
MOD = 1000000007

prod = lambda it: reduce(lambda x,y: (x * y) % MOD, it, 1)

class PrimePowerSum:

    def __init__(self, p):
        self.p = p
        self.m = 1
        self.s = 1
        self.cache = {}
        self.C = -1

    def __call__(self, k):
        if k > self.C:
            for j in range(self.C+1, k+1):
                self.cache[j] = self.s
                self.m = (self.m * self.p) % MOD
                self.s = (self.s + self.m) % MOD
            self.C = k
        return self.cache[k]
    

PRIMES = list(primerange(2, N))
PRIME_FACS = { n: factorint(n) for n in range(1, N+1) }
PRIME_POWER_SUMS = { p : PrimePowerSum(p) for p in PRIMES }

def d(n):
    C = { p: 0 for p in takewhile(lambda p: p <= n, PRIMES) }
    for i in range(2, n+1):
        for p in PRIME_FACS[i]:
            C[p] += PRIME_FACS[i][p] * (2 * i - n - 1)
    return prod(PRIME_POWER_SUMS[p](k) for p, k in C.items())


S = 0
for n in range(1, N+1):
    S = (S + d(n)) % MOD

print(S)
