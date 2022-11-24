from solveFun import np


def ansFun2(xArr, E, P, p, g, L):
    A = 0.0341
    Cx = E * A
    fx = p * g * A
    # return -0.0000328408 * xArr + 3.51525 * 1e-7 * np.power(xArr, 2)
    return fx / Cx * np.power(xArr, 2) / 2 + (-P / Cx - (fx / Cx * L)) * xArr


def infNorma(Yans, Yorig):
    absmax = np.max(np.abs(Yans - Yorig))
    infmax = absmax / np.max(np.abs(Yorig))
    return infmax, absmax


def l2Norm(Yans, Yorig):
    sum = np.sum(np.power(Yans - Yorig, 2))
    ans = np.power(sum / np.sum(np.power(Yorig, 2)), 1 / 2)
    return ans
