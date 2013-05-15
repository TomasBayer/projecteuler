from primeCache import nthPrime

max = 4000000

maxPower = 10 # <-- nicht-deterministisch

# Let (x,y,n) be as solution (with x <= y)
#   1) y = nx / (x-n) => x-n > 0 => x > n
#   2) x <= y => x <= nx / (x-n) => x <= 2n
# => n < x <= 2n

# Let x and n be natural number,
#     ex. y, such that (x,y,n) is a solution 
# <=> ex. y, such that (x-n)y=nx 
# <=> x-n | nx 
# <=> nx === 0 (mod x-n)
# <=> nn === 0 (mod x-n)
# <==> x-n | n^2

#   #{ x | ex. y: (x,y,n) solution }
# = #{ n < x <= 2n | x-n | n^2 }
# = #{ 1 <= x <= n  | x | n^2 }
# = ( anzahlTeiler(n^2) - 1 ) / 2 + 1

# n = min { product(p_i^a_i) | finite sequences (a_i) with product(2a_i+1) > max)

def candidates(n, a, k):
    if a > n:
        return [[]]
    b = []
    a1 = k
    prod = (2*k+1) * a
    while prod <= n + 2*a and a1 < maxPower:
        b = b + map(lambda x: x + [a1], candidates(n, prod, a1))
        a1 += 1
        prod += 2*a
    return b

min = None
for t in candidates(2*max - 1, 1, 1):
    c = 1
    for i in range(len(t)):
        c *= nthPrime(i+1) ** t[i]
        if min != None and c > min:
            break
    else:
        min = c
print min
