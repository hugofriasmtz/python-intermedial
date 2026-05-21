"""Reto 2: Rango y dispersion

Objetivo:
- Medir que tan separados estan los datos usando varianza y desviacion estandar.

Instrucciones:
1) Carga el CSV de jugadores.
2) Calcula min, max, var y std de goles.
3) Calcula min, max, var y std de valor_millones.
4) Imprime los resultados con una tabla sencilla o etiquetas claras.
"""

from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "pandas" / "jugadores_futbol.csv"
df = pd.read_csv(csv_path)

resumen = pd.DataFrame(
    {
        "goles": {
            "min": df["goles"].min(),
            "max": df["goles"].max(),
            "var": df["goles"].var(),
            "std": df["goles"].std(),
        },
        "valor_millones": {
            "min": df["valor_millones"].min(),
            "max": df["valor_millones"].max(),
            "var": df["valor_millones"].var(),
            "std": df["valor_millones"].std(),
        },
    }
)

print("Resumen de rango y dispersion:")
print(resumen)
