m = 50

c = 0
for x1 in range(0,m+1):
    for y1 in range(0,m+1):
        for x2 in range(0,m+1):
            for y2 in range(0,y1-x1+x2):
                if (x1 != 0 or y1 != 0) and (x2 != 0 or y2 != 0) and (x1 == y2 == 0 or x1*(x1-x2)+y1*(y1-y2) == 0 or x2*(x1-x2)+y2*(y1-y2) == 0):
                    c += 1
print c
