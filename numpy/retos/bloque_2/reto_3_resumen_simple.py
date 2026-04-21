"""Reto 3: Resumen simple de datos

Objetivo:
- Practicar calculos basicos con un arreglo de NumPy.

Instrucciones:
1) Crea un arreglo con notas de examenes.
2) Imprime la nota maxima, minima y el promedio.
3) Imprime cuantas notas estan por encima del promedio.
4) Explica con comentarios por que cada operacion es util.
"""

import numpy as np

# TODO: crea el arreglo con notas
scores = np.array([65, 70, 72, 88, 90, 75, 80])

# TODO: calcula y muestra la nota mas alta
print(scores.max())

# TODO: calcula y muestra la nota mas baja
print(scores.min())

# TODO: calcula y muestra el promedio
average_score = scores.mean()
print(average_score)

# TODO: cuenta cuantas notas superan el promedio
print(np.sum(scores > average_score))

# GLOSARIO
# - max(): devuelve el valor mas alto.
# - min(): devuelve el valor mas bajo.
# - mean(): calcula el promedio.
# - np.sum(condicion): cuenta cuantas veces la condicion es True.