from __future__ import division
from tools import tupel

peteDices = 9
colinDices = 6

peteMax = peteDices * 4 + 1
colinMax = colinDices * 6 + 1

pete = [0] * peteMax
for T in tupel([1,2,3,4], peteDices):
    pete[sum(T)] += 1

colin = [0] * colinMax
for T in tupel([1,2,3,4,5,6], colinDices):
    colin[sum(T)] += 1

# colinProb[i] = Probability of Pete winning, if Pete has a total of i
csum = sum(colin)
colinProb = [0] * colinMax
for i in range(colinMax):
    for j in range(i+1, colinMax):
        colinProb[j] += colin[i]
colinProb = map(lambda x: x / csum, colinProb)

s = 0
for i in range(peteMax):
    s += pete[i] * colinProb[i] 
print round(s / sum(pete), 7)
