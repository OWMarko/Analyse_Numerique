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
Ligne 1 : on calcule la longueur de chaque intervalle de chaque sous intervalle, on regarde la longueur totale : tf - t0, ensuite on divise par le nombre de sous intervalle.
Ligne 2 : tableau des temps
Ligne 3 : on regarde si on a un vecteur (système) ou un scalaire pour bien adapter notre 
Ligne 4 : dimension de notre première valeur
Ligne 5 : on crée notre vecteur (ou matrice) des résultats / approximations
Ligne 6 : on initalise la première valeur de notre tableau
Ligne 7 Boucle : schema Point Milieu 
Linge 8 : on calcul le temps entre t[k] et t[n+1]
Ligne 9 : l'idée est de ne pas avancer de 1 en 1 mais de trouver l'approximation entre n et n+1, on part de notre solution y[:, k-1] puis on calcule l'approxi entre ce point et y[:,k] 
MAIS ! On calcule la dérivé de f (la pente, et la ED) en K-1 et pas en mid ou K !!!! Et la boucle itère le procédé.
Ligne 10 : Maintenant on utilise nos "approximation et temps MID" pour trouver l'approximation de notre y en k (le pas suivant car remember : on était en k-1), on évalue la dérivé au point mid multiplié par notre discrétisation (subdiv)
On remarque que c'est "simplement" Euler Explicite mais en calculant le mid entre deux points. 


Return :
      t : Vecteur temps de dimension (N,) (un array !!!!)
      y : scalaire -> un tableau 1D de dimension (N,).
          système -> un tableau de dimension (m, N), où m = y0.size
    """

def Cranck_Nicolson(t0,tf,f,y0,N,tol=1e-8,maxit=50):
    h = (tf - t0) / (N - 1)
    t = np.linspace(t0, tf, N)
    y0 = np.atleast_1d(y0)
    m = y0.size
    y = np.zeros((m, N))
    y[:, 0] = y0
    for k in range(1, N):
        y_suiv = y[:,k-1].copy()
        for _ in range(maxit):
            y_nouv = y[:, k-1] + (h / 2.) * ( f(t[k-1], y[:, k-1]) + f(t[k], y_suiv))
            if np.linalg.norm(y_nouv - y_suiv) < tol:
                y_suiv = y_nouv
                break
            y_suiv = y_nouv.copy()
        y[:, k] = y_suiv
    if m == 1:
        return t, y[0, :]
    return t, y

"""
Expliquons ce code : 

Arguments :
t0 : temps initial
tf : temps final
f  : notre EDO comme en cours pb de Cacuhy ->  f(t, y)
y0 : condition initiale (peut être un scalaire ou un vecteur)
 N  : nombre de pas
tol  : tolérance pour l'itération de point fixe
maxit: nombre maximum d'itérations à chaque pas

Code :
Ligne 1 : on calcule la longueur de chaque intervalle de chaque sous intervalle, on regarde la longueur totale : tf - t0, ensuite on divise par le nombre de sous intervalle.
Ligne 2 : tableau des temps
Ligne 3 : on regarde si on a un vecteur (système) ou un scalaire pour bien adapter notre 
Ligne 4 : dimension de notre première valeur
Ligne 5 : on crée notre vecteur (ou matrice) des résultats / approximations
Ligne 6 : on initalise la première valeur de notre tableau
Ligne 7 Boucle : schema Cranck Nicolson, on cherche à résoudre l'équation suivante : y[k] = y[k-1] + (h/2)*[ f(t[k-1], y[k-1]) + f(t[k], y[k])], pour trouver y[k], nous utiliserons la méthode du point fixe
Ligne 8 : Pour essayer de trouver le bon candidat, on ne va pas jouer avec notre vrai vecteur donnée mais on va faire une copie de celui-ci pour s'assurer de ne pas modifier nos valeurs donnée y. Et on va commencer à k-1 et pas k.
Ligne 9 : Maintenant on crée une boucle pour tester nos points fixe et s'ils correspondent bien. donc on applique notre schema avec notre y_suiv (en réalité c'est notre guess, on suppose pour voir)
Ligne 10 : On vérifie s'il y a convergence et s'il correspond à nos conditions de point fixe, si oui -> 
Ligne 11 : on pose que notre guess (le suiv) est bon et donc on pose que y_nouv = y_suiv ce qui revient à dire que y_suiv = y[:, k-1], et ainsi de suite grâce à notre boucle.
Ligne 12 : Si on traite des scalaire, on applique le schema aussi et on retourne un vecteur 1D et pas un tableau de 2 dimension


Return :
      t : Vecteur temps de dimension (N,) (un array !!!!)
      y : scalaire -> un tableau 1D de dimension (N,).
          système -> un tableau de dimension (m, N), où m = y0.size
    """

#Du TP
def CrankNicolsonEx3(T,N,Y0):
    A=np.zeros((2,2))
    A[0,0]=0
    A[0,1]=1
    A[1,0]=-k/m
    A[1,1]=0
    h = T/N
    t=np.linspace(0,T,num=N+1)  
    l=np.size(Y0)
    y=np.zeros((l,N+1))
    y[:,0]=Y0[:]
    for n in range(0,N):
      y[:,n+1] = np.linalg.solve(np.eye(l)-1./2.*h*A,y[:,n]+1./2.*h*np.dot(A,y[:,n]))
    return t,y
