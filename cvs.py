# Complex vector space example

def complexVectSpaceScalarMultiplication(scalar, vect):
    arr = []
    for e in vect:
        ele = scalar * e
        arr.append(ele)
    return arr


def cvsAddition(vect1, vect2):
    arr = []
    for i,j in zip(vect1, vect2):
        e = i + j
        arr.append(e)
    print("Addition answer: {0}".format(arr))


from functools import partial
scalar = complex(input("Please input a complex scalar: "))
print("Scalar: {0}".format(scalar))

vect1 = [6+3j, 0+0j, 5+1j, 4]
vect2 = [6-4j, 7+3j, 4.2-8.1j, -3j]
vect3 = [16+2.3j, -7j, 6, -4j]

print("Vect1: {0}".format(vect1))

print("Multiplication Answer: {0}".format(complexVectSpaceScalarMultiplication(scalar, vect1)))
print(cvsAddition(vect2, vect3))
