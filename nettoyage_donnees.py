import pandas as pd

df = pd.read_csv("data/ventes.csv")
print(f"Nombre de lignes : {df.shape[0]}")
print(f"Nombre de colonnes : {df.shape[1]}")