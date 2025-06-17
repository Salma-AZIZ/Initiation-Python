
from calculatrice import Calculatrice
import math

class CalculatriceScientifique(Calculatrice):
    def puissance(self, a, b):
        resultat = math.pow(a, b)
        self._ajouter_historique(f"Puissance: {a}^{b} = {resultat}")
        return resultat

    def racine(self, a):
        resultat = math.sqrt(a)
        self._ajouter_historique(f"Racine: √{a} = {resultat}")
        return resultat
