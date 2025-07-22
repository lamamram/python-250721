"""
1/ saisir n valeurs entiers relatifs séparés par ","
2/ on veut itérer sur les valeurs pour vérifier
que ces valeur sont des entiers relatifs
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste
5/ présenter le résultat avec 2 chiffres sign.  
"""

# %%
# saisie n valeurs entiers relatifs séparée par , depuis le clavier
saisie = input("Saisir des valeurs entiers relatifs séparées par une virgule : ")
saisie
# %%
# itérer sur les valeurs pour vérifier
# print = 2
# print("hello")

liste = saisie.split(",")
liste
# %%
for valeur in liste:
  # si la valeur est un entier positif ou négatif
  # négatif == 1er caractère "-" ET le reste est numérique
  if valeur.isnumeric() or ( valeur[0] == "-" and valeur[1:].isnumeric()):
    valeur = int(valeur)
# %%
