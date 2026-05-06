"""Reto 1: Operaciones vectorizadas

Objetivo:
- Aplicar una operacion a todos los elementos a la vez.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "precios.csv"
prices = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=float)

prices_with_tax = prices * 1.16

print(prices)
print(prices_with_tax)
print(prices_with_tax - prices)