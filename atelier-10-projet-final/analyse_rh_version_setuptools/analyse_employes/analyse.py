import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

# Chargement du dataset
df = pd.read_csv("employes_dataset.csv")  # Lecture du fichier CSV contenant les données des employés

# --- 1. Exploration des données ---
print("Aperçu du jeu de données :")
print(df.head())  # Affiche les premières lignes du dataset
print(df.info())  # Affiche les types de données et valeurs manquantes

# --- 2. Nettoyage & Transformation ---
df = df.dropna()  # Suppression des lignes avec valeurs manquantes
df["Salaire_normalise"] = (df["Salaire"] - df["Salaire"].mean()) / df["Salaire"].std()  # Normalisation du salaire
df["Anciennete_doublee"] = df["Anciennete"].apply(lambda x: x * 2)  # Nouvelle colonne dérivée

# Sauvegarde du fichier nettoyé
df.to_csv("employes_transforme.csv", index=False)

# --- 3. Analyse statistique ---
print("Statistiques descriptives :")
print(df.describe())  # Résumé statistique des variables numériques

# --- 4. Visualisation des corrélations ---
plt.figure(figsize=(6, 4))
corr = df[["Age", "Salaire", "Anciennete"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
plt.title("Corrélations entre âge, salaire, ancienneté")
plt.tight_layout()
plt.savefig("correlation.png")
plt.close()

# --- 5. Visualisation de la distribution des salaires ---
plt.figure(figsize=(6, 4))
sns.histplot(df["Salaire"], kde=True, color="skyblue", edgecolor='black')
plt.title("Distribution des salaires")
plt.xlabel("Salaire")
plt.ylabel("Nombre d'employés")
plt.tight_layout()
plt.savefig("distribution_salaires.png")
plt.close()

# --- 6. Export des résultats ---
df.to_csv("resultats.csv", index=False)
df.to_excel("resultats.xlsx", index=False)

# --- 7. Rapport PDF automatique ---
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Rapport d'analyse RH", ln=True, align='C')
pdf.ln(10)

# Données tabulaires
for i in range(len(df)):
    ligne = ", ".join([str(val) for val in df.iloc[i].values])
    pdf.cell(200, 10, txt=ligne, ln=True)

# Corrélation
pdf.add_page()
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Corrélations entre variables", ln=True, align='C')
pdf.image("correlation.png", x=15, y=30, w=180)

# Distribution
pdf.add_page()
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Distribution des salaires", ln=True, align='C')
pdf.image("distribution_salaires.png", x=15, y=30, w=180)

pdf.output("rapport.pdf")

# --- 8. Confirmation ---
print("✅ Analyse terminée et fichiers exportés :")
print("- employes_transforme.csv")
print("- resultats.csv / resultats.xlsx")
print("- rapport.pdf")
