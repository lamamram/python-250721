# %%
# conversions entre et vers les types numériques
# surcharge des opérateurs

1 + 1
# 1 + "1"
1 + int("1")
# concatenation de chaines de caractères => addition des strings
str(1) + "1"
# exemple rare de conversion implicite en python
1 + 3.14
# %%
# opérateur accumulatif
x = 1
# x += 1 <==> x = x + 1
x += 1
x -= 1
x *= 2
x /= 2
print(x)
# %%
# conversions explicites booléennes
number = 33
zero = 0
last_name = ""
empty_name = ""
PI = 3.14
zerof = 0.

print(bool(number), bool(empty_name), bool(PI))
print(bool(zero), bool(last_name), bool(zerof))
# %%
# expressions booléennes
# or: l'expression est vraie si au - un des opérandes est vrai
print(bool(number or empty_name or PI))
# and: l'expression est vraie si tous les opérandes sont vrais
print(bool(zero and last_name and zerof))
# %%
# la valeur rééle d'une expression booléenne
# or: retourne la première valeur vraie rencontrée ou la dernière valeur fausse
print(number or empty_name or PI)
# and: retourne la permière valeur fausse ou la dernière valeur vraie rencontrée 
print(zerof and last_name and zero)
# %%
# exemple d'usage des valeurs réelles d'expressions booléennes 
taux_imposition = 0
default = "non imposable"

taux_imposition or default

# %%
# négation booléenne
print(not empty_name)

# %%
## opérateur de comparaison
# ==: égalité
# !=: inégalité
# >: supérieur
# <: inférieur
# >=: supérieur ou égal
# <=: inférieur ou égal

# %% 
## le IF en python

# if number < 50 and last_name != ""
# if <expression>:
if number < 50 and last_name:
  # ici bloc d'instructions si l'expression est vraie
  # l'indentation est OBLIGATOIRE
  print(f"{last_name} à moins de 50 ans")
# else if <expression>: expression alternative
elif number >= 50 and last_name:
  print(f"{last_name} a plus de 50 ans")
# condition par défaut
else:
  print("pas de nom")
# suite du programme
print("fin du programme")
# %%
