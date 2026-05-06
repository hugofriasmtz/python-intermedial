"""Reto 5: Filtrar con logical_or

Objetivo:
- Seleccionar valores que cumplen al menos una condicion.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "puntajes_extremos.csv"
scores = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=int)

extreme_scores = np.logical_or(scores < 50, scores > 90)

print(extreme_scores)
print(scores[extreme_scores])