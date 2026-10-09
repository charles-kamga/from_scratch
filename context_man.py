def lire_fichier_securise(chemin_fichier):
    try:
        with open(chemin_fichier, "r") as fichier:
            contenu = fichier.read()
            print(contenu)
        return contenu
    except FileNotFoundError:
        print("Dsl, fichier introuvable")
        return "Erreur : fichier introuvable"

message = lire_fichier_securise("inconu.text")
print(message)
