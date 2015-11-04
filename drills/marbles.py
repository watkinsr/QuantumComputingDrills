import numpy as np

def startMarbleSystem(bMatrix, tAmount, sState):
    print('Beginning marble system...')
    print('Starting state: ' + str(sState) + ', tClicks: ' + str(tAmount))
    state = sState
    for i in range(tAmount):
        state = np.dot(bMatrix, state)

    print('End state: ' + str(state))


def getStartingState(mAmount):
    sState = [mAmount]
    for i in range(mAmount):
        sState[i] = int(input('Input amount of marbles assigned to vertex[' + str(i) + ']'))


    print('Obtained starting state: ' + str(sState))


def getTimeClickAmount():
    print('enter time click amount')


def begin():
    # getBooleanMatrix()
    mAmount = 6
    bMatrix = [[0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,1,0,0,0,1],
               [0,0,0,1,0,0],
               [0,0,1,0,0,0],
               [1,0,0,0,1,0]]
    # getStartingState(mAmount)
    sState = [6, 2, 1, 5, 3, 10]
    tAmount = 6
    startMarbleSystem(bMatrix, tAmount, sState)


def getBooleanMatrix():
    # Get boolean matrix from user
    mAmount = int(input('Enter marble amount:'))
    print (mAmount)
    bMatrix = [[x for x in range(mAmount)] for y in range(mAmount)]

    for i in range(mAmount):
        for j in range(mAmount):
            try:
                bMatrix[i][j] = (int)(input('Enter value for [' + str(i) + ']['+ str(j) + ']: '))
            except:
                bMatrix[i][j] = (int)(input('Enter value for [' + str(i) + ']['+ str(j) + ']: '))

    print('Obtained boolean matrix...' + str(bMatrix))


begin()
