
from calculatrice_scientifique import CalculatriceScientifique

# Exemple d'utilisation
calc = CalculatriceScientifique()
print(calc.addition(10, 5))
print(calc.racine(16))
print(calc.puissance(2, 3))

# Polymorphisme
def appliquer_operation(operation_obj, a, b):
    return operation_obj(a, b)

print(appliquer_operation(calc.addition, 3, 7))

print("Afficher l'historique :", calc.afficher_historique())

# Introspection
print("Attributs de calc :", dir(calc))
