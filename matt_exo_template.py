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

# while _template.find("((") != -1:
while _template.count("(("):
    start_index = _template.index("((")
    end_index = _template.index("))")
    key = _template[start_index + 2:end_index]
    # gestion de clé manquante
    val = injections.get(key, "N/A")

    _template = _template.replace("((" + key + "))", val)

print(_template)
# %%
