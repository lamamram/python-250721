# %%
# ouverture en lecture en utf-8
f = open("./users.csv", mode="r", encoding="utf-8")
content = f.read()
f.close()
print(content)

# %%
# gestionnaire de contexte : with
with open("./users.csv", mode="r", encoding="utf-8") as f:
  lines = []
  # les objets fichiers sont itérables
  for line in f:
    lines.append(line)
# en sortant du bloc with f est fermé
print(lines)
# f.read()
# %%
