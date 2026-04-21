"""Reto 2: Revisar dimension y forma

Objetivo:
- Aprender a leer la forma de un arreglo y su cantidad de dimensiones.

Instrucciones:
1) Crea un arreglo de dos filas y tres columnas.
2) Imprime su shape.
3) Imprime su ndim.
4) Imprime su dtype.
"""

import numpy as np

# TODO: crea una matriz simple de 2x3
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# TODO: imprime la forma del arreglo
print(matrix.shape)

# TODO: imprime cuantas dimensiones tiene
print(matrix.ndim)

# TODO: imprime el tipo de datos almacenado
print(matrix.dtype)

# GLOSARIO
# - shape: indica filas y columnas.
# - ndim: indica el numero de dimensiones.
# - dtype: indica el tipo de dato interno.