import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)

num1 = input("Please input a complex number: ")
num1 = complex(num1)
real = num1.real
im = num1.imag
print("Polar form: {0} ".format(cart2pol(real, im)))
