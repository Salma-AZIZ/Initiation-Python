from gestion_bibliotheque import Livre, Utilisateur, Bibliotheque

# Création de la bibliothèque
biblio = Bibliotheque("Centrale")

# Ajout de livres
livre1 = Livre("1984", "George Orwell")
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)

# Création d’un utilisateur
utilisateur = Utilisateur("Alice")

# Emprunter un livre
utilisateur.emprunter_livre(livre1)

# Affichage
print("\nLivres empruntés :")
utilisateur.afficher_livres_empruntes()

# Introspection
print("\nIntrospection sur l'utilisateur :")
print("Attributs :", dir(utilisateur))
