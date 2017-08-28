from zth import isTriagonal
from fget import fgetStringList

print(len([1 for s in fgetStringList("problem042") if isTriangonal(sum([ord(i) - 64 for i in s]))]))
