def day(d,m,j):
	M = [0,3,3,6,1,4,6,2,5,0,3,5]
	r = d + M[m-1] + j % 100 + (j % 100) // 4 + ( 3 - ( (j // 100) % 4) ) * 2
	if j % 4 == 0 and (j % 100 != 0 or j % 400 == 0) and m < 3:
		r -= 1
	return r % 7

def isPandiagonal(s):
	return len(set(s)) == len(s) and "0" not in s
