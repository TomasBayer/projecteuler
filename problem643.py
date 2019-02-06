import sympy

# first steps: this is not efficient

def powers(n, bound):
    a = n
    while a <= bound:
        yield a
        a *= n

class Test(object):

    def __init__(self, bound):
        self.bound = bound
        self.primes = list(sympy.primerange(2, bound))
        self.pc = len(self.primes)

    def extend(self, p, q, pi=0, self_yield=False):
        if self_yield:
            yield p, q
    
        if pi < self.pc:

            n = self.primes[pi]

            for pp in powers(n, self.bound // p):
                yield from self.extend(p * pp, q, pi + 1, True)
            for pp in powers(n, self.bound // q):
                yield from self.extend(p, q * pp, pi + 1, True)

            yield from self.extend(p, q, pi + 1, False)

    def run(self):
        c = 0
        for k in powers(2, self.bound):
            for p, q in self.extend(k, k):
                c += 1
        return c // 2

    
for i in range(4,100,2):
    print(i, Test(i).run())
