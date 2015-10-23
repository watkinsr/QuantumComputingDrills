import numpy as np
import cmath

def complexNorm(c1):
    c2 = np.conjugate(c1)
    print(c1)
    print(c2)
    s1 = sum(sum(c2*c1))
    print(np.sqrt(s1))


c1 = np.array([(4+3j, 6-4j, 12-7j, 13j)])
complexNorm(c1)
