from zth import fibonacci
k = 0
for i in fibonacci():
	k += 1
	if len(str(i)) > 1000:
		print(k)
		break
