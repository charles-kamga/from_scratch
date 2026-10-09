try:
    with open("fichier_fantome.txt", "r") as f:
        contenu = f.read()
        print(contenu)
except :
    print("Le fichier n'existe pas encore, pas de panique !")

print("Le reste du programme continue à tourner tranquillement !")
