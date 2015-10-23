import numpy as np

a = np.array([(1,2,3)])
a = a.transpose()
b = np.array([(4, 5, 6)])

def innerProduct(v1, v2):
    # Transpose first vector and multiply it against the second
    print(v1 * v2)


innerProduct(a, b)
