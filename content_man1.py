with open("journal.txt", "w") as f:
    f.write ("Debut du journal \n")

with open("journal.txt", "a") as fichier :
    fichier.write("Nouvelle entrée : tout fonctionne bien. \n")
