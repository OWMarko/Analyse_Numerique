import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -y + np.cos(t)

#Résolution de la EDO (avec ou sans pb Cauchy, à faire à la main jour du TP)
def y_exact(t):
    return 0.5 * np.exp(-t) + 0.5 * (np.cos(t) + np.sin(t))

"""
Pour des soucis de visibilité et d'apprentissage, nous assumons que les fonctions Point_Milieu(t0, tf, f, y0, N) et Runge_Kutta(t0, tf, f, y0, N) sont déjà écrite dans notre code/
"""

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
# Comparaison graphique des solutions
#==================================================

#On paramètre la taille du graph
plt.figure(figsize=(10, 6))

# Tracé de la solution exacte
plt.plot(t_exact, y_ex, 'k-', label='Solution exacte', linewidth=2)

# Tracé des résultats par Point Milieu
plt.plot(t_pm, y_pm, 'bo-', label='Schéma Point Milieu', markersize=4)

# Tracé des résultats par Runge-Kutta
plt.plot(t_rk, y_rk, 'rs-', label='Schéma Runge–Kutta 4', markersize=4)

#Nos légendes, et axes
plt.xlabel('Temps t')
plt.ylabel('Solution y(t)')
plt.title("Comparaison des schémas")
plt.legend()
plt.grid(True)
plt.show()
