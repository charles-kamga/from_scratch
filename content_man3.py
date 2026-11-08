import json
sauvegarde = {
    "joueur": "Alex",
    "points_de_vie": 85,
    "niveau": 3,
    "objets": ["potion", "bouclier"]
}

with open ("sauvegarde.json", "w") as f:
    json.dump(sauvegarde, f, ensure_ascii=False)
