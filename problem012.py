from zth import anzahlTeiler, polygonalZahlen
for i in polygonalZahlen(3):
	if anzahlTeiler(i) > 500:
		print(i)
		break
