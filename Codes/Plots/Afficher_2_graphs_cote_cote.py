import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------
# Initialisation des données
#---------------------------------------------------------------------
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

#---------------------------------------------------------------------
# Création d'une figure avec 1 ligne et 2 colonnes
#---------------------------------------------------------------------

fig, axs = plt.subplots(1, 2, figsize=(10, 4))  

#---------------------------------------------------------------------
# Premier graphique sur notre axe x (coo : (0,1) )
#---------------------------------------------------------------------

axs[0].plot(x, y1, 'b-')
axs[0].set_title("Sinus")
axs[0].set_xlabel("x")
axs[0].set_ylabel("sin(x)")

#---------------------------------------------------------------------
# Deuxième graphique sur notre axe x (coo : (0,2) )
#---------------------------------------------------------------------
axs[1].plot(x, y2, 'r-')
axs[1].set_title("Cosinus")
axs[1].set_xlabel("x")
axs[1].set_ylabel("cos(x)")

#---------------------------------------------------------------------
#Affichage & Ajustements
#---------------------------------------------------------------------

#Bien ajusté côte à côte
plt.tight_layout()

#Afficher la figure
plt.show()

