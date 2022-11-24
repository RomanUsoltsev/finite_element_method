import solveFun as sf
from solveFun import np

import complFun as cf

import time
import pandas as pd
import matplotlib.pyplot as plt

def main():
    E = 30 * 1e9
    P = 30000
    L = 5
    b = 0.1
    p = 2150
    g = 9.81
    x0 = 0

    Ni = [2, 4, 8, 16, 32, 64, 128]
    arrAns = np.zeros(shape=[len(Ni), 7])

    i = 0
    for N in Ni:
        start_time = time.time()

        uVector, stiffnessMatrix = sf.finiteElementMethod(P, p, g, E, b, x0, L, N)

        times = time.time() - start_time

        Q = 10000

        xVector = np.linspace(x0, L, Q)
        yArrAns = sf.ksiFun(xVector, uVector, x0, L)
        yOrig = cf.ansFun2(xVector, E, P, p, g, L)

        infmax, absmax = cf.infNorma(yArrAns, yOrig)

        Erl = cf.l2Norm(yArrAns, yOrig)

        arrAns[i][0] = N
        arrAns[i][1] = infmax
        arrAns[i][3] = Erl
        arrAns[i][5] = np.linalg.cond(stiffnessMatrix)
        arrAns[i][6] = times

        if (i != 0):
            R1 = np.log2(arrAns[i - 1][1] / infmax)
            R2 = np.log2(arrAns[i - 1][3] / Erl)
            arrAns[i][2] = R1
            arrAns[i][4] = R2

        i += 1

        plt.figure(figsize=(15, 10))
        plt.xlabel("X", fontsize=14)
        plt.ylabel("Y", fontsize=14)
        plt.rcParams['font.size'] = '14'
        plt.plot(xVector, yOrig, label="exact solution", color='red')
        plt.scatter(xVector, yArrAns, marker='^', label="approximate solution for N = " + str(N))
        plt.legend()
        plt.grid(True)
        plt.show()
    return arrAns


if __name__ == "__main__":
    arrAns = main()
    arrAnspd = pd.DataFrame(arrAns, columns=["N", "Er", "R", "El", "R", "cond(K)", "time, s"])
    print(arrAnspd)