N = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000};
def parse(s):
	last = None
	r = 0
	for i in s:
		if last != None:
			if N[i] > last:
				r += N[i] - last
			else:
				r += last
		last = N[i]
	return r

print(parse("XVIV"))
