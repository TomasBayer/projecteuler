from roman import decToRom, romToDec
from fget import fgetLines

print sum(map(lambda s: len(s) - len(decToRom(romToDec(s))), fgetLines("problem089")))
