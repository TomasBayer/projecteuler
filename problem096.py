from fget import fgetLines
from collections import deque

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

######################

class Sudoku:
    def __init__(self, S):
        self.__grid = S
        self.__poss = [ [ [False] + [True] * 9 for _ in range(9) ] for _ in range(9) ]
        self.__queue = deque([])
        for a in range(9):
            for b in range(9):
                for (i,j) in self.neighbours(a,b):
                    self.__poss[a][b][S[i][j]] = False
                if S[a][b] == 0:
                    self.__queue.append((0,a,b));
    def neighbours(self, a, b):
        for i in range(9):
            yield (a,i)
            yield (i,b)
            yield (3*(a//3)+i//3, 3*(b//3)+i%3)
    def solve(self):
        self.process_queue();
    def process_queue(self):
        while self.__queue:
            T = self.__queue.popleft();
            print T
            if T[0] == 0:
                poss = filter(lambda x: self.__poss[T[1]][T[2]][x], range(1,10))
                if len(poss) == 1:
                    self.put(T[1], T[2], poss[0])
    def put(self, a, b, v):
        self.__grid[a][b] = v
        for (i,j) in self.neighbours(a,b):
            self.__poss[i][j][v] = False
            self.__queue.append((0,i,j))
        
    def p(self):
        s = ""
        for i in range(9):
            for j in range(9):
                if self.__grid[i][j]:
                    s += str(self.__grid[i][j])
                else:
                    s += "."
                if j % 3 == 2 and j != 8:
                    s += "|"
            s += "\n"
            if i % 3 == 2 and i != 8:
                s += "-" * 11 + "\n"
        print s

######################

s = Sudoku(sudokus[0])

s.solve()
s.p()
