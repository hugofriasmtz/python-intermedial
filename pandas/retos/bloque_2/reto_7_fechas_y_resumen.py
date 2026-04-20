"""Reto 7: Fechas y resumen mensual

Objetivo:
- Convertir una columna a fecha y resumir por mes.

Instrucciones:
1) Crea el DataFrame con columna `fecha` y `monto`.
2) Convierte `fecha` a tipo datetime.
3) Crea una columna `mes` a partir de la fecha.
4) Resume el monto total por mes.
5) Ordena el resultado por mes.
"""

import pandas as pd

data = {
    "fecha": ["2026-01-05", "2026-01-20", "2026-02-10", "2026-02-28", "2026-03-03", "2026-03-25"],
    "monto": [120, 180, 200, 150, 300, 220]
}

df = pd.DataFrame(data)
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M").astype(str)

resumen_mensual = (
    df.groupby("mes", as_index=False)["monto"]
    .sum()
    .sort_values(by="mes", ascending=True)
)

print("DataFrame original:")
print(df)
print("\nResumen mensual de montos:")
print(resumen_mensual)
