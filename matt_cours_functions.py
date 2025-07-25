# %%
## définition et appel d'une fonction

def ma_fonc():
  print("coucou")

# appel: () est l'opérateur d'appel
# exécute le bloc de la fonction
ret = ma_fonc()
# pas de return donc l'appel vaut NONE
print(ret)

# introspection sur la fonction
# print(type(ma_fonc), dir(ma_fonc))
# %%
## valeur de retour d'une fonction
def ma_fonc():
  return "coucou"
  # return arrête le bloc de la fonction
  print("end")

# appel: () est l'opérateur d'appel
# exécute le bloc de la fonction
ret = ma_fonc()
print(ret)
# %%

def deux_fois_deux():
  return 2 * 2

result = deux_fois_deux()
result

# %%
# paramètre à la définition
def fois_deux(nb):
  return nb * 2

# paramètre à l'appel => obligatoire
val = 2
# result = fois_deux(2)
# result = fois_deux(val)
result = fois_deux(val * 2)
result
# %%
# gestion de types des paramètres: AUCUNE


fois_deux(3.14)
# surcharge de * pour les str, list, tuple : répétition
fois_deux("rien")
fois_deux([0])
fois_deux({"key": "value"})
# %%
# annotation => indication pas un contrôle
# pour contrôler: if ou utiliser des exceptions
def deux_fois(nb: int|float):
  if type(nb) in (int, float):
    return nb * 2
  else:
    print(f"bad type: {type(nb)}")

deux_fois({})
deux_fois(2)
# %%
# notion de portée
# nb est globale (extrieure) à la fonction
nb = 2

def fois_deux():
  # a priori nb est locale (interne à la fonction)
  # sauf si on ajoute 
  # global nb
  nb = 2
  nb *= 2
  print(nb)


fois_deux()
print(nb)

## on utilise global pour des fonctions que ne retournent pas
## MAIS modifie des variables globales
## fonction san retour => procédure

## on préfère ajoute des paramètres et un return
# %%
# paramètres positionnels et optionnels à la définition

def ma_fonc(pos1, pos2, opt="default"):
  print(pos1, pos2, opt)

ma_fonc(10, 3.13, "truc")
ma_fonc(10, 3.13)
ma_fonc(10)
# %%
# option variadic *args:
# permet d'appeler une fonction avec 1 ou plusieurs paramètres positionnels 
# ces paramètres sont stockés dans un tuple
def ma_fonc(*param):
  print(param)

ma_fonc(2)
print(2)
ma_fonc(2, 3, "truc")
print(2, 3, "truc")
# %%
# option variadic **kw
# permet d'appeler une fonction avec 1 ou plusieurs paramètres optionnels 
# ces paramètres sont stockés dans un dictionnaire
def ma_fonc(param, **opts):
  print(param, opts)

ma_fonc(1, opt1=2)
ma_fonc(1, opt1=2, opt2="truc")
# %%
