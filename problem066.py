from zth import continuedFractionOfRoot, continuedFractions, generatorFromPeriod, isRoot
def minPellSolutionX(D):
	(L,F) = continuedFractionOfRoot(D)
	t = len(F)
	if t % 2:
		t *= 2
	k = 0
	for (z,n) in continuedFractions(generatorFromPeriod(L,F)):
		k += 1
		if k == t:
			return z

print(max([i for i in range(2,1001) if not isRoot(i,2)],key=lambda i:minPellSolutionX(i)))
