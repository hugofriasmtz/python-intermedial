"""Reto 5: Filtrar con logical_or

Objetivo:
- Seleccionar valores que cumplen al menos una condicion.

Instrucciones:
1) Crea un arreglo con puntajes.
2) Crea una mascara para seleccionar puntajes menores a 50 o mayores a 90.
3) Imprime la mascara booleana.
4) Imprime los puntajes extremos.
"""

import numpy as np

# TODO: crea el arreglo de puntajes
scores = np.array([35, 48, 52, 67, 75, 91, 96])

# TODO: combina condiciones con logical_or
# Significa: menor a 50 O mayor a 90
extreme_scores = np.logical_or(scores < 50, scores > 90)

# TODO: imprime la mascara
print(extreme_scores)

# TODO: imprime solo los puntajes que cumplen alguna de las dos condiciones
print(scores[extreme_scores])

# GLOSARIO
# - np.logical_or(a, b): devuelve True donde al menos una condicion es True.
# - caso extremo: aqui representa valores muy bajos o muy altos.