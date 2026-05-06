"""Reto 4: Filtrar con logical_and

Objetivo:
- Combinar dos condiciones que deben cumplirse al mismo tiempo.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "edades.csv"
ages = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=int)

young_adults = np.logical_and(ages >= 18, ages <= 30)

print(young_adults)
print(ages[young_adults])