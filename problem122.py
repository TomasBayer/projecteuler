from zth import factorize

def count(b):
    if b == 1:
        return 0
    if b % 2:
        return count(b-1) + 1
    else:
        return count(b// 2) + 1

def minpow(y):
    return sum(map(lambda x: count(x), factorize(y)))
    
print sum(map(lambda i: min(minpow(i), count(i)), range(1,201)))
