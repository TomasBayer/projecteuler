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

## Lösungsmethoden



## Starte
for S in sudokus:
	print(S)


	break
