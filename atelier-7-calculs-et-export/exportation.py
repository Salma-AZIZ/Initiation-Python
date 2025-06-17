import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Données fictives : Simulation des données d’un test de logique chronométré (score et temps par participant).
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Score': [85, 92, 78, 90],
    'Temps (s)': [34.5, 29.3, 45.6, 31.2]
}
df = pd.DataFrame(data)

# Export CSV
df.to_csv("resultats.csv", index=False)

# Export Excel
df.to_excel("resultats.xlsx", index=False)

# Graphique
plt.figure(figsize=(6, 4))
plt.bar(df['Nom'], df['Score'], color='skyblue')
plt.title("Scores des participants")
plt.xlabel("Nom")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("graphique.png")
plt.close()

# Rapport PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Rapport d'Analyse des Scores", ln=True, align='C')
pdf.ln(10)
pdf.multi_cell(0, 10, txt=(
    "Ce rapport présente les résultats d'une analyse simple des scores obtenus par quatre participants.\n"
    "Résumé :\n"
    f" - Score moyen : {df['Score'].mean():.2f}\n"
    f" - Score maximal : {df['Score'].max()}\n"
    f" - Score minimal : {df['Score'].min()}\n"
))
pdf.image("graphique.png", x=30, w=150)
pdf.output("rapport_resultats.pdf")

# Message de confirmation
print("Exportation des fichiers réussie avec succès.")
