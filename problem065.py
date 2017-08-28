from zth import continuedFractions, arithmFolge, quersumme

def ecf():
	yield 2
	for i in arithmFolge(2,2):
		yield 1
		yield i
		yield 1

k = 0
for i in continuedFractions(ecf()):
	k += 1
	if k == 100:
		print(quersumme(i[0]))	
		break
