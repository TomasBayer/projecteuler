from fget import fgetLines

## Kartenblatt analysieren
def isStraight(B):
	for i in range(0,4):
		if B[i] == B[i+1]:
			return False
	return B[0]-B[4] == 4

td = { 9: 7, 8: 6, 7: 3, 6: 2, 5: 1, 3: 0 }
def tupel(B):
	T = []
	l, m = B[0], 1
	for i in range(1,6):
		if i < 5 and B[i] == l:
			m += 1
		else:
			T.append((l,m))
			l, m = B[i], 1
	T = sorted(T,key=lambda x: x[1], reverse=True)
	return [td[2 * T[0][1] + T[1][1]]] + [k[0] for k in T]

## Wert des Kartenblattes:
def value(B):
	S = isStraight(B)
	if S and B[5]:
		if S[0][0] == 8:
			return [9]
		return [8, B[0]]
	T = tupel(B)
	if T[0] >= 6:
		return T
	if B[5]:
		return [5] + B[:5]
	if S:
		return [4, B[0]]
	return T

def cmp(A,B):
	A = value(A)
	B = value(B)
	for i in range(0,len(A)):
		if A[i] == B[i]:
			continue
		if A[i] > B[i]:
			return 1
		else:
			return -1
	return 0
	

# Parser für String -> Kartenblatt
d1 = { '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12 }
def parse(s):
	L = []
	C = set([])
	for i in s.split(' '):
		L.append(d1[i[0]])
		C.add(i[1])
	return sorted(L,reverse=True) + [len(C) == 1]

# Parser für Partien
def partien():
	for s in fgetLines("problem054"):
		yield (parse(s[:14]),parse(s[15:]))

# Eigentliches Programm
s = 0
for (A,B) in partien():
	if cmp(A,B) == 1:
		s += 1
print(s)
