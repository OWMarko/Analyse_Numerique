import numpy as np
from matplotlib.pyplot import * 

def quadNumRG(f,a,b,M):
    x = linspace(a,b,M)
    h = x[1] - x[0]
    return sum(f(x[:-1]))*h
