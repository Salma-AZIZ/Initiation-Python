# Importer un module Python depuis un chemin externe

## ✅ Importer un module situé ailleurs (chemin externe)

```python
import sys  # Permet d'accéder à la liste des chemins d'importation (sys.path)
sys.path.insert(0, "/chemin/absolu/vers/le/dossier")  # Ajoute un chemin personnalisé en tête de la liste
import mon_module  # Importe le module situé dans le dossier ajouté
```

### 🧪 Exemple :

```python
sys.path.insert(0, "/home/user/Téléchargements")
import mon_module
mon_module.ma_fonction()
```

---

## 📋 Que contient `sys.path` ?

`sys.path` est une **liste ordonnée** des chemins que Python explore pour chercher les modules.  
Elle contient généralement :

- Le dossier courant (`''`)
- Le dossier où se trouve le script exécuté
- Les chemins système (`/usr/lib/python3.X`, etc.)
- Le dossier des packages installés (`site-packages`)
- Les chemins ajoutés manuellement via :
  - `sys.path.insert()`
  - ou la variable d’environnement `PYTHONPATH`

---

## 🖨️ Afficher les chemins de recherche (`sys.path`)

```python
import sys
print(sys.path)  # Affiche la liste complète
```

👉 Pour un affichage plus lisible :

```python
for chemin in sys.path:
    print(chemin)
```

---

## 🧭 Utiliser `os` pour explorer l'environnement d'exécution

```python
import os

# Répertoire de travail actuel
print("Répertoire d'exécution :", os.getcwd())

# Obtenir le chemin absolu d'un dossier relatif
chemin_absolu = os.path.abspath("mon_dossier")
print("Chemin absolu :", chemin_absolu)

# Ajouter dynamiquement un dossier dans sys.path
import sys
sys.path.insert(0, chemin_absolu)
```

---

## ⚠️ Inconvénients de cette méthode (`sys.path.insert`)

- ❌ Peu maintenable : les chemins sont codés en dur.
- ⚠️ Non portable : dépend de l’environnement local.
- ❗ Risque de conflits si un fichier a le même nom qu’un module standard (`random.py`, `math.py`, etc.).
- 💡 Pas recommandé pour des projets partagés ou en production.

---

## ✅ Bonne pratique recommandée

Organiser ses modules dans un sous-dossier de projet (ex : `libs/`) et utiliser :

```python
from libs import mon_module
```

✔️ Lisible, portable, structuré et maintenable à long terme.
