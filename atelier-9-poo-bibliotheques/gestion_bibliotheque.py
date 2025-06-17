class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._emprunte = False

    def afficher_info(self):
        return f"{self._titre} par {self._auteur}"

    def emprunter(self):
        if not self._emprunte:
            self._emprunte = True
            return True
        return False

    def est_emprunte(self):
        return self._emprunte


class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres.append(livre)
            print(f"{self.nom} a emprunté : {livre.afficher_info()}")
        else:
            print(f"Le livre {livre.afficher_info()} est déjà emprunté.")

    def afficher_livres_empruntes(self):
        for livre in self.livres:
            print(livre.afficher_info())


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self._livres = []

    def ajouter_livre(self, livre):
        self._livres.append(livre)

    def lister_livres(self):
        for livre in self._livres:
            print(livre.afficher_info())
