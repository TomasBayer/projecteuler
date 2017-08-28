sum = 0
k = 100
for i in range(1,k+1):
	sum += i * ( k * (k+1) // 2 - i)
print(sum)
