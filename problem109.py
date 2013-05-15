max = 99

felder  = [ a*b for a in range(1,21) for b in range(1,4) ] + [25,50]
doubles = range(2,41,2) + [50]; 

checks = [ [0] * (max + 1) for _ in range(3) ]
for d in doubles:
    checks[0][d] = 1

for a in range(2):
    for n in range(1, max + 1):
        for c in felder:
            if c < n:
                checks[a+1][n] += checks[a][n-c]

schecks = [0] * (max + 1)
for d in doubles:
    for c in felder:
        c = d + 2*c
        if c <= max:
            schecks[c] += 1


c = 0
for a in range(1, max + 1):
    d = checks[0][a] + checks[1][a] + ( checks[2][a] + schecks[a] ) // 2
    c += d
print c
