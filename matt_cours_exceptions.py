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
# Exception est le type d'erreur générique qui capture tout
except Exception as e:
  print(e, type(e))
# %%
