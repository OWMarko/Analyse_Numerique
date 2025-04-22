import numpy as np

def Euler_Explicite(t0, tf, f, y0, N):
    h = (tf - t0) / N #on calcule la longueur de chaque intervalle de chaque sous intervalle, on regarde la longueur totale : tf - t0, ensuite on divise par le nombre de sous intervalle.
    t = np.linspace(t0, tf, N+1) #tableau des temps
    y0 = np.atleast_1d(y0) #on regarde si on a un vecteur (système) ou un scalaire pour bien adapter notre y
    m = y0.size #
    y = np.zeros((m, N+1))
    y[:, 0] = y0
    for n in range(N):
        y[:, n+1] = y[:, n] + h * f(t[n], y[:, n])
    return t, y


