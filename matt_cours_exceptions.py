# %%
data = {
  "name": "bob",
  "age": 44,
  "heigth": 1.70
}

data2 = {
  "name": "bill",
  "age": 43,
  "heigth": 1.70,
  "weight": 0
}

data3 = {
  "name": "bruno",
  "age": 43,
  "heigth": 1.70,
  "weight": 0
}

# %%
## bloc de code testé
try:
  # if "weight" in data:
  # Erreur ou Exception de type KeyError
  # le programme plante
  data["weight"]
  print("end_try")
## exécuté dès qu'il y a une erreur
except:
  print("erreur !!!")
print("suite du programme")
# %%
## sécuriser une portion de code avec except Exception
try:
  data2["weight"]
  ratio  = data2["heigth"]/data2["weight"]
  print("end_try")
except Exception as e:
  print(e, type(e))
# %%
## gérer différents types d'erreurs
try:
  data["weight"]
  ratio  = data2["heigth"]/data2["weight"]
  print("end_try")

except KeyError as e:
  print("pb de clé")
except ZeroDivisionError as e:
  print("weight null")
# Exception est le type d'erreur générique qui capture tout
except Exception as e:
  print(e, type(e))
# %%
# ajouter un else et un finally
try:
  data3["weight"]
  ratio  = data3["heigth"]/data3["weight"]
  print("end_try")
except KeyError as e:
  print(e, type(e))
## bloc exécuté si try s'exécute jusqu'au bout == sans erreur
else:
  print("pas d'erreur")
## bloc exécuté dans tous les cas même en cas de plantage == exception non géré
## juste avant de planter (logging, alerting, email ...)
finally:
  print("dans tous les cas possible même plantage")
# %%
def ratio_h_w(h, w):
  if not w:
    # déclencher une exception attendue par le code
    raise ValueError("poids nul")
  return h/w

data = {
  "h": 1.78,
  "w": 0
}

try:
  ratio_h_w(data["h"], data["w"])
# gestion du raise
except ValueError as e:
  print(e)
# %%
