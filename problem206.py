from tools import tupel
from zth import froot

loops = 5

b1 = 1
for i in range(2, loops + 2):
    b1 = b1 * 100 + i
b2 = 10**(18-2*loops)

def stelle(n, a):
    return ( n % (10**a) ) // (10 ** (a-1) )

def check(n):
    if n % 10:
        return False
    for i in range(9, 0, -1):
        a = 21 - 2*i
        if ( n % (10**a) ) // (10 ** (a-1) ) != i:
            return False
    return True

for t in tupel(range(10), loops):
    a = b1
    for i in range(loops):
        a += t[i] * ( 10 ** (2 * i + 1) )
    a *= b2
    r = froot(a,2)
    s = (r + 1) ** 2
    if s % 10:
        continue
    for i in range(9, 0, -1):
        a = 21 - 2*i
        if ( s % (10**a) ) // (10 ** (a-1) ) != i:
            break
    else:
        print r+1
        break
