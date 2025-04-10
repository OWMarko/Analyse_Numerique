import numpy as np
from matplotlib.pyplot import * 

#élémentaire
def quadNumRG(f,a,b,M):
    x = np.linspace(a,b,M)
    h = x[1] - x[0]
    return sum(f(x[:-1]))*h


#composé non uniforme
def quadNumRG_Compose(f,x):
    h = np.diff(x)
    return np.sum(f(x[:-1]) * h)

#composé uniforme
def quadNumRG_Compose_Uniforme(f,x):
    x = np.linspace(a,b,M)
    h = x[1] - x[0]
    return np.sum(f(x[:-1]) * h

    
