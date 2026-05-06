"""Reto 1: Crear arreglos basicos con NumPy

Objetivo:
- Convertir datos simples en un arreglo de NumPy.
"""

from pathlib import Path

import numpy as np

data_file = Path(__file__).resolve().parents[3] / "data" / "numpy" / "numeros_base.csv"
numbers = np.loadtxt(data_file, delimiter=",", skiprows=1, dtype=int)

print(numbers)
print(type(numbers))
print(numbers.size)