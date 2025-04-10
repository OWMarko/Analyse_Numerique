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

