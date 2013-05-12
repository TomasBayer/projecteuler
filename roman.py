N1 = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000};
N2 = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]];
def romToDec(s):
   last = None
   r = 0
   for i in s:
      if last != None:
         if N1[i] > last:
            r += N1[i] - last
            last = None
         else:
            r += last
            last = N1[i]
      else:
         last = N1[i]
   if last:
       r += last
   return r


def decToRom(n):
    s = ""
    for [d,c] in N2:
        a = n // d
        n -= a * d;
        s += c * a;
    return s
