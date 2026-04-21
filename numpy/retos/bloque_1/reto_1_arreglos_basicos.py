"""Reto 1: Crear arreglos basicos con NumPy

Objetivo:
- Entender como pasar de listas de Python a arreglos de NumPy.

Instrucciones:
1) Importa NumPy.
2) Crea un arreglo con numeros del 1 al 5.
3) Imprime el arreglo y su tipo.
4) Imprime la cantidad de elementos que tiene.
"""

import numpy as np

# TODO: crea el arreglo a partir de una lista normal
numbers = np.array([1, 2, 3, 4, 5])

# TODO: imprime el arreglo para ver su contenido
print(numbers)

# TODO: imprime el tipo de dato de la variable
print(type(numbers))

# TODO: imprime el numero total de elementos
print(numbers.size)

# GLOSARIO
# - np.array(): convierte una lista en un arreglo de NumPy.
# - type(): muestra el tipo de la variable.
# - size: indica cuantos elementos tiene el arreglo.