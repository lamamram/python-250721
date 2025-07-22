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
