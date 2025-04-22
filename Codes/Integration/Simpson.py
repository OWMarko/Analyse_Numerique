import numpy as np

# élémentaire 
def quadraNumSimp(f,a,b):
  return (b-a)/6 * (f(a) + 4*f((b+a)/2) + f(b)

#Composé non uniforme
def quadraNumSimp_nnuni(f,x):
  if len(x)%2 == 0:
    raise ValueError("Nombre impair uniquement")
  h = np.diff(x)
  return np.sum((h[:-1] + h[1:]) / 6 * (f(x[:-2]) + 4 * f(x[1:-1]) + f(x[2:])))

#Composé uniforme
def quadraNumSimp_uni(f,a,b,M):
  if M%2 !=0:
    raise ValueError("M doit être pair")
  x = linspace(a,b,M)
  h = x[1] - x[0]
  return sum(f(x[:-1]) + 4*f((x[:-1] + x[1:])/2) + f(x[1:]))* h/6 
    

