import pandas as pd

# Leer histórico original

df = pd.read_csv("historico_baloto_revancha_2017_2026.csv")

# Filtrar únicamente Baloto

df = df[df["Tipo_Sorteo"] == "Baloto"]

# Renombrar columnas

df = df.rename(columns={
"Fecha": "draw_date",
"B1": "n1",
"B2": "n2",
"B3": "n3",
"B4": "n4",
"B5": "n5",
"Super_Balota": "superbalota"
})

# Seleccionar columnas finales

df = df[
[
"draw_date",
"n1",
"n2",
"n3",
"n4",
"n5",
"superbalota"
]
]

# Crear CSV compatible con Lottery Analytics

df.to_csv(
"data/baloto_seed.csv",
index=False
)

print("CSV convertido correctamente")
print("Total sorteos:", len(df))
