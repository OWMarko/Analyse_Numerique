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
    
#Si on cherch les coefs du poly p
def coef(x,y): 
    x = np.array(x)
    y = np.array(y)
    n = len(x) - 1
    a = np.zeros(n)
    d = np.zeros(n)
    for i in range(n):
        a[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])
        d[i] = y[i] - a[i]*x[i]
    return a, d
