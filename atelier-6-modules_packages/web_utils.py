import requests
from bs4 import BeautifulSoup

def recuperer_html(url):
    """Effectue une requête HTTP GET sur l'URL et retourne le contenu HTML."""
    reponse = requests.get(url)
    return reponse.text

def extraire_titres(html):
    """Extrait les titres h2 de la page HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    return [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
