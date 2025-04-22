import numpy as np

def eval_poly_scalaire(a, z) :
    n = np.size(a)
    Pz = 0
    for i in range (n) :
        Pz += a[i]*z**i
    return Pz

def eval_poly_vect(a,z) :
         n = np.size(a)
         N = np.size(z)
         P = np.zeros(N)
         for j in range(N) :
            P[j]=valpoly(a,z[j])
         return P
