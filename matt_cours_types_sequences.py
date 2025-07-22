# %%
# présentation des listes et des tuples
# list: structure de données, de types disparates, indexable
patient = ["pierre", "dupont", 33, 1.76]

print(patient, type(patient), dir(patient))
# %%
## lire un élément d'une liste
# first_name = patient[0]
# age = patient[2]
# afectation en ligne  => unpacking
first_name, age = patient[0], patient[2]
print(first_name, age)
# %%
# lire le dernier élément d'une liste
# longueur de la liste
# liste_size = len(patient)
# print(patient[liste_size - 1])
print(patient[len(patient) - 1])
print(patient[-1])
# %%
# str: un chaine de caractères est indexable
first_name[0], len(first_name)
# %%
## modifier un élément d'une liste => mutabilité
patient[0] = "jean"
patient[0] = patient[0].capitalize()
print(patient)
# %%
# impossible de modifier un élément d'une str => immutabilité
# first_name[0] = "P"
# on est obligé de réaffecter la variable
# REM: capitalize() retourne une valeur modifée MAIS ne modifie pas la variable
first_name = first_name.capitalize()
# %%
patient = tuple(patient)
patient, type(patient), patient[0], len(patient)

# tuple:  immutable
# ERROR
# patient[0] = "jean"
# %%
# unpacking d'un tuple
first_name, last_name, age, height = patient
# first_name, last_name, age, height = patient[0], patient[1], patient[2], patient[3] 
print(first_name, last_name, age, height)
# %%
# opérateur in
phrase = "appeler un chat un chat"

"chat" in phrase
if "chat" not in phrase:
  print("pas de chat dans la phrase")
# %%
# convertir une str en liste de mots
mots = phrase.split()
print(mots)
print("chat" in mots)
print(mots.count("chat"))
# %%
## mutabilité des listes
# ERROR
# mots[5] = "est"
# append ne retourne pas une valeur mais modifie la variable
print(mots.append("est"))
mots.append("correct")
print(mots)

# %%
# au lieu de faire 2x append on aurait pu ajouter une liste à 2 éléments à le 1ère
# mots.extend(["correct", "correct"])
# même chose
mots + ["est", "correct"]

# %%
# supprimer
# print(mots.pop(-1))
# print(mots.pop(-1))
# print(mots.pop())
# print(mots.pop())
print(mots)
# %%
# tranche entre l'indice de début compris
# et l'indice de fin NON compris
# mots[1:-2]
mots[1:3]

# tranche à partir de un et à la fin
mots[1:]

# tranche depuis le début jusqu'au 1er chat compris
mots[:3]
# %%
# retourner l'index de 1ère occurence d'une valeur d'une liste
mots.index("chat")
mots[:mots.index("chat") + 1]
# %%
# joindre les éléments d'une liste de même type str
phrase = " ".join(mots)
# %%

## in, slicing [:], .index(), .count(), fonctionne avec les str et tuples
phrase[3:10], phrase.count("chat")
# %%

# itérer sur les éléments d'une liste ou d'un tuple ou d'une str
# pour chaque élément appelé "mot" dans liste "mots"
## on itère en consumant les élements des structures itérables (str, list, tupole)
for mot in mots:
  print(mot)

print("fin de la boucle")

for letter in phrase:
  print(letter)
# %%

## reprendre l'exemple du patient avec un dictonnaire
patient = {
  "first_name": "pierre",
  "last_name": "dupont",
  "age": 33,
  "height": 1.76
}
patient
# %%
patient["first_name"]
# %%
# une clé peut être autre chose qu'une str !!!
points = {
  (-2.4303, 47.4354): "PARIS",
  (-1.6345, 42.4544): "MARSEILLE"
}

## 
patient["first_name"] = "jean"
print(dir(patient))
patient, type(patient)


# %%
# l'opérateur in foncitonne avec les clés et pas les valeurs
print("jean" in patient)
print("first_name" in patient)
# %%
# print(patient["weight"])

# if "weight" in patient:
#   print(patient["weight"])
# else:
#   print(60)

# retourner la valeur d'une clé OU une valeur par défaut SINON
print(patient.get("weight", 60))
print(patient.get("height", 1.70))
# %%
# a priori on itère sur les clés
print("----keys-----")
for x in patient:
  print(x)
print("----values-----")
for v in patient.values():
  print(v)
print("----items (key, value)-----")
for k, v in patient.items():
  print(k, v)
# %%
# dict => list
list(patient.items())
# %%
# list[tuple(2)] => dict

paires = [("key1", "value1"), ("key2", "value2")]
dict(paires)
# %%
