from zth import polygonalZahlen, isPentagonal
for n in polygonalZahlen(6):
	if isPentagonal(n):
		if n > 40755:
			print(n)
			break
