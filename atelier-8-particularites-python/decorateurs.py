def decorateur_journalisation(fonction):
    def fonction_modifiee(*args, **kwargs):
        print(f"[LOG] Appel de {fonction.__name__} avec les arguments {args} {kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"[LOG] {fonction.__name__} a retourné {resultat}")
        return resultat
    return fonction_modifiee

@decorateur_journalisation
def multiplication(a, b):
    return a * b

# Test du décorateur
print("Résultat final :", multiplication(3, 4))
