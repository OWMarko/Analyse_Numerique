#Dictionnaire
depart = {
    "Var": 83,
    "Isere": 38,
    "Drome": 26,
    "Vaucluse": 86,
    "Finistere": 29,
    "Cher": 18
}

#Extraire les valeurs selon une condition valeur < 30
valeurs_inf_30 = [valeur for cle, valeur in depart.items() if valeur < 30]

#Trier notre liste
valeurs_inf_30_triees = sorted(valeurs_inf_30)

#Extraire les valeurs selon une condition clefs avec un nombre de lettre
cles_6_lettres = [cle for cle in depart if len(cle) >= 6]

#Trier notre liste selon leur valeur ordre croissant (reverse = False)
cles_6_lettres_triees = sorted(cles_6_lettres, key=lambda x: depart[x], reverse = False)

#Trier notre liste selon l'ordre alphab. 
cles_6_filtrees_triees = sorted(cles_6_lettres, reverse = False)

#Extraire les paires (clefs, valeurs) selon une condition
paires_sup_30 = [(cle, valeur) for cle, valeur in depart.items() if valeur > 30]
E = [(cle, valeur) for cle, valeur in depart.items() if len(cle) <= 5]

#Trier par ordre alphabétique des clés
E_alpha = sorted(E, key=lambda x: x[0], reverse = False)

#Trier par ordre décroissant des valeurs NB ; On peut aussi l'utiliser si on a une liste qu'avec les clefs sans les valeurs, ça va nous trier notre liste selon l'odre décroissant des valeurs de nos clefs présente dans la liste
E_valeurs = sorted(E, key=lambda x: x[1], reverse=True)











