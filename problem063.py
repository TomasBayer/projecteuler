from math import log, floor
print(sum([floor(1/(1-log(a,10))) for a in range(1,10)]))
