from zth import continuedFractionOfRoot, continuedFractions, generatorFromPeriod, intRoot

# Case 1:
# n, n, n+1 works
# <=> (n+1)/4 * sqrt((2n)^2-(n+1)^2) in Z
# <=> (n+1)/4 * sqrt(3n^2-2n-1) in Z
# <=> 3n^2-2n-1 is a square and 4 | (n+1) * sqrt(3n^2-2n-1)
# <=> 3n^2-2n-1 is a square and 16 | (n+1)^2 * (3n^2-2n-1)
# <=> 3n^2-2n-1 is a square and n is odd
# <=> ex a: 3n^2-2n-1=a^2 and n is odd
# <=> ex a: (3n-1)^2-4=3a^2 and n is odd
# <=> ex a: ((3n-1)/2)^2-3(a/2)^2=1 and n is odd
# <=> ex a: x^2-3y^2=1 and 3 | 2x + 1                   (with x=(3n-1)/2 and y = a/2)

# Pellsche Gleichung. Periodenlaenge von sqrt(3) ist 2.
# Loesungen sind also Kettenbrueche (p_i,q_i) von sqrt(2) mit i gerade.

# Case 2:
# n, n, n-1 works
# <=> (n-1)/4 * sqrt((2n)^2-(n-1)^2) in Z
# <=> (n-1)/4 * sqrt(3n^2+2n-1) in Z
# <=> 3n^2+2n-1 is a square and 4 | (n-1) * sqrt(3n^2+2n-1)
# <=> 3n^2+2n-1 is a square and 16 | (n-1)^2 * (3n^2+2n-1)
# <=> 3n^2+2n-1 is a square and n is odd
# <=> ex a: 3n^2+2n-1=a^2 and n is odd
# <=> ex a: (3n+1)^2-4=3a^2 and n is odd
# <=> ex a: ((3n+1)/2)^2-3(a/2)^2=1 and n is odd
# <=> ex a: x^2-3y^2=1 and 3 | 2x - 1                   (with x=(3n+1)/2 and y = a/2)

b = 10**9

skip = False
k = 1
sum = 0
for (p,q) in continuedFractions(generatorFromPeriod(continuedFractionOfRoot(3))):
    skip = not skip
    if skip:
        continue
    r = p % 3
    if r == 0:
        continue
    if r == 1:
        peri = 2*(p+1)
    if r == 2:
        if p <= 3:
            continue
        peri = 2*(p-1)
    if peri > b:
        break
    else:
        sum += peri
print sum
