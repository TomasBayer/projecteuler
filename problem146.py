from zth import rp, isProbablePrime

max = 150 * 10**2

def set(n):
    s = n*n
    return map(lambda x: s + x, [1,3,7,9,13,27])

m = 2
residues = []
for i in range(m):
    for r in set(i):
        if not rp(r,m):
            break
    else:
        residues.append(i)

steps = []
for i in range(1,len(residues)):
    steps.append(residues[i]-residues[i-1])
steps.append(m+residues[0]-residues[-1])

k = 0
l = len(steps)
n = residues[0]

candidates = []
while True:
    for i in set(n):
        if not isProbablePrime(i,3):
            break
    else:
        candidates.append(n)
    n += steps[k]
    if n >= max:
        break
    k += 1
    if k == l:
        k = 0

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
