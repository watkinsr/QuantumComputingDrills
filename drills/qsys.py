# Write a program that simulates the first quantum system
# described in this section (4.1) The user should be able to specify
# how many points the particle can occupy. The user will specify a
# key state vector by assigning it's amplitudes. The program, when asked
# the likelihood of finding the particle at a given point, will perform
# the calculations described in example 4.1.1. If the user enters two kets,
# the system will calculate the probability of transitioning from the first
# key to the second, after an observation has been made.

# Therefore we have a ket vector that represents the state

import math
import copy
import numpy as np


def start():
    sKet, eKet = getKetStates()
    print('Starting state ket: ' + str(sKet))
    print('End state ket: ' + str(eKet))
    while(0 == 0):
        getLikelihood(sKet, eKet)


def getKet():
    sKetSize = int(input('Please enter state ket size: '))
    print('Ket size set to: ' + str(sKetSize))
    sKet = [0] * sKetSize
    for i in range(sKetSize):
        sKet[i] = complex(input('Enter val[' + str(i) + '] for state ket:'))
        print('sKet[' + str(i) + '] assigned to: ' + str(sKet[i]))

    print('Initialized ket: ' + str(sKet))
    return sKet


def getKetStates():
    sKet = getKet()
    print('Initialized starting state of quantum system: ' + str(sKet))
    if (input('Would you like to specify an end state? [y] or [n]') == 'y'):
        eKet = getKet()
        getTransitionLikelihood(sKet, eKet)
    else:
        print('Lets move on then...')
        eKet = 0

    return (sKet, eKet)


def getTransitionLikelihood(sKet, eKet):
    print('Getting transition amp for: ' + str(sKet) + ' to: ' + str(eKet))
    sNorm = copy.deepcopy(sKet)
    eNorm = copy.deepcopy(eKet)
    eNorm = np.conjugate(eNorm)
    for i in range(len(sKet)):
        sNorm[i] = 1/math.sqrt(2) * sNorm[i]
        eNorm[i] = 1/math.sqrt(2) * eNorm[i]
    pVect = eNorm * sNorm
    p = 0
    for i in range(len(pVect)):
        p = p + pVect[i]
    print('Found transition likelihood: ' + str(p))
    return p


def getLikelihood(sKet, eKet):
    pVal = int(input('Point for likelihood:(0-' + str(len(sKet) - 1) + '): '))
    print('You chose likelihood val: ' + str(pVal))
    print('Getting norm...')
    norm = getKetNorm(sKet)
    print('Found norm: ' + str(norm))
    print('Getting likelihood...')
    pOfX = abs(sKet[pVal])**2 / norm**2
    print('Found likelihood: ' + str(pOfX))


def getKetNorm(sKet):
    x = 0
    for i in range(len(sKet)):
        x = x + abs(sKet[i]) * abs(sKet[i])
        if (i == len(sKet) - 1):
            return math.sqrt(x)


start()
