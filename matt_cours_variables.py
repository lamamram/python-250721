# %%
# x est une référence / étiquette (tag) / libellé (label) représentant une valeur (1) en RAM
# on met 1 dans x
# on affecte (=) la valeur 1 à x
# "=" est l'opérateur d'affectation
# pas de déclaration de type en Python => typage dynamique
x = 1
# %%
# "y = x - 2" est une instruction => ligne de code
# "x - 2" est une expression
# "x" est une variable est également une expression
# "2" est une valeur littérale est également une expression
# expression = n'importe quelle écriture qui peut être affichée
y = x - 2
print(y)
print(-1)
print(x - 2)
# %%
# conventions de nommage des variables
# variables en minuscules + underscore => snake_case
first_name = "john"
last_name = 'doe'

# pas de valeurs constantes en python (!= const en c)
# mais par convention, on utilise des majuscules
PI = 3.14
# %%
## fonctions de base de python

# %%
# afficher la valeur
# 1. on peut affichier plusieurs expressions
# 2. on peut changer le séparateur entre exps (" ")
# 3. on peut changer la fin de ligne
print(x, y, last_name, PI * 2, sep="|", end=", ")
print("x - y =", x - y)
# %%
# saisir la valeur d'une variable à partir du clavier

last_name = input("insérez le nom de famille: ")
print(last_name)
age = input("insérez l'âge: ")
print(age)
# %%
# type: retourner le type de donnée d'une variable
print(type(age))

# convertir la variable age (str) en entier
# reaffectation d'une variable: age à gauche et à droite
# int(), str(), float() sont des fonctions de conversion
age = int(age)
# erreur => exception
# err = int("erreur")
# %%
#  autres fonctions d'introspection
# identifiant unique d'un objet en RAM géré par l'interpréteur Python
print(id(last_name))
x = 1
y = 1
# x et y pointent vers le même objet en RAM
print(id(x), id(y))
# opérateur "is" retourne un booléen True ou False
# print(id(x) == id(y)) => == opérateur de comparaison
print("x et y même valeur 1 => x is y vaut: ", x is y)
y = 2
print("x et y ont des valeurs ! => x is y vaut: ", x is y, id(x), id(y))
# %%
# help(): documentation
help(print)
# %%
# afficher les "variables et fonctions internes" d'une variable
print(dir(last_name))
# %%
# mettre une chaine de caractères en majuscules
# on utilise la fonction interne upper depuis la variable
# çà retourne la valeur transformée MAIS ne modifie PAS la valeur de la variable
print(last_name.upper(), last_name)
# %%
# supprimer une variable
truc = "machin"
del truc
truc
# %%
