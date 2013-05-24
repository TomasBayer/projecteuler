from fget import fgetLines

## Import
sudokus = []
for line in fgetLines("problem096"):
    if line[:4] == "Grid":
        if line[5:7] != "01":
            sudokus.append(S)
        S = []
    else:
        S.append([ int(c) for c in line.rstrip() ])
sudokus.append(S)

def sprint(S):
    s = ""
    for i in range(9):
        for j in range(9):
            s += str(S[i][j])
        s += "\n"
    print s

## Loesungsmethoden
def checkField(S,a,b):
    if S[a][b] != 0:
        return
    map = [0] * 10
    for i in range(9):
        map[S[a][i]] = 1
        map[S[i][b]] = 1
        map[S[3*(a//3)+i//3][3*(b//3)+i%3]] = 1
    R = filter(lambda x: map[x] == 0, range(1,10))
    if len(R) == 1:
        S[a][b] = R[0]

## Starte
for S in sudokus:
    for a in range(9):
        for b in range(9):
            checkField(S,a,b)
    sprint(S)


    break
