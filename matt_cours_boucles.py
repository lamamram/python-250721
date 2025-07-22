# %%
# mettre les fruits en majuscules dans nouvelle liste
maj_fruits = []
fruits = ["pomme", "poire", "cerise", "orange"]

for f in fruits:
  maj_fruits.append(f.upper())
# si je n'ai pas besoin de garder la liste d'origine
del fruits
maj_fruits
# %%
fruits = ["pomme", "poire", "cerise", "orange"]
i = 0
for f in fruits:
  fruits[i] = f.upper()
  i += 1
fruits
# %%
# range: d'entier
# for i in range(10):
# for i in range(5, 10):
# for i in range(0, 10, 2):
for i in range (10, -1, -1):
  print(i)

# %%
# pas besoin de gestion d'index
fruits = ["pomme", "poire", "cerise", "orange"]
for i in range(len(fruits)):
  fruits[i] = fruits[i].upper()
fruits
# %%

fruits = [ (0, "pomme"), (1, "poire"), (2, "cerise"), (3, "orange") ]
# for f in fruits:
#  print(f)
# unpacking de la variable locale de la boucle
for i, fruit in fruits:
  print(i, fruit)
# %%
fruits = ["pomme", "poire", "cerise", "orange"]
# enumerate transforme une liste d'éléments en tuples à 2 éléments (indice, elem)
for i, fruit in enumerate(fruits):
  fruits[i] = fruit.upper()
fruits
# %%
fruits = ["pomme", "poire", "cerise", "orange"]
# liste en intension => définition des valeurs qu'on veut voire
# sucre syntaxique
# je veux créer des variables f.upper() prises dans les valeurs de la liste fruits
# avec un filtre (fruits qui commencent par "p")
fruits = [ f.upper() for f in fruits if f[0] == "p" ]
fruits
# %%
for i in range(2, 10):
  # regarder les entiers diviseurs possible depuis 2 jusqu'à i (en fait jusqu'à i//2 + 1)
  for j in range(2, i):
    # pas premier car j divise i
    if j >= i // 2 + 1:
      # pas besoin de regarder parce que j est trop grand pour diviser de façon entière i
      # on arrête l'itération courante du for courant et on continue avec l'itération suivante
      continue
    print(f"{j} est candidat divisueur possible de {i}")
    if i % j == 0:
      # j'interromps le for courant et je sors du for courant
      break
  # le else sur le for ne s'exécute que si le for associé se termine sans break
  # autrement dit le for associé est itérée jusqu'au bout
  else:
    print(f"{i} est premier !!!")
# %%
