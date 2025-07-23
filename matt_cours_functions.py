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
