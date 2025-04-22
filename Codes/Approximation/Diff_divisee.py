import numpy as np

def diffdiv(x, y):
    n =  len(x)
    F = np.zeros((n, n))
    F[:, 0] = y  
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+ 1,j - 1] - F[i,j - 1]) / (x[i+j] - x[i])

    return F[0, :]


def diffdiv(x, y) :
    N = np.size(y)
    NN = np.size(y)
    if N != NN :
       return("Probleme de taille entre les vecteurs")
    Tab = np.zeros((N,N)) #tableau différence divisées
    Tab[:,0] = y #notre première colonne est connue
#Ligne par ligne
    for i in range (1,N) :
        for j in range (1,i+1) :
            Tab[i,j] = (Tab[i,j-1] - Tab[i-1,j-1])/(x[i] - x[i-j]) #Notre formule du cours diff divisé notre i
    return Tab

print(diffdiv(x,y))
