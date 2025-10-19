
import pandas as pd
import matplotlib.pyplot as plt

# Données
data = {
    "Annee": list(range(2010, 2025)),
    "Inflation": [1.7, 2.0, 1.5, 0.8, 0.5, 0.2, 0.3, 1.0, 1.8, 0.5, 0.9, 1.6, 5.2, 4.9, 3.2],
    "Chomage":   [9.5, 9.2, 9.8, 10.2, 10.0, 9.9, 9.4, 8.9, 8.5, 8.1, 7.8, 7.3, 7.1, 7.4, 7.5]
}

df = pd.DataFrame(data)

# Tableau propre
print("\n=== Aperçu du jeu de données ===\n")
print(df.to_string(index=False))

# Graphique avec deux axes
fig, ax1 = plt.subplots(figsize=(7,4))

# Axe gauche : inflation
ax1.set_xlabel("Année")
ax1.set_ylabel("Inflation (%)", color="tab:blue")
ax1.plot(df["Annee"], df["Inflation"], color="tab:blue", marker="o", label="Inflation")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Axe droit : chômage
ax2 = ax1.twinx()
ax2.set_ylabel("Chômage (%)", color="tab:red")
ax2.plot(df["Annee"], df["Chomage"], color="tab:red", marker="s", label="Chômage")
ax2.tick_params(axis="y", labelcolor="tab:red")

plt.title("Évolution Inflation et Chômage en France (2010–2024)")
plt.grid(True)
fig.tight_layout()
plt.show()
plt.savefig("inflation_chomage.png", dpi=300)

# Corrélation
corr = df["Inflation"].corr(df["Chomage"])
print(f"\nCorrélation Inflation/Chômage = {corr:.2f}")