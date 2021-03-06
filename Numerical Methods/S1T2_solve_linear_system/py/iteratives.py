import numpy as np
import numpy.linalg as la


def transform(A, b):
    """
    Преобразуем систему: Ax = b -> x = Cx+d
    """
    C = A.copy()
    d = b.copy()
    for i in range(len(C)):
        d[i] /= C[i, i]
        C[i, :] /= -C[i, i]
        C[i, i] = 0
    return C, d


def richardson(A, b, tol, max_iter=100):
    """
    Метод Ричардсона, tau_k = ||A||
    returns: list of x, list of y
    """
    tau = la.norm(A)

    xs = []
    ys = []
    x = b / tau

    while len(xs) < max_iter:
        xs.append(x)
        err = la.norm(A @ x - b)
        ys.append(err)

        if err <= tol:
            break

        x = x - (A @ x - b)/tau

    return xs, ys


def jacobi(A, b, tol, max_iter=100):
    """
    Метод Якоби
    returns: list of x, list of y
    """
    raise NotImplementedError
    return xs, ys


def seidel(A, b, tol, max_iter=100):
    """
    Метод Гаусса-Зейделя
    returns: list of x, list of y
    """
    raise NotImplementedError
    return xs, ys
