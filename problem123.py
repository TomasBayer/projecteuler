from primeCache import primes
# (a+1)^n = sum of (n i) a^i * 1^(n-i) over i=0,...,n
#         = sum of (n i) a^i           over i=0,...,n
#         = (n 0) a^0 + (n 1) a^1
#         = 1 + na
# (a-1)^n = sum for (n i) a^i * (-1)^(n-i) over i=0,...,n
#         = (n 0) a^0 * (-1)^n + (n 1) a^1 * (-1)^(n-1)
#         = (-1)^n + na * (-1)^(n-1)
#         = { 1 - an if n is odd
#           { an - 1 if n is even
# (a-1)^n+(a+1)^n = { 2 if n is odd
#                   { 2an if n is even

# For odd n: Remainder of n is 2*p_n*n

# Fuer hinreichend grosse n ist n < 2*p_n, damit 2*p_n*n > n^2, damit ist 2*p_n*n der Rest.

max = 10**10

max //= 2
n = 1
for p in primes():
    if n & 1 == 1 and p*n > max:
        print n
        break
    n += 1
