# %%
# 1. saisir un entier au clavier => compris entre 0 et 86400 (nb de secondes dans une journée)
# 2. convertir la sortie précédente en entier
# 3. décomposer ce nombre en nb en heure, minutes, secondes
# 4. affichier le résulat <nb_hour>h <nb_min>m <nb_sec>

# number = int(input("saisir un nombre de secondes (0-86400) : "))
number = input("saisir un nombre de secondes (0-86400) : ")
# TODO vérifier que le nombre est bien convertible en entier
number = int(number)

nb_hour = number // 3600
# utilisation des parenthèses pour forcer l'ordre des opérations
nb_minute = (number % 3600) // 60
nb_second = number % 60

print(nb_hour, "h", nb_minute, "m", nb_second, "s")
# %%
## techniques de formatage de chaînes de caractères
## %%
# templating old-school (python2)
template = "%dh, %dm, %ds"
## tpl % (...)
# %: opérateur de formatage
# (...): tuple
# (x, y): paire, (x, y, z): triplet (x1, ..., xt) => t-uplet 
# structure ordonnée de valeurs de types disparates
# NON MODIFIABLE => immutable
print(template % (nb_hour, nb_minute, nb_second) )
# %%
# templating version python3
# {}: emplacement réservé pour les paramètres
template = "{}h, {}m, {}s"
print(template.format(nb_hour, nb_minute, nb_second))
# %%
# f-strings
print(f"{nb_hour + 2}h, {nb_minute}m {nb_second}s")

# %%
