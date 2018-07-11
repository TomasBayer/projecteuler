N = 20
C = [0,0,0] + [None] * (N-2)
def c(n):
    if n < 3:
        return 0
    else:
        h = C[n-1]
        #print n
        for i in xrange(1, n//3+1):
            #print n,h,i, n-3*i + 1
            h += n - 3*i + 1
        # Crazies:
        for k in xrange(6,n+1,6):
            h += n - k + 1
        C[n] = h
        return h

for n in xrange(3,N+1):
    a = c(n)
    print n, c(n)
