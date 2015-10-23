import numpy as np

def complexDistance(v1, v2):
    v3 = v1 - v2
    print(v3)
    print(np.sqrt(np.conjugate(v3)*v3))


v1 = np.array([(1+2j, 3-4j)])
v2 = np.array([(1+0j, 3+1j)])
complexDistance(v1, v2)
