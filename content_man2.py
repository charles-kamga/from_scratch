def lire_contenu_fichier(nom_fichier):
    try:
        with open(nom_fichier, "r") as f:
            content = f.read("")
        return content
    except FileNotFoundError :
        return "None"
