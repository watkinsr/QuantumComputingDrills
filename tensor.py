import numpy as np

def constructTensor(m1, m2):
    # Get tensor by multiplying each element in m1 by all of m2
    rows = len(m1[0]) * 2
    columns = len(m1) * 2
    t1 = [[x for x in range(columns)] for y in range(rows)]
    x = 0
    y = 0
    # loop through cAmount, loop through cAmount for first line
    for n in range(len(m1)):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                for k in range(len(m1[0])):
                    t1[x][y] = m1[n][j] * m2[i][k]
                    y = y + 1
                    if y == columns:
                        y = 0
                        x = x + 1


    print(m1)
    print(m2)
    print(t1)



m1 = ([[1, 2],
       [3, 4]])
m2 = ([[2, 3],
       [4, 5]])
constructTensor(m1, m2)
