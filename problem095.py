from time import clock

max = 10**6

divisor = [None] * (max + 1)

for p in range(2,max + 1):
    if divisor[p]:
        continue
    q = p
    n = 1
    while q <= max:
        if not divisor[q]:
            k = 1
            m = n
            power = p
            sum = p + 1
            while True:
                (d,r) = divmod(m,p)
                if r == 0:
                    m = d
                    k += 1
                    power *= p
                    sum += power
                else:
                    break
            divisor[q] = (sum,m)
        q += p
        n += 1

divsum = [None] * (max+1)

def calcdivsum(n):
    a = divsum[n]
    if a:
        return a
    else:
        if n == 1:
            a = 1
        else:
            (e,m) = divisor[n]
            a = e * calcdivsum(m)
        divsum[n] = a
        return a
   
for i in range(2,max+1):
    calcdivsum(i)
for i in range(1,max+1):
    divsum[i] -= i

def calcchain(chain):
    next = divsum[chain[-1]]
    if next > max or next == 1:
        return None
    elif next in chain:
        if chain[0] == next:
            return len(chain)
        else:
            return None
    else:
        return calcchain(chain + [next])

ret = (0, None)
for i in range(2,max):
    c = calcchain([i])
    if c != None and c > ret[0]:
        ret = (c, i)

print ret
