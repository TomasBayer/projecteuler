from zth import continuedFractionOfRoot, continuedFractions, generatorFromPeriod, intRoot

#      a/n * (a-1)/(n-1) = 1/2
# <=>  2a^2 - 2a = n^2 - n
# <=>  ( (2a-1)^2 - 1 ) / 2 = ( (2n-1)^2 -1 ) / 4
# <=>  (2a-1)^2 * 2 =  (2n-1)^2 + 1 
# <=>  (2n-1)^2 - 2*(2a-1)^2 = -1
# <=>  x^2 - 2*y^2 = -1             (x=2n-1, y=2a-1)

# Pellsche Gleichung. Periodenlaenge von sqrt(2) ist 1.
# Loesungen sind also Kettenbrueche (p_i,q_i) von sqrt(2) mit i ungerade.
# Fuer alle Loesungen (x,y) sind x und y ungerade.

b = 10**12

# n > b <=> x > 2b-1

b = 2*b-1
skip = True
for (p,q) in continuedFractions(generatorFromPeriod(continuedFractionOfRoot(2))):
    skip = not skip
    if skip:
        continue
    if p > b:
        n = (p + 1) // 2
        b = ( intRoot(2*n*(n-1)+1,2) + 1 ) // 2
        print b
        break
