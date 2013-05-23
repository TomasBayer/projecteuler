from zth import mpowmod, mmulmod
# Fall A: Starte 1, Ende 4, Erlaube:  Von beiden Punkten ist der erste Schritt je vertikal und der zweite nach rechts.
# Fall B: Starte 1, Ende 4, Verbiete: Erster Schritt von beiden Punkten ist vertikal.Von beiden Punkten ist der erste Schritt je vertikal und der zweite nach rechts.
# Fall C: Starte 1, Ende 2 (aequivalent: Starte 3, Ende 4)

# Abgeleitete Rekursionen:
# T(n, A) = T(n,   B) + T(n-2, A)
# T(n, B) = T(n-1, B) + 2 * T(n-1, C)
# T(n, C) = T(n-1, A) + T(n-1, C)

# Anfangswerte:
# T(1, A) = 1
# T(1, B) = 1
# T(1, C) = 0
# T(2, A) = 1

# T(n, C) = Summe von T(i, A) ueber i = 1,...,n-1 
# T(n, B) = 1 + 2 * ( Summe von T(i, C) ueber i = 1,...,n-1 )

# =>
# T(n, B) = 1 + 2 * ( Summe von (Summe von T(j, A) ueber j = 1,...,i) ueber i = 1,...,n-2 )
# T(n, B) = 1 + 2 * ( Summe von (n - 1 - i) * T(i, A) ueber i = 1,...,n-2 )

# T(n, A) = T(n, B) + T(n-2, A)
# => 
# T(n, A) = 1 + 2 * ( Summe von (n - 1 - i) * T(i, A) ueber i = 1,...,n-2 ) + T(n-2, A)

n = 10**12
m = 10**8

print mmulmod([[1, 1, 1, 1]], mpowmod([[0, 0, 1, 1], [1, 1, 0, 0], [2, 2, 1, 0], [1, 0, 0, 0]], n-2, m), m)[0][0]
