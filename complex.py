import math

#Modulus of complex numbers
def modulus (num1):
    real = complex(num1).real
    imag = complex(num1).imag
    modulus = real*real  + imag*imag
    return math.sqrt(modulus)

#Conjugate of complex number
def conjugate (num):
    print('Conjugate: {0}'.format(num.conjugate()))
    return 0


#Complex input
num1 = input('Enter first complex number: ')
num1 = complex(num1)
print(num1)
modNum1 = modulus(num1)
conjuNum1 = conjugate(num1)
print('Modulus of {0} is: {1}'.format(num1, modNum1))
num2 = input('Enter second complex number: ')
num2 = complex(num2)
print(num2)
modNum2 = modulus(num2)
conjuNum2 = conjugate(num2)
print('Modulus of {0} is: {1}'.format(num2, modNum2))

#Add two complex numbers
sum = complex(num1) + complex(num2)

#Multiple two complex numbers
product = complex(num1) * complex(num2)

#Divide two complex numbers
division = complex(num1) / complex(num2)

#Subtract two complex numbers
subtract = complex(num1) - complex(num2)


print('Producing respective answers for the two numbers...')
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The product of {0} and {1} is {2}'.format(num1, num2, product))
print('The division of {0} and {1} is {2}'.format(num1, num2, division))
