import random

# --- Partie 1 : Listes et Tuples ---

# Création d'une liste de 10 nombres aléatoires entre 1 et 100
liste_nombres = [random.randint(1, 100) for _ in range(10)]
print("Liste de nombres :", liste_nombres)

# Calcul de la somme des éléments de la liste
somme = sum(liste_nombres)
print("Somme des éléments :", somme)

# Conversion en tuple
tuple_nombres = tuple(liste_nombres)

# Recherche du minimum et du maximum dans le tuple
min_val = min(tuple_nombres)
max_val = max(tuple_nombres)
print("Valeur minimale :", min_val)
print("Valeur maximale :", max_val)

# --- Partie 2 : Ensembles ---

ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

# Union
union = ensemble1 | ensemble2
print("Union :", union)

# Intersection
intersection = ensemble1 & ensemble2
print("Intersection :", intersection)

# Différence
difference = ensemble1 - ensemble2
print("Différence (ensemble1 - ensemble2) :", difference)

# --- Partie 3 : Dictionnaires ---

notes = {
    'Alice': 15,
    'Bob': 12,
    'Charlie': 17,
    'Diana': 14
}

# Calcul de la moyenne
moyenne = sum(notes.values()) / len(notes)
print("Moyenne des notes :", moyenne)

# Recherche de l'étudiant ayant la meilleure note
meilleur_etudiant = max(notes, key=notes.get)
print(f"L'étudiant ayant la meilleure note est {meilleur_etudiant} avec {notes[meilleur_etudiant]}")
