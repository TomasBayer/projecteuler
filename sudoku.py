from collections import deque
from copy import deepcopy

class Sudoku:
    def __init__(self, S):
        self.__grid = S
        self.__poss = [ [ [False] + [True] * 9 for _ in range(9) ] for _ in range(9) ]
        self.__queue = deque([])
        for a in range(9):
            for b in range(9):
                for (i,j) in self.getNeighbours(a,b):
                    self.__poss[a][b][S[i][j]] = False
        self.__solvable = True

    def getRow(self, a):
        for b in range(9):
            yield (a,b)

    def getColumn(self, b):
        for a in range(9):
            yield (a,b)

    def getBlock(self, n):
        a1 = 3 * (n // 3)
        b1 = 3 * (n % 3)
        for a in range(a1,a1+3):
            for b in range(b1,b1+3):
                yield (a,b)

    def getBlockOfField(self, a, b):
        return 3 * (a // 3) + (b // 3)

    def getNeighbours(self, a, b):
        M = [(a,b)]
        for T in self.getRow(a):
            if T in M:
                continue
            M.append(T)
            yield T
        for T in self.getColumn(b):
            if T in M:
                continue
            M.append(T)
            yield T
        for T in self.getBlock(self.getBlockOfField(a,b)):
            if T in M:
                continue
            M.append(T)
            yield T

    def getEmptyNeighbours(self,a,b):
        for P in self.getNeighbours(a,b):
            if self.isEmpty(P):
                yield P

    def fullCheck_SingleCandidate(self):
        for a in range(9):
            for b in range(9):
                if self.isEmpty(a,b):
                    self.__queue.append((0,a,b));

    def fullCheck_SinglePosition(self):
        for i in range(9):
            self.__queue.append((1,0,i));
            self.__queue.append((1,1,i));
            self.__queue.append((1,2,i));

    def solve(self):
        self.fullCheck_SingleCandidate()
        self.fullCheck_SinglePosition()
        self.__solve()


    def __solve(self):
        self.process_queue()
        if not self.__solvable:
            return False
        P = self.getEmptyField()
        if P == None:
            return True
        V = self.getCandidates(P[0],P[1])
        for a in V:
            S = deepcopy(self) 
            S.put(P[0],P[1], a)
            if S.__solve():
                self.__grid = S.__grid
                return True
        return False

    def getEmptyField(self):
        for i in range(9):
            for j in range(9):
                if self.__grid[i][j] == 0:
                    return (i,j)
        return None

    def solved(self):
        return self.getEmptyField() == None

    def getCandidates(self, a, b):
        return filter(lambda x: self.__poss[a][b][x], range(1,10))

    def process_queue(self):
        while self.__queue:
            T = self.__queue.popleft();
            # Single Candidate Check
            if T[0] == 0:
                poss = self.getCandidates(T[1], T[2])
                if len(poss) == 1:
                    self.put(T[1], T[2], poss[0])
                elif len(poss) == 0:
                    self.__solvable = False
                    break
            # Single Position Check
            if T[0] == 1:
                # Rows
                if T[1] == 0:
                    PP = [P for P in self.getRow(T[2])]
                elif T[1] == 1:
                    PP = [P for P in self.getColumn(T[2])]
                elif T[1] == 2:
                    PP = [P for P in self.getBlock(T[2])]
                L = [ self.get(P) for P in PP ]
                for i in range(1,10):
                    if i in L:
                        continue
                    H = filter(lambda P: self.isEmpty(P) and self.isPossibleValue(i,P), PP)
                    if len(H) == 1:
                        self.put(H[0][0],H[0][1],i)
                    elif len(H) == 0:
                        self.__solvable = False
                        break

    def get(self, a, b=None):
        if b == None:
            return self.__grid[a[0]][a[1]]
        else:
            return self.__grid[a][b]

    def isEmpty(self, a, b=None):
        return self.get(a,b) == 0

    def isPossibleValue(self, v, a, b=None):
        if b == None:
            return self.__poss[a[0]][a[1]][v]
        else:
            return self.__poss[a][b][v]

    def put(self, a, b, v):
        self.__grid[a][b] = v
        for (i,j) in self.getEmptyNeighbours(a,b):
            self.__poss[i][j][v] = False
            self.__queue.append((0,i,j))
            self.__queue.append((1,0,i))
            self.__queue.append((1,1,j))
            self.__queue.append((1,2,self.getBlockOfField(i,j)))

    def __str__(self):
        s = ""
        for i in range(9):
            for j in range(9):
                if self.isEmpty(i,j):
                    s += "."
                else:
                    s += str(self.get(i,j))
                if j % 3 == 2 and j != 8:
                    s += "|"
            s += "\n"
            if i % 3 == 2 and i != 8:
                s += "-" * 11 + "\n"
        return s

    def grid(self):
        return self.__grid

    def checkIntegrity(self):
        for i in range(9):
            A = [self.getRow(i), self.getColumn(i), self.getBlock(i)]
            for gen in A:
                m = [0] * 10
                for P in gen:
                    m[self.get(P)] += 1
                if filter(lambda x: m[x] > 1, range(1,10)):
                    return False
        return True
