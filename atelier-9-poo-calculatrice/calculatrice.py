
class Calculatrice:
    def __init__(self):
        self._historique = []

    def addition(self, a, b):
        resultat = a + b
        self._ajouter_historique(f"Addition: {a} + {b} = {resultat}")
        return resultat

    def soustraction(self, a, b):
        resultat = a - b
        self._ajouter_historique(f"Soustraction: {a} - {b} = {resultat}")
        return resultat

    def multiplication(self, a, b):
        resultat = a * b
        self._ajouter_historique(f"Multiplication: {a} * {b} = {resultat}")
        return resultat

    def division(self, a, b):
        if b == 0:
            self._ajouter_historique("Erreur: Division par zéro")
            return "Erreur : Division par zéro."
        resultat = a / b
        self._ajouter_historique(f"Division: {a} / {b} = {resultat}")
        return resultat

    def _ajouter_historique(self, operation):
        self._historique.append(operation)

    def afficher_historique(self):
        return self._historique
