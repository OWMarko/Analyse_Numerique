import numpy as np

def Vandermonde(x) :
    N = np.size(x)
    Vander = np.zeros((N,N))
    for j in range (N) :
        for i in range (N) :
            Vander[i,j]= (x[i])**j
    return Vander

#On peut aussi le faire sans boucle pour économiser de la mémoire et temps de calcul :

def matrice_vandermonde_mieux(x):
    X = np.array(x)
    N = len(X)
    V = X[:, np.newaxis] ** np.arange(N)
    return V
