def appliquer_operation_sur_liste(fonction, liste):
    """Applique une fonction donnée à chaque élément de la liste."""
    return [fonction(x) for x in liste]

# Exemple d'utilisation
def doubler(x):
    return x * 2

nombres = [1, 2, 3, 4, 5]
resultats = appliquer_operation_sur_liste(doubler, nombres)
print("Résultats de l'application de la fonction:", resultats)
