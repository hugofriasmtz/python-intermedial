"""Reto 1: Operaciones vectorizadas

Objetivo:
- Ver como NumPy aplica una operacion a todos los elementos a la vez.

Instrucciones:
1) Crea un arreglo con precios base.
2) Suma un impuesto del 16% a todos los valores.
3) Imprime ambos arreglos.
4) Imprime el incremento total de cada precio.
"""

import numpy as np

# TODO: crea el arreglo de precios
prices = np.array([100, 250, 400, 800])

# TODO: aplica el aumento de forma vectorizada
prices_with_tax = prices * 1.16

# TODO: imprime el arreglo original
print(prices)

# TODO: imprime el arreglo con impuesto
print(prices_with_tax)

# TODO: calcula cuanto aumento cada precio
print(prices_with_tax - prices)

# GLOSARIO
# - vectorizada: la operacion se aplica a todo el arreglo al mismo tiempo.
# - 1.16: equivale a 100% + 16%.