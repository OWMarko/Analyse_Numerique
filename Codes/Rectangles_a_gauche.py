import numpy as np

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


#Utilisation 

def f(x):
    return x**2

a, b = 0, 1
M = 4
result_uniforme = quadNumRG(f,a,b,M):
print(result_uniforme)

x_points = [0, 0.3, 0.6, 1.0]  #subdiv non uniforme
result_non_uniforme = def quadNumRG_Compose(f,x):
print(result_non_uniforme)

    
