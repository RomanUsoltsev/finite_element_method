import numpy as np


def globalStiffnessMatrix(E, b, x0, L, N):
    A = 0.0341
    gMatrix = np.zeros(shape=[N, N])
    EI = E * A
    h = abs(L - x0) / (N - 1)

    for i in range(gMatrix.shape[0] - 1):
        buffMatrix = np.zeros(shape=[N, N])
        buffMatrix[i:i + 2, i: i + 2] = [[1, -1], [-1, 1]]
        gMatrix += buffMatrix

    gMatrix[0][1] = 0
    gMatrix[1][0] = 0

    gMatrix = gMatrix * (EI / h)

    return gMatrix


def loadVector(P, p, g, E, b, x0, L, N):
    A = 0.0341
    pMatrix = np.zeros(shape=[N, N])
    fVector = np.zeros(shape=[N, 1])

    h = abs(L) / (N - 1)

    for i in range(pMatrix.shape[0] - 1):
        buffMatrix = np.zeros(shape=[N, N])
        buffMatrix[i:i + 2, i: i + 2] = [[2, 1], [1, 2]]
        pMatrix += buffMatrix
        fVector[i] = p * g * A

    fVector[N - 1] = p * g * A

    pMatrix[0] = np.zeros(shape=N)

    pMatrix = pMatrix * -h / 6

    return pMatrix.dot(fVector)


def finiteElementMethod(P, p, g, E, b, x0, L, N):
    stiffnessMatrix = globalStiffnessMatrix(E, b, x0, L, N)
    loadV = loadVector(P, p, g, E, b, x0, L, N)

    loadV[N - 1] += (-P)
    uVector = (np.linalg.inv(stiffnessMatrix)).dot(loadV)

    return uVector, stiffnessMatrix


def ksiFun(xArr, yCoeffArr, x0, L):
    xVector = np.linspace(x0, L, yCoeffArr.shape[0])
    arrAns = np.zeros(shape=xArr.shape)

    for index, i in enumerate(xArr):
        j = 1
        while (i > xVector[j]):
            j += 1

        b = - (xVector[j] * yCoeffArr[j - 1] - xVector[j - 1] * yCoeffArr[j]) / (xVector[j - 1] - xVector[j])
        k = -(-yCoeffArr[j - 1] + yCoeffArr[j]) / (xVector[j - 1] - xVector[j])
        arrAns[index] = k * i + b

    return arrAns
