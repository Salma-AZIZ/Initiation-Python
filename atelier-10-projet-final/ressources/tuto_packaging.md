# 📦 Mini-Tuto : Packaging d’un projet Python

Le packaging permet de transformer un projet Python en une bibliothèque installable ou un produit distribuable. Cela facilite sa réutilisation, son partage et son installation.

---

## ✅ Version 1 : Packaging avec setuptools

### Étape 1 : Créer la structure du projet

Organisez vos fichiers comme ceci :

```
mon_projet/
│
├── analyse_employes/         # Le dossier contenant le code source
│   ├── __init__.py
│   └── analyse.py          
├── employes_dataset.csv      # Données utilisées
├── main.py                   # Point d’entrée du script
├── setup.py                  # Fichier de configuration setuptools
└── README.md                 # Documentation
```

### Étape 2 : Créer le fichier setup.py

```python
from setuptools import setup, find_packages

setup(
    name='analyse_employes',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'fpdf'
    ],
)
```

### Étape 3 : Installer le package localement

```bash
pip install .
```

Cela installe votre module `analyse_employes` comme un package utilisable dans vos scripts Python.

### Étape 4 : Exécuter le script principal

```python
from analyse_employes.analyse import *

print("Analyse RH démarrée.")
```

Exécution :

```bash
python main.py
```

### 💡 Remarques utiles :

Distribuez votre projet avec :

```bash
python setup.py sdist
```

Ou :

```bash
python setup.py bdist_wheel
```

---

## ✅ Version 2 : Packaging avec Poetry (gestion moderne)

### Étape 1 : Initialiser le projet

```bash
poetry init
```

### Étape 2 : Modifier le fichier pyproject.toml

```toml
[tool.poetry]
name = "analyse-employes"
version = "0.1.0"
description = "Analyse RH avec export CSV, Excel et PDF"
authors = ["Votre Nom <email@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
pandas = "^1.3.0"
matplotlib = "^3.4.0"
seaborn = "^0.11.0"
fpdf = "^1.7.2"
openpyxl = "^3.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### Étape 3 : Installer localement avec Poetry

```bash
poetry install
poetry run python main.py
```

---

## 🚀 Mise en production ou distribution

Distribuez un package avec :

```bash
# setuptools
python setup.py bdist_wheel

# poetry
poetry build
```

Intégrez-le ensuite dans vos scripts, notebooks ou pipelines (CI/CD, tests...).
