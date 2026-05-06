"""Reto 4: Operaciones vectorizadas

Objetivo:
- Aplicar una operacion a todos los elementos de un arreglo al mismo tiempo.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "precios.csv"
prices = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=float)

# Suma un impuesto del 16% de forma vectorizada
prices_with_tax = prices * 1.16

print(prices)
print(prices_with_tax)
print(prices_with_tax - prices)