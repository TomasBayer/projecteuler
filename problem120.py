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
# m(a) := max { 2an % a^2 | 0 <= n <= phi(a^2), n even }
#       = max { 2an % a^2 | 0 <= n <= a-1, n even }
# => a | m(a) => m(a) <= a*(a-1)

# For odd a, choose n = (a-1) / 2, then
#  2*a*(a-1)/2 % a^2 = a*(a-1) % a^2 = a*(a-1) 
# => m(a)=a*(a-1)

# For even a:
# m(a)  = max { 2an % a^2 | 0 <= n <= a-1, n even }
#       = max { 2an       | 0 <= n <= a/2-1, n even }
#       = 2a*(a/2-1)
#       = a*(a-2)

# s(n) := sum of m(a) for 3 <= a <= n
#       = ( sum of a^2 for 3 <= a <= n ) - ( sum of a for 3 <= a <= n ) - ( sum of a for 3 <= a <= n where a is even )
#       = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( sum of a for 2 <= a <= n where a is even - 2 )
# Let n be even.
# s(n)  = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( sum of 2*a for 1 <= a <= n//2 - 2 )
#       = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( 2 * sum of a for 1 <= a <= n//2 - 2 )
#       = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( 2 * (n//2)*(n//2+1) // 2 - 2 )
#       = n*(n+1)*(2n+1) // 6 - n*(n+1) // 2 - (n//2)*(n//2+1) 
#       = ( 4n^3 - 3n^2 - 10n ) // 12 
# Let n be odd.
# s(n)  = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( sum of a for 1 <= a <= n-1 where a is even - 2 )
# s(n)  = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( sum of 2*a for 1 <= a <= (n-1) // 2 - 2 )
#       = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( 2 * sum of a for 1 <= a <= (n-1)//2 - 2 )
#       = (n*(n+1)*(2n+1) // 6 - 5) - ( n*(n+1) // 2 - 3 ) - ( 2 * ((n-1)//2)*((n-1)//2+1) // 2 - 2 )
#       = n*(n+1)*(2n+1) // 6 - n*(n+1) // 2 - ((n-1)//2)*((n-1)//2+1) 
#       = ( 4n^3 - 3n^2 - 4n + 3 ) // 12 

def s(n):
    return ( 4*n**2 - 3*n - 10 ) * n  // 12

print s(1000)
