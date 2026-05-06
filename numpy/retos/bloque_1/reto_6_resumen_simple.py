"""Reto 6: Resumen simple

Objetivo:
- Calcular maximo, minimo y promedio de un arreglo numerico.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "puntajes.csv"
scores = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=int)

average_score = scores.mean()

print(scores.max())
print(scores.min())
print(average_score)
print(np.sum(scores > average_score))