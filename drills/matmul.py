import numpy as np

def test(m1):
    print(len(m1[0]))


def matMul(X, Y):
    result = [[0, 0],
              [0, 0]]
    #iterate through columns of X
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
        # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    print(result)


m1 = ([[1, 2],
      [3, 4]])

m2 = ([[4, 5],
       [6, 7]])

matMul(m1, m2)
