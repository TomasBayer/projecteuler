from fget import fgetStringList
L = sorted(fgetStringList("problem22"))

print(sum([(i + 1) * sum([ord(c) - 64 for c in L[i]]) for i in range(0,len(L))])) 
