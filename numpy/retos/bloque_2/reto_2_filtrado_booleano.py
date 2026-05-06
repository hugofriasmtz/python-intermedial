"""Reto 2: Filtrado booleano

Objetivo:
- Seleccionar solo los valores que cumplen una condicion.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "temperaturas.csv"
temperatures = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=int)

hot_days = temperatures >= 30

print(hot_days)
print(temperatures[hot_days])