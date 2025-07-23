"""
bibliothèque utils: 
uniquement des définitions de variables et fonctions (ou classes)
DEFAULT
parse_template
"""

## les imports sont TOUJOURS calculés depuis le programme principal
from project.helpers.logger import log

DEFAULT = "N/A"

def parse_template(
        tpl: str, 
        injects: dict, 
        delim: tuple=("{{","}}"), 
        default: str=DEFAULT,
        **opts
) -> str:
    """
    fonction d'interprétation d'un fichier template pour injecter
    des valeurs venues d'un diction
    **opts: "debug", "log", ...
    """
    while tpl.count(delim[0]):
        start_index = tpl.index(delim[0])
        end_index = tpl.index(delim[1])
        key = tpl[start_index + len(delim[0]):end_index]
        if "debug" in opts and opts["debug"]:
            log(f"key: {key}")
        val = injects.get(key, default)

        tpl = tpl.replace(delim[0] + key + delim[1], str(val))
    return tpl

# import et from ... import exécutent la totalité du fichier
# print("coucou")
