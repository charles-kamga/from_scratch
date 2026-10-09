# Exercice de manipulation de données Python
# Analyse les notes des étudiants et affiche le classement

données = [
    {"nom": "Alice", "sexe": "f", "note": 18, "date_naissance": "2022-04-15", "heure_repose": "19:30"},
    {"nom": "Bob", "sexe": "m", "note": 14, "date_naissance": "2022-03-10", "heure_repose": "20:00"},
    {"nom": "Charlie", "sexe": "m", "note": 16, "date_naissance": "2022-01-25", "heure_repose": "18:45"},
    {"nom": "Diane", "sexe": "f", "note": 12, "date_naissance": "2022-02-28", "heure_repose": "19:15"},
    {"nom": "Erf", "sexe": "m", "note": 10, "date_naissance": "2022-05-20", "heure_repose": "20:30"},
]

# Exercice 1 : Affichage des informations
print("=== Infos sur les élèves ===")
for etudiant in données:
    print(f"{etudiant['nom']} : {etudiant['date_naissance']} (Note: {etudiant['note']})")

# Exercice 2 : Trouver l'élève avec la meilleure note
meilleure_note = max(données, key=lambda d: d['note'])
print(f"\n=== Meilleure note : {meilleure_note['nom']} ({meilleure_note['note']}) ===")

# Exercice 3 : Filtrer par date de naissance
print("\n=== Élèves nés en 2022 ===")
d2022 = [d for d in données if d['date_naissance'].startswith('2022')]
for e in d2022:
    print(f"{e['nom']}")

# Exercice 4 : Trier par note décroissante
classe_trip = sorted(données, key=lambda d: d['note'], reverse=True)
print("\n=== Classement par note décroissante ===")
for i, etudiant in enumerate(classe_trip, 1):
    print(f"{i}. {etudiant['nom']} : {etudiant['note']}")

# Exercice 5 : Filtrer par note
print("\n=== Élèves avec note >= 15 ===")
excellents = [d for d in données if d['note'] >= 15]
for e in excellents:
    print(f"{e['nom']} ({e['sexe']})")
