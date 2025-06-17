# 🧩 Atelier 10 — Projet Final Python

Bienvenue dans le dernier atelier de la formation ! Cet exercice est une **synthèse complète** de tout ce que vous avez appris jusqu'ici.

---

## 🎯 Objectif du projet

Créer un projet Python complet en manipulant un **jeu de données réel** (ou simulé), de l'exploration initiale à l'export des résultats, tout en structurant votre code de manière professionnelle.

---

## 🧠 Compétences mobilisées

- Chargement et nettoyage de données avec `pandas`
- Analyse descriptive et visualisation (`matplotlib`, `seaborn`)
- Exportation des résultats dans différents formats : CSV, Excel, PDF
- Création de fonctions et modules réutilisables
- Structuration du code avec la Programmation Orientée Objet
- Packaging du projet avec `setuptools` ou `poetry`

---

## 🗂 Structure recommandée

Organisez vos projets dans des dossiers clairs :

```
atelier-10-projet-final/
│
├── ressources/                       # Fichiers complémentaires (proposition de datasets, doc technique…)
│   ├── proposition_datasets.md
│   └── tuto_packaging.md
│
├── employes_analyse_setuptools/     # Exemple complet avec setuptools
│   ├── analyse_employes/
│   ├── setup.py
│   ├── main.py
│   ├── employes_dataset.csv
│   └── README.md
│
├── employes_analyse_poetry/         # Même projet mais packagé avec poetry
│   ├── analyse_employes/
│   ├── pyproject.toml
│   ├── main.py
│   ├── employes_dataset.csv
│   └── README.md
│
└── projet_final_nomprenom/          # Dossier de votre projet final à remettre
```

---

## 📎 Remarques

- Le fichier `proposition_datasets.md` dans le dossier `/ressources` vous propose des jeux de données si vous n’en avez pas.
- Le fichier `tuto_packaging.md` dans le même dossier explique pas à pas comment transformer votre projet en package Python.
- Chaque sous-projet possède son propre `README.md` avec instructions spécifiques.
- Vous pouvez vous inspirer des exemples fournis mais **le projet final doit refléter votre propre réflexion**.

---

Bon courage, et surtout, prenez plaisir à montrer tout ce que vous avez appris ! 🚀
