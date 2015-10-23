import numpy as np

def checkHermitian(m1):
    # check transposed elements to see if complex conjugate is the same
    #iterate through columns of X
    for i in range(len(m1)):
    # iterate through columns of Y
        for j in range(len(m1[0])):
        # iterate through rows of Y
            if i != j:
                if m1[i][j] != np.conjugate(m1[j][i]):
                    return 0


    return 1



m1 = ([[4, 3-4j],
      [3-4j, 5]])

found = checkHermitian(m1)
if found == 0:
    print('Not hermitian')
else :
    print('Hermitian matrix found')
