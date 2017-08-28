from math import sqrt
def letterFreq(s = "en"):
	if s == "en":
		return [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015,
			6.094, 6.966, 0.153, 0.772,  4.025, 2.406, 6.749,
			7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
			2.758, 0.978, 2.360, 0.150, 1.974, 0.074] 

def getLetterFreq(t):
	L = [0] * 26
	for i in t:
		i = ord(i)
		if 65 <= i <= 90:
			L[i-65] += 1
		elif 97 <= i <= 122:
			L[i-97] += 1
		elif i < 32:
			s += 1
	m = len(t)	
	if m:
		return [100*i/m for i in L]
	else:
		return L

def languageCheck(t,s = "en"):
	O = letterFreq(s)
	M = getLetterFreq(t)
	return sqrt(sum([ (O[i]-M[i])**2 for i in range(0,26) ])) 

def hatSteuerzeichen(t):
	for i in t:
		if ord(i) < 32:
			return True
	return False

# f: decryption function
# K: list of possible keys
# l: estimated keylength
def crackPolyAlph(t,K,l,f,s = "en"): 
	R = [ [] for i in range(0,l) ]
	k = 0
	for c in t:
		R[k].append(c)
		k = (k+1)%l
	for k in range(0,l):
		m = (1000,"")
		for i in K:
			H = ''.join([f(d,i) for d in R[k]])
			if hatSteuerzeichen(H):
				continue
			m = min(m, (languageCheck(H,s),H),key=lambda x: x[0])
		R[k] = m[1]
	s = ""
	for i in range(0,len(R[0])):
		for k in range(0,l):
			if i >= len(R[k]):
				break
			s += R[k][i]	
	return s

def crackMonoAlph(t,K,f,s = "en"):
	return crackPolyAlph(t,K,1,f,s)
