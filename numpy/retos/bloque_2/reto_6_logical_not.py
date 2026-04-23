"""Reto 6: Invertir condiciones con logical_not

Objetivo:
- Aprender a invertir una condicion booleana para obtener su complemento.

Instrucciones:
1) Crea un arreglo con temperaturas.
2) Crea una mascara para dias calurosos (>= 30).
3) Invierte esa mascara con logical_not para obtener dias no calurosos.
4) Imprime las dos mascaras y los valores no calurosos.
"""

import numpy as np

# TODO: crea el arreglo de temperaturas
temperatures = np.array([22, 27, 30, 33, 25, 31, 19])

# TODO: crea la condicion base
hot_days = temperatures >= 30

# TODO: invierte la condicion
# Significa: seleccionar todo lo que NO sea dia caluroso
not_hot_days = np.logical_not(hot_days)

# TODO: imprime las mascaras para comparar
print(hot_days)
print(not_hot_days)

# TODO: imprime solo las temperaturas no calurosas
print(temperatures[not_hot_days])

# GLOSARIO
# - np.logical_not(a): invierte True por False y False por True.
# - complemento: conjunto contrario al de la condicion original.