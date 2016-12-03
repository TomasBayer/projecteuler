from fget import fgetLines

mat = []
for l in fgetLines("problem107"):
    mat.append(l.split(","))






s = "16  12  21  -   -   -\
16  -   -   17  20  -   -\
12  -   -   28  -   31  -\
21  17  28  -   18  19  23\
-   20  -   18  -   -   11\
-   -   31  19  -   -   27\
-   -   -   23  11  27  -"



M = len(mat)

edges = []
for i in range(M):
    for j in range(M):
        if mat[i][j] != "-":
            edges.append((int(mat[i][j]), i, j))

edges.sort(key=lambda a: a[0])

vertices = [0] * M

c = 0
for (v,i,j) in edges:
    if vertices[i] and vertices[j]:
        continue
    print (v,i,j)
    c += v
    vertices[i] = vertices[j] = 1
print c
