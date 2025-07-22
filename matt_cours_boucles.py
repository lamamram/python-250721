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
