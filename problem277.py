from zth import inv

S = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"[::-1]

bound = 10**15

a,b,c = 1,0,1
for s in S:
    a *= 3
    b *= 3
    if s == 'd':
        b += c
        c *= 2
    elif s == 'U':
        b -= 2*c 
        c *= 4
    elif s == 'D':
        continue

# (n*a+b) / c > bound <=> n > ( c * bound - b ) / a => n > ( c*bound - b) // a
bound = (c * bound - b) // a

r = ((-1) * ( (b%c * inv(a%c, c)) % c) + c) % c
m = c

s = bound % m
while r <= s:
    r += m
n = bound + r - s
print ( n*a + b ) // c
