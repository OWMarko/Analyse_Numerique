import numpy as np
import matplotlib.pyplot as plt

#############################
Numpy
#############################

#----------------------------------------------------------------------
# Créer un tableau (array) à partir d’une liste ou d’une autre séquence.
#----------------------------------------------------------------------

a = np.array([1, 2, 3, 4])
print("np.array:", a)  # Affiche : [1 2 3 4]


#----------------------------------------------------------------------
# Générer un tableau de nombres linéairement espacés.
#----------------------------------------------------------------------

x_lin = np.linspace(0, 10, 100)  # 100 points entre 0 et 10
print("np.linspace (5 premiers éléments):", x_lin[:5])


#----------------------------------------------------------------------
# Créer un tableau avec un pas fixe avec np.arange.
#----------------------------------------------------------------------

x_arange = np.arange(0, 10, 0.5)  # De 0 (inclus) à 10 (exclus) avec un pas de 0.5
print("np.arange:", x_arange)


#----------------------------------------------------------------------
# Créer un tableau rempli de zéros.
#----------------------------------------------------------------------

Z = np.zeros((3, 4))  # Matrice de dimension 3x4 remplie de 0
print("np.zeros:\n", Z)


#----------------------------------------------------------------------
# Créer un tableau rempli de uns.
#----------------------------------------------------------------------

O = np.ones(5)  # Vecteur de 5 éléments, tous égaux à 1
print("np.ones:", O)


#----------------------------------------------------------------------
# Créer un tableau non initialisé (les valeurs sont aléatoires selon la mémoire).
#----------------------------------------------------------------------

E = np.empty((2, 2))
print("np.empty:\n", E)


#----------------------------------------------------------------------
# Créer une matrice identité.
#----------------------------------------------------------------------

I = np.eye(3)  # Matrice identité 3x3
print("np.eye:\n", I)


#----------------------------------------------------------------------
# Indexation et slicing : accéder à une partie d'un tableau.
#----------------------------------------------------------------------

b = np.array([10, 20, 30, 40, 50])
print("Slicing b[1:4]:", b[1:4])   # Affiche : [20 30 40]


#----------------------------------------------------------------------
# Opérations arithmétiques élémentaires sur des tableaux.
#----------------------------------------------------------------------

c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print("Addition c + d:", c + d)       # Affiche : [5 7 9]
print("Multiplication c * d:", c * d)  # Affiche : [4 10 18]


#----------------------------------------------------------------------
# Exemple de broadcasting : opérations entre tableaux de formes différentes.
#----------------------------------------------------------------------

e = np.array([1, 2, 3])
f = np.array([[10], [20], [30]])
print("Broadcasting e + f:\n", e + f)
# Résultat : 
# [[11 12 13],
#  [21 22 23],
#  [31 32 33]]


#----------------------------------------------------------------------
# Calcul du produit scalaire ou matriciel avec np.dot.
#----------------------------------------------------------------------

g = np.array([1, 2])
h = np.array([3, 4])
print("np.dot(g, h):", np.dot(g, h))  # Affiche : 11


#----------------------------------------------------------------------
# Multiplication matricielle avec l'opérateur @.
#----------------------------------------------------------------------

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])
print("Multiplication matricielle A @ B:\n", A @ B)
# Affiche : [[4, 4], [10, 8]]


#----------------------------------------------------------------------
# Résolution d'un système d'équations linéaires avec np.linalg.solve.
#----------------------------------------------------------------------

A = np.array([[3, 1], [1, 2]])
b_vect = np.array([9, 8])
x_sol = np.linalg.solve(A, b_vect)
print("Solution du système:", x_sol)


#----------------------------------------------------------------------
# Calcul de la norme d'un vecteur avec np.linalg.norm.
#----------------------------------------------------------------------

v = np.array([3, 4])
print("Norme de v:", np.linalg.norm(v))  # Affiche : 5.0


#----------------------------------------------------------------------
# Ajustement de polynômes : np.polyfit et np.polyval.
#----------------------------------------------------------------------

