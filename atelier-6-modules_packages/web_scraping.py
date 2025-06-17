import web_utils

url = "https://www.python.org"
contenu = web_utils.recuperer_html(url)
titres = web_utils.extraire_titres(contenu)

for titre in titres:
    print("- " + titre)
