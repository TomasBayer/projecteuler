from primeCache import primesUpTo

N = 5000

S = [p for p in primesUpTo(N)]
l = sum(S)
C = [0] * (l + 1)
C[0] = 1

for p in S:
    print p
    for i in range(l, -1, -1):
        if C[i]:
            C[p+i] += C[i]

print str(sum(map(lambda x: C[x], primesUpTo(l))))[-16:]
