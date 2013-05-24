from fget import fgetLines
from sudoku import Sudoku

## Import
sudokus = []
S = None
for line in fgetLines("problem096"):
    if line[:4] == "Grid":
        if S != None:
            sudokus.append(S)
        S = []
    else:
        S.append([ int(c) for c in line.rstrip() ])
sudokus.append(S)

r = 0
for S in sudokus:
    s = Sudoku(S)
    s.solve()
    grid = s.grid()
    r += sum(10**i * grid[0][2-i] for i in range(3))
print r
