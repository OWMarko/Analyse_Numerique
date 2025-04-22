import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------------------
# Définition de l'EDO et de la solution exacte
#---------------------------------------------------------------------
def f(t, y):
    return -y + np.cos(t)

def y_exact(t):
    return 0.5 * np.exp(-t) + 0.5 * (np.cos(t) + np.sin(t))

"""
Pour des soucis de visibilité et d'apprentissage, nous assumons que les fonctions Point_Milieu(t0, tf, f, y0, N) et Runge_Kutta(t0, tf, f, y0, N) sont déjà écrite dans notre code/
"""

#==================================================
# On définit notre fonction de calcul d'erreur
#==================================================

def calculer_erreurs(approx, exacte):
    erreur_absolue = np.abs(approx - exacte)
    erreur_relative = erreur_absolue / np.abs(exacte)
    return erreur_absolue, erreur_relative
#==================================================
# Paramètres de l'intégration et résolution
#==================================================
t0 = 0.0
tf = 10.0
y0 = 1.0
N = 101  # Nombre de points (donc 100 sous-intervalles)

#==================================================
#On calcul pour les 2 schémas
#==================================================
t_pm, y_pm = Point_Milieu(t0, tf, f, y0, N)      
t_rk, y_rk = Runge_Kutta(t0, tf, f, y0, N)

#==================================================
#On calcul pour la solution exact
#==================================================
t_exact = np.linspace(t0, tf, 1000)
y_ex = y_exact(t_exact)

#==================================================
# On calcule les erreurs
#==================================================

erreur_pm, rel_error_pm = calculer_erreurs(y_pm, y_ex_pm)
erreur_rk, rel_error_rk = calculer_erreurs(y_rk, y_ex_rk)

#=======================================================================================
# Tracé des solutions et des erreurs (en log) sur une même figure à deux sous-graphiques
#=======================================================================================

#On paramètre la taille du graph
plt.figure(figsize=(12, 5))

# Sous-graphe 1 : Comparaison des solutions approchées et la solution exacte
plt.subplot(1, 2, 1)
plt.plot(t_pm, y_ex_pm, 'k-', label='Solution exacte', linewidth=2)
plt.plot(t_pm, y_pm, 'bo-', label='Point Milieu', markersize=4)
plt.plot(t_rk, y_rk, 'rs-', label='Runge–Kutta 4', markersize=4)
plt.xlabel('Temps t')
plt.ylabel('Solution y(t)')
plt.title("Comparaison des solutions approchées")
plt.legend()
plt.grid(True)

# Sous-graphe 2 : Tracé du logarithme de l'erreur absolue en fonction du temps
plt.subplot(1, 2, 2)
plt.plot(t_pm, np.log(np.abs(error_pm)), 'bo-', label="Point Milieu")
plt.plot(t_rk, np.log(np.abs(error_rk)), 'rs-', label="Runge–Kutta 4")
plt.xlabel('Temps t')
plt.ylabel('log(|Erreur|)')
plt.title("Erreur absolue (en log) vs. temps")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

#----------------------------------------------------------------------
# Représentation graphique en log-log
# On trace log(erreur) en fonction de log(h), ici h = T/Nvec avec Nvec = np.array([50, 100, 200, 400, 800])
#----------------------------------------------------------------------

plt.figure(3)
plt.plot(np.log(T/Nvec), np.log(errexp), 'r+-', label='Euler explicite')
plt.plot(np.log(T/Nvec), np.log(errCN), 'g+-', label='Crank Nicolson')

# On ajoute des droites de référence pour différentes pentes :
plt.plot(np.log(T/Nvec), np.log(T/Nvec), 'b', label='Droite de pente 1')    # Pente 1
plt.plot(np.log(T/Nvec), 2. * np.log(T/Nvec), 'c', label='Droite de pente 2')  # Pente 2
plt.plot(np.log(T/Nvec), 3. * np.log(T/Nvec), 'm', label='Droite de pente 3')  # Pente 3

plt.title("Graphe log-log")
plt.xlabel("log(N)")
plt.legend()
plt.show()
