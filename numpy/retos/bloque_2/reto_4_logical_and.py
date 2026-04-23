"""Reto 4: Filtrar con logical_and

Objetivo:
- Combinar dos condiciones que deben cumplirse al mismo tiempo.

Instrucciones:
1) Crea un arreglo con edades.
2) Crea una mascara para seleccionar edades entre 18 y 30 (incluyendo ambos extremos).
3) Imprime la mascara booleana.
4) Imprime solo las edades filtradas.
"""

import numpy as np

# TODO: crea el arreglo de edades
ages = np.array([15, 18, 21, 29, 30, 34, 40])

# TODO: combina dos condiciones con logical_and
# Significa: edad mayor o igual a 18 Y menor o igual a 30
young_adults = np.logical_and(ages >= 18, ages <= 30)

# TODO: imprime la mascara
print(young_adults)

# TODO: imprime solo las edades que cumplen ambas condiciones
print(ages[young_adults])

# GLOSARIO
# - np.logical_and(a, b): devuelve True solo donde a y b son True.
# - mascara booleana: arreglo de True y False para filtrar valores.