from random import randint, shuffle

def throwDice():
	return (randint(1,4),randint(1,4))

P = 0
cD = 0
C = [0] * 40
CP = [ [0,10] + [None] * 14 for i in range(0,3) ] + [ [0,10,11,24,39,5,"R","R","U","B"] + [None] * 6 for i in range(0,3) ]
for i in range(0,6):
	shuffle(CP[i])

def move():
	global P, cD, CP, C
	def moveTo(n):
		global P
		P = n%40
		p = None
		if P == 2:
			p = 0
		elif P == 7:
			p = 3
		elif P == 17:
			p = 1
		elif P == 22:
			p = 4
		elif P == 30:
			moveTo(10)
			return
		elif P == 33:
			p = 2
		elif P == 36:
			p = 5
		if p != None:
			s = CP[p].pop(0)
			CP[p].append(s)
			if s != None:
				if s == "R":
					moveTo((P+5)//10*10+5)
					return
				elif s == "U":
					if 12 < P < 28:
						moveTo(28)
					else:
						moveTo(12)
					return
				elif s == "B":
					moveTo(P-3)
					return
				else:
					moveTo(s)
					return		
		C[P] += 1
	(d1,d2) = throwDice()
	if d1 == d2:
		cD += 1
		if cD == 3:
			moveTo(10)			
			cD = 0
			return
	else:
		cD = 0
	moveTo(P+d1+d2)


for i in range(0,499999):
	move()

C = sorted([ (i,C[i]) for i in range(0,40) ],key=lambda x: x[1],reverse=True)
print(C[0][0],C[1][0],C[2][0])
