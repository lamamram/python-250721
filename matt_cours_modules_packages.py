# %%
truc = """
machin {{k1}}
bidule {{k2}}
nawak {{k3}}
"""

data = {
    "k1": 33,
    "k2": 3.14
}

# %%
## programme principal
# import du fichier utils.py du même dossier
import utils

# utils est l'espace de nom de la fonction parse_template
print(utils.parse_template(truc, data))
# %%
# import sans espace de nom
from utils import parse_template

print(parse_template(truc, data))

# %%
# en cas de collision de noms on peut aliaser un import sans espace de nom
from utils import parse_template as parse_tpl

# ...
parse_template = "on"
# ...

print(parse_tpl(truc, data))
# %%
# import depuis un paquet (package)
# paquet => dossier + un fichier __init__.py + au - 1 module.py

# dir.subdir.{...}.module => chemin python (PYTHON PATH)
import project.utils

print(project.utils.parse_template(truc, data))

# %%
from project.utils import parse_template

print(parse_template(truc, data, debug=True))
# %%