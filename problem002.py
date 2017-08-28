fib = [1,2]
while fib[-1] <= 4000000:
	fib.append(fib[-1]+fib[-2])
sum = 0
for i in fib:
	if i % 2 == 0:
		sum += i	

print(sum)
