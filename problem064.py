from zth import continuedFractionOfRoot
print(len([i for i in range(1,10001) if len(continuedFractionOfRoot(i)[1]) % 2]))
