from math import log
from fget import fgetIntMat

#    a^b < c^d <=> b < d * log_a(c)

def cmp(a,b):
    (c1,c2) = (a[0]>b[0], a[1]>b[1])
    if c1 == c2:
        return c1
    if (c1 and a[1] == b[1]) or (c2 and a[0] == b[0]):
        return True
    return log(b[0]) * b[1] > a[1] * log(a[0])

list = fgetIntMat("problem099")
max = 0
for i in range(1,len(list)):
    if cmp(list[max], list[i]):
        max = i
print max + 1
