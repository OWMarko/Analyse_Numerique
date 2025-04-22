import numpy as np

def diffdiv(x, y):
    n =  len(x)
    F = np.zeros((n, n))
    F[:, 0] = y  
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+ 1,j - 1] - F[i,j - 1]) / (x[i+j] - x[i])

    return F[0, :]

