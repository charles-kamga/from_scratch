classe = [
    {"etudiant": "Sam", "note": 14},
    {"etudiant": "Léa", "note": 18},
    {"etudiant": "Tom", "note": 9},
    {"etudiant": "Chloé", "note": 16},
]

def calculer_statistiques(liste_etudiants):
    somme_notes = 0
    for n in liste_etudiants:
        somme_notes += n["note"]
    moyenne = somme_notes / len(liste_etudiants)
    admis =[]
    for etu in liste_etudiants:
        if etu["note"] >= 10:
            admis.append(etu["etudiant"])

    return {
        "moyenne" : moyenne,
        "admis" : admis
        }


print(calculer_statistiques(classe))
