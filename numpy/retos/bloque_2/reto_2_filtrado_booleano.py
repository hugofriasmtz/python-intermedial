"""Reto 2: Filtrado booleano

Objetivo:
- Seleccionar solo los valores que cumplen una condicion.

Instrucciones:
1) Crea un arreglo con temperaturas.
2) Crea una mascara para detectar valores mayores o iguales a 30.
3) Imprime la mascara.
4) Imprime solo las temperaturas calientes.
"""

import numpy as np

# TODO: crea el arreglo de temperaturas
temperatures = np.array([24, 28, 30, 31, 22, 35, 29])

# TODO: crea la condicion booleana
hot_days = temperatures >= 30

# TODO: imprime la mascara booleana
print(hot_days)

# TODO: imprime solo las temperaturas que cumplen la condicion
print(temperatures[hot_days])

# GLOSARIO
# - mascara booleana: arreglo de True y False.
# - filtrado booleano: selecciona solo los valores True.