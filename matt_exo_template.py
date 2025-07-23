"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

# %%

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": "500",
    "section": "30",
    "debit": "2"
}

# %%
# pour tester avec un petit nb d'itérations
# i = 0
# while _template.find("((") != -1:
while _template.count("(("):
    start_index = _template.index("((")
    end_index = _template.index("))")
    key = _template[start_index + 2:end_index]
    # gestion de clé manquante
    val = injections.get(key, "N/A")

    _template = _template.replace("((" + key + "))", val)
    # if i > 10:
    #   break
    # i += 1

print(_template)
# %%
# créer une fonction à partie de la cellule ci dessous

# 1/ enapsuler le code ave un def et un nom():
# 2/ remplacer les variables globales avec un paramètre (refactoring: remplacer avec ctrl+H)
# 3/ remplacer les valeurs littérales qui peuvent varier
# 4/ remplacer le print en return et utiliser l'appel

def parse_template(tpl, injects, delim, default):
    while tpl.count(delim[0]):
        start_index = tpl.index(delim[0])
        end_index = tpl.index(delim[1])
        key = tpl[start_index + 2:end_index]
        val = injects.get(key, default)

        tpl = tpl.replace(delim[0] + key + delim[1], str(val))
    return tpl

# %%
_template = parse_template(_template, injections, ("((","))"), "N/A")
_template
# %%
truc = """
machin {{k1}}
bidule {{k2}}
"""

data = {
    "k1": 33,
    "k2": 3.14
}

print(parse_template(truc, data, ("{{", "}}"), ""))
# %%
