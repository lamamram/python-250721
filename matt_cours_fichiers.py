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
# écriture et en création ou en écrasement si le fichier existe
with open("./clone_users.csv", mode="w", encoding="utf-8") as f:
  # for line in lines:
  #   f.write(line)
  f.writelines(lines)


# %%
user = ["brenda", 28, "M", "admin"]
# prétraitement du 28 en "28"
for i in range(len(user)):
  user[i] = str(user[i])

# mode "a" comme "append" écriture à la fin du fichier
with open("./users.csv", mode="a", encoding="utf-8") as f:
  f.write(";".join(user))
# %%
import csv

with open("./users.csv", mode="r", encoding="utf-8") as f:
  rd = csv.reader(f, delimiter=";", quotechar='"')
  # itération pas à pas du reader (ou de n'importe quel itérable)
  lines = []
  header = next(rd)
  for line in rd:
    lines.append(line)
# %%

import csv
# pour utiliser le writer csv sur windows => ajouter newline="" désactive le saut de ligne sur f
with open("./clone_users.csv", mode="w", encoding="utf-8", newline="") as f:
  wr = csv.writer(f, delimiter=";", quotechar='"')
  wr.writerow(header)
  wr.writerows(lines)



# %%
