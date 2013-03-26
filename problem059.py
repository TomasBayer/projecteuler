from crypto import crackPolyAlph
from fget import fgetIntList
print(sum([ ord(n) for n in crackPolyAlph(list(fgetIntList("problem059")),list(range(0,256)),3,lambda x,y: chr(x^y)) ]))
