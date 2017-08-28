from zth import factorization, zahlen
S = [0,0,0,0]
for n in zahlen(2):
	S.pop(0)
	S.append(len(list(factorization(n))))
	if S[0] == S[1] == S[2] == S[3] == 4:
		print(n-3)
		break
