d = { 0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7, 1000: 8 }

def nlen(n):
	if n <= 20:
		return d[n]
	elif n < 100:
		return d[n // 10 * 10] + nlen(n % 10)
	elif n < 1000:
		if n % 100:
			return nlen(n//100) + d[100] + 3 + nlen(n % 100)
		else:
			return nlen(n//100) + d[100]
	elif n < 1000000:
		return nlen(n // 1000) + d[1000] + nlen( n % 1000) 

print(sum([nlen(i) for i in range(1,1001)]))
