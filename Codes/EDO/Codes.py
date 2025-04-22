import numpy as np

def Euler_Explicite(t0, tf, f, y0, N):
    h = (tf - t0) / N
    t = np.linspace(t0, tf, N+1)
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m, N+1))
    y[:, 0] = y0
    for n in range(N):
        y[:, n+1] = y[:, n] + h * f(t[n], y[:, n])
    return t, y


