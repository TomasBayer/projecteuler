max = 10**6
mod = 10**3

sum = 0
for i in xrange(1,mod):
    for n in xrange(i, max + 1, mod):
        sum += ( (i**2 % mod) * (max // n) ) % mod
print sum
