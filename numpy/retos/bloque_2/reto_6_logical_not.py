"""Reto 6: Invertir condiciones con logical_not

Objetivo:
- Obtener el complemento de una condicion booleana.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "temperaturas.csv"
temperatures = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=int)

hot_days = temperatures >= 30
not_hot_days = np.logical_not(hot_days)

print(hot_days)
print(not_hot_days)
print(temperatures[not_hot_days])