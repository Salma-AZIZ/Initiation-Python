
# Fonction utilisant une boucle for
def somme_carres_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

# Fonction utilisant une boucle while
def somme_carres_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i ** 2
        i += 1
    return total

# Fonction utilisant la récursivité
def somme_carres_recursive(n):
    if n == 1:
        return 1
    return n ** 2 + somme_carres_recursive(n - 1)

# Test des trois fonctions
if __name__ == "__main__":
    n = 10
    print("Somme des carrés de 1 à", n, "avec boucle for :", somme_carres_for(n))
    print("Somme des carrés de 1 à", n, "avec boucle while :", somme_carres_while(n))
    print("Somme des carrés de 1 à", n, "avec récursivité :", somme_carres_recursive(n))
