# %%
## bloc de code testé
try:
  data = {
    "name": "bob",
    "age": 44,
    "heigth": 1.70
  }
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
