import numpy as np
from matplotlib.pyplot import * 

#élémentaire
def quadraNumPM(f,a,b):
  return (b-a) * f((a+b)/2)


#Composé non unfirme
def quadraNumPM_nnuni(f,x):
  h = np.diff(x)
  return sum(f((x[:-1] + x[1:]) / 2) *h


#COmposé uniforme 
def quadraNumPM_uni(f,a,b,M):
  x = np.linspace(a,b,M)
  h = x[1] - x[0]
  return sum(f((x[:-1] + x[1:] / 2 ))*h


#Utilisation 

def f(x):
  return x**2

#élémentaire 
a,b = 0,1
resultat_elementaire = quadraNumPM(f,a,b)

#composé non uniforme 
x = [0, 0.2, 0.5, 0.7, 1.0]
resultat_nnuni = quadraNumPM_nnuni(f,x)

#composé uniforme
M = 10
resultat_uni = quadraNumPM_uni(f,a,b,M)


        
