panier = [19.99, "gratuit", 5.50, 42, None, 10.0]


def calculer_total(prix_articles):
    somme = 0
    for n in prix_articles:
        if isinstance(n, (int, float)):
            somme += n
    return somme

print(calculer_total(panier))
