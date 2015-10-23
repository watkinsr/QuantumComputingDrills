import numpy as np
def checkUnitary(m1):
    #U (inner product) U(hermitian conjugate) => Identity matrix
    m2 = np.transpose(m1)
    m3 = m1 * np.conjugate(m2)
    for i in range(len(m1)):
    # iterate through columns of Y
        for j in range(len(m1[0])):
            if i != j and m3[i][j] != 0:
                return 0
            elif i == j and m3[i][j] != 1:
                return 0

    return 1


m1 = ([[1, 0],
       [0, -1]])

isUnitary = checkUnitary(m1)
print(m1)
if isUnitary == 1:
    print('found unitary matrix')
else:
    print('couldnt find unitary matrix')
