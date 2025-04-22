import numpy as np
import matplotlib.pyplot as plt

# --- Paramètres de l'intégration ---
a = 0.0                 # borne inférieure
b = 2 * np.pi           # borne supérieure

# Vecteur contenant différents nombres d'intervalles pour affiner la discrétisation
M_values = np.array([50, 200, 400, 800])
taille_M = M_values.size

# Calcul du pas de discrétisation associé à chaque M:
h_values = (b - a) / M_values

# Valeur exacte de l'intégrale (ici donnée par l'expression issue du TP)
ex = -((10 * np.pi - 3 + 3 * np.exp(2 * np.pi)) / (25 * np.exp(2 * np.pi))) * np.ones(l)

# --- Méthode : Rectangles à gauche ---
Grg = np.zeros(taille_M)  # approximations calculées
for i in range(taille_M):
    Grg[i] = fonctions.intnum(a, b, M_values[i], fonctions.f2, 1)
# Calcul de l'erreur : différence entre la valeur approchée et la valeur exacte
erg = Grg - ex

# Tracé en échelle logarithmique
plt.figure(figsize=(10, 6))
plt.plot(np.log(h_values), np.log(np.abs(erg)), 'o-', label="Rectangles à gauche")

# Calcul des ordres numériques (pentes locales sur la courbe log-log)
orders_rect_left = (np.log(np.abs(erg[1:])) - np.log(np.abs(erg[:-1]))) / (np.log(h_values[1:]) - np.log(h_values[:-1]))
print("Ordres numériques rectangles à gauche :", orders_rect_left)

# --- Méthode : Rectangles à droite ---
Grd = np.zeros(taille_M)
for i in range(taille_M):
    Grd[i] = fonctions.intnum(a, b, M_values[i], fonctions.f2, 2)
erd = Grd - ex

plt.plot(np.log(h_values), np.log(np.abs(erd)), 's-', label="Rectangles à droite")
orders_rect_right = (np.log(np.abs(erd[1:])) - np.log(np.abs(erd[:-1]))) / (np.log(h_values[1:]) - np.log(h_values[:-1]))
print("Ordres numériques rectangles à droite :", orders_rect_right)

# --- Méthode : Point milieu ---
Gpm = np.zeros(taille_M)
for i in range(taille_M):
    Gpm[i] = fonctions.intnum(a, b, M_values[i], fonctions.f2, 3)
epm = Gpm - ex

plt.plot(np.log(h_values), np.log(np.abs(epm)), '^-', label="Point milieu")
orders_midpoint = (np.log(np.abs(epm[1:])) - np.log(np.abs(epm[:-1]))) / (np.log(h_values[1:]) - np.log(h_values[:-1]))
print("Ordres numériques point milieu :", orders_midpoint)

# --- Méthode : Trapèzes ---
Gt = np.zeros(taille_M)
for i in range(taille_M):
    Gt[i] = fonctions.intnum(a, b, M_values[i], fonctions.f2, 4)
et = Gt - ex

plt.plot(np.log(h_values), np.log(np.abs(et)), 'd-', label="Trapèzes")
orders_trapezoidal = (np.log(np.abs(et[1:])) - np.log(np.abs(et[:-1]))) / (np.log(h_values[1:]) - np.log(h_values[:-1]))
print("Ordres numériques trapèzes :", orders_trapezoidal)

# --- Méthode : Simpson ---
Gs = np.zeros(taille_M)
for i in range(taille_M):
    Gs[i] = fonctions.intnum(a, b, M_values[i], fonctions.f2, 5)
es = Gs - ex

plt.plot(np.log(h_values), np.log(np.abs(es)), 'v-', label="Simpson")
orders_simpson = (np.log(np.abs(es[1:])) - np.log(np.abs(es[:-1]))) / (np.log(h_values[1:]) - np.log(h_values[:-1]))
print("Ordres numériques Simpson :", orders_simpson)

# Configuration finale du graphique
plt.xlabel("log(h)")
plt.ylabel("log(abs(erreur))")
plt.title("Convergence des méthodes d'intégration numérique")
plt.legend()
plt.grid(True)
plt.show()
