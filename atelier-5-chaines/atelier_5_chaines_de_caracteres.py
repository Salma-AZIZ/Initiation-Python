
# Atelier 5 : Opérations sur les chaînes de caractères

def inverser_chaine(chaine):
    """Retourne la chaîne inversée."""
    return chaine[::-1]

def compter_voyelles(chaine):
    """Compte le nombre de voyelles dans la chaîne."""
    voyelles = "aeiouyAEIOUY"
    return sum(1 for c in chaine if c in voyelles)

def remplacer_caractere(chaine, ancien, nouveau):
    """Remplace toutes les occurrences d’un caractère par un autre."""
    return chaine.replace(ancien, nouveau)

def concatener(chaine1, chaine2):
    """Concatène deux chaînes et les retourne."""
    return chaine1 + chaine2

# Exemples de test
if __name__ == "__main__":
    exemple = "Bonjour Python"
    print("Chaîne originale :", exemple)
    print("Chaîne inversée :", inverser_chaine(exemple))
    print("Nombre de voyelles :", compter_voyelles(exemple))
    print("Remplacer o par a :", remplacer_caractere(exemple, 'o', 'a'))
    print("Concaténation avec ' !' :", concatener(exemple, " !"))
