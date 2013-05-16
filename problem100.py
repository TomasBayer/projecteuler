from zth import froot, intRoot

# Let n be an integer
#     ex a in Z, s.t. a/n * (a-1)/(n-1) = 1/2
# <=> ex a in Z, s.t. 2a(a-1)=n(n-1)
# <=> ex a in Z, s.t. a^2-a-(n^2-n)/2=0
# <=> (sqrt(2n^2-2n+1) + 1) / 2 is in Z 
# <=> 2n^2-2n+1 is an odd square
# <=> 2n^2-2n+1 is a square
# <=> ex c in Z, s.t.  2n^2-2n+1=c^2
# <=> ex c in Z, s.t. n = (sqrt(2c^2-1)+1)/2
# Let c be an integer
#     ex n in Z, s.t. 2n^2-2n+1=c^2
# <=> (sqrt(2c^2 - 1) + 1) / 2 is in Z
# <=> 2c^2 - 1 is an odd square
# <=> 2c^2 - 1 is a square
#   { n in Z with n >= b, s. t. ex a in Z, s.t. a/n * (a-1)/(n-1) = 1/2 }
# = { (sqrt(2c^2-1) + 1) / 2 | c in Z, 2c^2-1 is a square, 2c^2-1 > (2b-1)^2 }
# = { (sqrt(2c^2-1) + 1) / 2 | c in Z, 2c^2-1 is a square, c > sqrt(2(b-1)(b+1)) }

cache = None
def isSquare(n):
    global cache
    if cache == None:
        a = froot(n,2)
        cache = (a,a*a)
    while n > cache[1]:
        cache = ( cache[0] + 1, cache[1] + 2*cache[0] + 1 )
    return n == cache[1]

b = 10**12
c = froot(2*(b-1)*(b+1), 2)
a = 2*c*c-1
while True:
    r = intRoot(a, 2)
    if r:
        print (r + 1) // 2
        break
    a += 4*c + 2
    c += 1
