import pandas as pd
df = pd.read_csv('data/ventes.csv')
print(df)
print(
    df.head()
)
CA_total = sum(df["quantite"] * df["prix_unitaire"])
print(CA_total)
print("Ceci est une amélioration")
quantite_total = sum(df["quantite"])
print("La quantite totale restante est de", quantite_total)