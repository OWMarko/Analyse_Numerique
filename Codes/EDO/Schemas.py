import numpy as np
from scipy.optimize import fsolve

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

def Euler_Implicite_Newton(t0,tf,f,y0,N):
    h = T / (N - 1) 
    t = np.linspace(0, T, N) 
    x = np.zeros(N) 
    x[0] = x0 
    for k in range(1, N): 
        xk = x[k-1] 
        tk = t[k] 
        g = lambda y: y - xk - dt * f(tk, y) 
        dg = lambda y: 1 - dt * df(tk, y) 
        x[k] = Newton(xk, g, 10, 1e-10, 1e-10, tk, dt, xk) 
    return t, x

"""
Il existe plusieurs schéma d'Euler Implicite, certains utilisent l'algo de Newton, d'autres non. Dans le cours nous nous limitons à l'Euler Implicite générale, sans cas particulier comme dans l'exercice 1.2 du TP5. 
Pour ce faire, nous appliquons le même raisonnemment qu'à l'Euler Explicite le seul détail qui change est la boucle, on résoud explicitement notre équation en y[n+1]. 
"""

def Euler_Implicite(t0,tf,f,y0,N):
    h = (tf-t0)/N
    t = np.linspace(t0, tf, N+1) 
    y0 = np.atleast_1d(y0) 
    m = y0.size
    y = np.zeros((m, len(y0)) 
    y[:, 0] = y0
    for n in range(N):
        g = lambda y_suiv: y_suiv - y[n] - h * f(t[n+1], y_suiv)
        y[n+1] = fsolve(g, y[n])
    return t, y

"""
Expliquons le code d'Euler Implicite.

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
Ligne 8 c'est quoi ce lambda ?  Pour passer de y[n] à y[n+1] nous devons satisfaire l'équation suivante : y[n+1] = y[n] + h*f(t[n+1],y[n+1])
Et comme dit précédement, nous devons résoudre l'équation y[n+1], et nous savons que nous pouvons trouver les racines de la fonction caractéristique de la EDO, trouver les racines et résoudre.
C'est ce que nous faisons ici, nous cherchons implicitement (car on retrouve n+1 des deux côtés) la racine de g. et si y_suiv correspond à notre racine, alors elle devient y[n+1]
Linge 9 : On regarde si notre y_suiv correspond à la racine en utilisant la résolution numérique de scipy. Dans le contexte du TP et peut-être du contrôle, on devra le faire à la main ;) 
Ligne 10 Return : on prend nos approximation et notre tableau des temps


Return :
      t : tableau des instants (N+1 éléments)
      y : solution approchée, de dimension (m, N+1) si y0 est de dimension m.
"""

def Point_Milieu(t0,tf,f,y0,N): 
    h = (tf-t0)/ (N-1)
    t = np.linspace(t0, tf, N)
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m,N) 
    y[:, 0] = y0
    for k in range(1, N):
        tk_mid = t[k-1] + h/2.
        y_mid = y[:, k-1] + (h/ 2.) * f(t[k-1], y[:, k-1])
        y[:, k] = y[:, k-1] + h* f(tk_mid, y_mid)    
    if m == 1:
        return t, x[0, :]
    return t, x

"""
Expliquons ce code : 

Arguments :
t0 : temps initial
tf : temps final
f  : notre EDO comme en cours pb de Cacuhy ->  f(t, y)
y0 : condition initiale (peut être un scalaire ou un vecteur)
 N  : nombre de pas

Code :


  
Retourne :
      t : numpy.ndarray
          Vecteur temps de dimension (N,).
      x : Pour un problème scalaire, un tableau 1D de dimension (N,).
          Pour un système, un tableau de dimension (m, N), où m est la dimension de y0.
    """
