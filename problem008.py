from fget import fget
s = fget("problem008")
m = -1
while len(s) > 4:
	m = max(m,int(s[0])*int(s[1])*int(s[2])*int(s[3])*int(s[4]))
	s = s[1:]
print(m)
