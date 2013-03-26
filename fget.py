import re
def fgetLines(filename):
	with open(filename + ".input",'r') as f:
		for l in f:
			yield l.rstrip()

def fget(filename):
	return '\n'.join(list(fgetLines(filename)))

def fgetInt(filename):
	return int(fget(filename))

def fgetIntList(filename):
	for l in fgetLines(filename):
		for i in re.finditer('([0-9]+)', l):
			yield int(i.group(1))

def fgetIntMat(filename):
	t = []
	for l in fgetLines(filename):
		n = []
		for d in re.split('[^0-9]',l.rstrip()):
			n.append(int(d))
		t.append(n)
	return t

def fgetStringList(filename):
	for l in fgetLines(filename):
		for k in l.split(','):
			yield k[1:-1]
