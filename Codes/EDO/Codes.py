import numpy as np
import matplotlib as mpltb

def Eulerexplicite(x0, f, T, N): 
    dt = T / (N - 1)
    t = np.linspace(0, T, N)
    x = np.zeros(N)
    [x0] = x0
    for k in range(1, N): 
        xk = x[k-1] + dt * f(t[k-1], x[k-1])
    return t, x