x_poly = np.linspace(0, 10, 50)
y_poly = 2*x_poly + 3 + np.random.randn(50)*0.5  # Relation linéaire bruitée
coeff = np.polyfit(x_poly, y_poly, 1)  # Ajustement linéaire, degré 1
y_fit = np.polyval(coeff, x_poly)  # Évaluer le polynôme ajusté
print("Coefficients du polynôme (np.polyfit):", coeff)


#----------------------------------------------------------------------
# Intégration numérique avec np.trapz.
#----------------------------------------------------------------------

x_int = np.linspace(0, np.pi, 100)
y_int = np.sin(x_int)
area_trapz = np.trapz(y_int, x_int)  # Intégrale de sin(x) de 0 à pi
print("Intégrale par trapèzes (np.trapz):", area_trapz)


#############################
Matplotlib
#############################

#----------------------------------------------------------------------
# Tracer un graphique simple avec plt.plot.
#----------------------------------------------------------------------

x_plot = np.linspace(0, 10, 100)
y_plot = np.sin(x_plot)
plt.plot(x_plot, y_plot, 'b-')
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Graphique de sin(x)")
plt.show()


#----------------------------------------------------------------------
# Ajouter un titre et des labels aux axes.
#----------------------------------------------------------------------

plt.plot(x_plot, np.cos(x_plot), 'r--')
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.title("Graphique de cos(x)")
plt.show()


#----------------------------------------------------------------------
# Afficher un graphique en transformation logarithmique explicite.
# Utilisation de log sur les données avant de tracer.
#----------------------------------------------------------------------

h_vals = np.array([0.1, 0.05, 0.025, 0.0125])
errors = np.array([0.1, 0.025, 0.00625, 0.00156])
plt.plot(np.log(h_vals), np.log(np.abs(errors)), 'o-', label="Erreur")
plt.xlabel("log(h)")
plt.ylabel("log(|Erreur|)")
plt.title("Convergence en log-log")
plt.legend()
plt.show()

#----------------------------------------------------------------------
# Personnalisation
#----------------------------------------------------------------------
"""
Pour tracer une courbe, on peut définir :
# - la couleur avec 'color' (ex: 'red', 'blue', '#33FF99', ...)
# - le style de ligne avec 'linestyle' (ex: '-' continue, '--' tiret, '-.' tiret point, ':' pointillé)
# - la largeur de ligne avec 'linewidth' ou 'lw'
# - les marqueurs avec 'marker' ('o', 's', '^', 'd', '*', etc.)
# - la taille des marqueurs avec 'markersize' ou 'ms'
# - la couleur du bord du marqueur avec 'markeredgecolor' et l’épaisseur avec 'markeredgewidth'
# - la transparence avec 'alpha'
"""

plt.figure(figsize=(10, 5))
plt.plot(x, y,
         color='blue',           # Couleur en nom (alternativement: "#0000FF")
         linestyle='--',         # Ligne tiretée
         linewidth=2,            # Largeur de la ligne
         marker='o',             # Marqueur circulaire
         markersize=6,           # Taille du marqueur
         markerfacecolor='red',  # Couleur de remplissage du marqueur
         markeredgecolor='black',# Couleur du contour du marqueur
         markeredgewidth=1,      # Épaisseur du contour du marqueur
         alpha=0.8,              # Transparence (0 opaque, 1 transparent)
         label="sin(x)")

plt.xlabel("x")   
plt.ylabel("sin(x)")
plt.title("Graph")
plt.xlim(2, 8)  # Limite de l'axe des x
plt.ylim(-0.5, 0.5)  # Limite de l'axe des y

plt.annotate("Maximum local", xy=(1.57, np.sin(1.57)),
             xytext=(3, 1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)

plt.text(2, 0.0, "Zone centrale", color="purple", fontsize=12) # Ajouter un texte simple à une position donnée
plt.legend()  # Affiche la légende avec le label fourni ici sin(x)
plt.grid(True)  # Ajoute une grille
plt.show()
