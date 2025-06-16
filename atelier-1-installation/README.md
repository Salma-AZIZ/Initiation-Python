# 🐍 Atelier 1 – Installation d’un environnement Python et exécution d’un premier script

Bienvenue dans cet atelier d’introduction à Python !

Dans ce dossier, vous trouverez :
- Des instructions pour installer un environnement Python
- Votre tout premier script à créer et exécuter
- Une comparaison des outils que vous pouvez utiliser

---

## 🎯 Objectifs

- Installer un environnement de développement Python sur votre poste
- Écrire et exécuter un premier script `.py`
- Comprendre les différences entre les environnements de développement

---

## 🧩 Étape 1 – Installer un environnement Python

Vous avez plusieurs options. Choisissez celle qui vous semble la plus confortable :

### ✅ Option 1 : Anaconda (recommandée pour débuter en data science)

📌 **Avantages** :
- Python est déjà inclus
- Jupyter Notebook est intégré
- Facile à utiliser pour tester du code

🔗 [Télécharger Anaconda](https://www.anaconda.com/download)

🛠️ **Instructions** :
1. Choisissez votre système d’exploitation (Windows, macOS, Linux).
2. Lancez l’installation avec les options par défaut.
3. Une fois installé, ouvrez **Anaconda Navigator** ou **Jupyter Notebook**.

### ✅ Option 2 : VS Code + Python (léger et personnalisable)

📌 **Avantages** :
- Très rapide à installer
- Fonctionne pour tout type de projets (web, scripts, data...)

🔗 [Télécharger Python](https://www.python.org/downloads/)  
🔗 [Télécharger VS Code](https://code.visualstudio.com/)

🛠️ **Instructions** :
1. Installez **Python** (cochez “Add Python to PATH” lors de l’installation).
2. Installez **VS Code**.
3. Dans VS Code, installez l’extension “Python” dans l’onglet **Extensions**.
4. Créez un fichier `premier_script.py` et exécutez-le directement.

### ✅ Option 3 : PyCharm (complet et structuré)

📌 **Avantages** :
- Très bon pour projets complexes
- Gestion automatique des environnements

🔗 [Télécharger PyCharm Community](https://www.jetbrains.com/pycharm/download/)

🛠️ **Instructions** :
1. Téléchargez et installez PyCharm.
2. Créez un nouveau projet Python.
3. Un interpréteur Python est automatiquement installé si vous ne l'avez pas encore.

---

## 🧪 Étape 2 – Vérifier l’installation

Ouvrez un **terminal** ou **invite de commandes**, et tapez :

```bash
python --version
```

Vous devez voir une ligne comme :

```
Python 3.10.12
```

---

## 📝 Étape 3 – Écrire et exécuter un premier script

Créez un fichier nommé `premier_script.py` contenant :

```python
print("Bonjour, bienvenue dans le monde de Python !")
```

### ▶️ Pour l’exécuter via le terminal :

1. Ouvrez votre terminal ou invite de commande.
2. Naviguez jusqu’au dossier contenant le fichier avec `cd`.  
   Par exemple :
   ```bash
   cd C:\Utilisateurs\MonNom\Documents\FormationPython
   ```
3. Tapez la commande suivante :
   ```bash
   python premier_script.py
   ```

💡 Si vous utilisez VS Code ou PyCharm, vous pouvez aussi cliquer sur le bouton **"Run"** ou **"▶️"** dans l’éditeur.

---

## 📊 Étape 4 – Comparaison des environnements

| Critère                  | Anaconda                         | VS Code                              | PyCharm                               |
|--------------------------|----------------------------------|--------------------------------------|----------------------------------------|
| **Version de Python**    | Intégrée (à jour)                | À installer séparément               | Intégrée lors de la création du projet |
| **Installation**         | Facile, mais lourde (~3 Go)      | Très légère et rapide                | Moyennement lourde                     |
| **Éditeur de code**      | Basique (Jupyter)                | Avancé, personnalisable              | Très complet, orienté projet           |
| **Exécution du code**    | Par blocs (Jupyter)              | Terminal ou bouton "Run"             | Bouton "Run", gestionnaire d’erreurs   |
| **Gestion des packages** | Conda (graphique ou terminal)    | pip (terminal)                       | pip ou interface intégrée              |
| **Adapté aux débutants** | ✅ Très simple                    | ✅ Simple après configuration         | ⚠️ Moins intuitif pour débutants        |
| **Utilisation typique**  | Data science, IA, scripts courts | Développement général, scripts       | Projets logiciels structurés           |

---

## 📁 Contenu du dossier

```
atelier-1-installation/
│
├── premier_script.py        # Votre premier script Python
└── README.md                # Ce fichier avec toutes les explications
```

---

## 🎉 Bravo !

Vous venez d’écrire et d’exécuter votre tout premier programme Python !  
Nous allons maintenant découvrir la syntaxe de base du langage et manipuler des données.

```