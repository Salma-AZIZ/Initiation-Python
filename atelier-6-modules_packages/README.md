
# Atelier 6 : Modules et packages

## Objectifs
- Utiliser des modules standards (`requests`) et externes (`beautifulsoup4`)
- Structurer le code Python en modules séparés
- Automatiser une extraction de contenu HTML

## Instructions

1. Installez les bibliothèques nécessaires :

```
pip install requests beautifulsoup4
```

2. Lancez le fichier `web_scraping.py`. Il s'appuie sur `web_utils.py`, qui contient deux fonctions :
- `recuperer_html(url)`: récupère le contenu HTML d’une page web
- `extraire_titres(html)`: extrait tous les titres `<h2>`

## Contenu

- `web_scraping.py` : script principal
- `web_utils.py` : module utilitaire
- `atelier_6_modules_packages.ipynb` : version Notebook commentée

## Résultat attendu

Le script doit afficher une liste de titres extraits de la page web ciblée.
