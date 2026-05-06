"""Reto 2: Revisar dimension y forma

Objetivo:
- Leer shape, ndim y dtype de una matriz.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "matriz_2x3.csv"
matrix = np.loadtxt(data_file, delimiter=",", dtype=int)

print(matrix.shape)
print(matrix.ndim)
print(matrix.dtype)