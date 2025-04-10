import numpy as np
from matplotlib.pyplot import * 


#élémentaire
def quadNumRD(f,a,b):
  return (b-a)*f(a)


#Composé non uniforme
def quadNumRD(f,a,b,M):
    h = np.diff(x)
    return sum(f(x[1:])*)h


#Composé uniforme
def quadNumRD(f,a,b,M):
    x = linspace(a,b,M)
    h = x[1] - x[0]
    return sum(f(x[1:]))*h


#Utilisation : 

def f(x):
    return x**2

# Cas élémentaire
a, b = 0, 1
result_elementaire = quadNumRD(f,a,b)
print(result_elementaire)

# Cas uniforme
M = 10
result_uniforme = quadNumRD(f,a,b,M)
print(result_uniforme)

# Cas non uniforme
x_points = [0, 0.25, 0.5, 0.75, 1.0]  
result_non_uniforme = quadNumRD(f,a,b,M)
print(result_non_uniforme)

