from zth import rp, isProbablePrime, integersModulo, chinaRest
from primeCache import primes

max = 150 * 10**6

def set(n):
    s = n*n
    return map(lambda x: s + x, [1,3,7,9,13,27])

k = 10
dic = {}
for n in primes():
    T = []
    for i in range(n):
        for r in set(i):
            if not rp(r,n):
                break
        else:
            T.append(i)
    dic[n] = T
    k -= 1
    if k == 0:
        break

C = chinaRest(dic)
candidates = []
for n in integersModulo(C[0], C[1]):
    for i in set(n):
        if not isProbablePrime(i,3):
            break
    else:
        candidates.append(n)
    if n >= max:
        break

print candidates
res = 0
for n in candidates:
    for i in set(n):
        if not isProbablePrime(i):
            break
    else:
        if not isProbablePrime(n*n + 21):
            res += n
print res
