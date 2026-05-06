"""Reto 3: Indexado basico

Objetivo:
- Practicar indices positivos, negativos y slices.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "secuencia_6.csv"
values = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=int)

print(values[0])
print(values[-1])
print(values[1:4])
print(values[2])