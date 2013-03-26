from zth import numberOfIntegerPartitions

n = 0
for i in numberOfIntegerPartitions():
	if i % 1000000 == 0:
		print(n)
		break
	n += 1
