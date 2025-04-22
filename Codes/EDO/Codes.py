import numpy as np

def Euler_Explicite(t0, tf, f, y0, N):
    h = (tf - t0) / N
    t = np.linspace(t0, tf, N+1) 
    y0 = np.atleast_1d(y0) 
    m = y0.size 
    y = np.zeros((m, N+1)) 
    y[:, 0] = y0 
    for n in range(N):
        y[:, n+1] = y[:, n] + h * f(t[n], y[:, n])
    return t, y 


"""
Expliquons le code du Schéma d'Euler explicite :  : 

Arguments :
      t0 : temps initial
      tf : temps final
      f  : notre EDO comme en cours pb de Cacuhy ->  f(t, y)
      y0 : condition initiale (peut être un scalaire ou un vecteur)
      N  : nombre de pas

Code : 
Ligne 1 : on calcule la longueur de chaque intervalle de chaque sous intervalle, on regarde la longueur totale : tf - t0, ensuite on divise par le nombre de sous intervalle.
Ligne 2 : tableau des temps
Ligne 3 : on regarde si on a un vecteur (système) ou un scalaire pour bien adapter notre 
Ligne 4 : dimension de notre première valeur
Ligne 5 : on crée notre vecteur (ou matrice) des résultats / approximations
Ligne 6 : on initalise la première valeur de notre tableau 
Ligne 7 Boucle : schema Euler Explicite
Ligne 9 Return : on prend nos approximation et notre tableau des temps


Return :
      t : tableau des instants (N+1 éléments)
      y : solution approchée, de dimension (m, N+1) si y0 est de dimension m.
"""



"""


