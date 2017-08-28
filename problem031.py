# d[i][n] denotes the number of different ways k 
# can be made using any number of the coins in M[0:i+1] 
M = [1,2,5,10,20,50,100,200]
d = [ [1] + [0] * 200 for i in range(0,8) ]


for n in range(1,201):
	for i in range(0,8):
		d[i][n] = sum([d[k][n-M[k]] for k in range(0,i+1) if M[k] <= n])

print(d[7][200])
