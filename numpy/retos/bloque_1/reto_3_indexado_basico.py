"""Reto 3: Indexado basico

Objetivo:
- Practicar como seleccionar posiciones especificas dentro de un arreglo.

Instrucciones:
1) Crea un arreglo con al menos 6 numeros.
2) Imprime el primer y el ultimo elemento.
3) Imprime un corte con los elementos del indice 1 al 3.
4) Imprime el elemento de la posicion 2.
"""

import numpy as np

# TODO: crea un arreglo con varios numeros
values = np.array([10, 20, 30, 40, 50, 60])

# TODO: imprime el primer elemento
print(values[0])

# TODO: imprime el ultimo elemento usando indice negativo
print(values[-1])

# TODO: imprime un slice del arreglo
print(values[1:4])

# TODO: imprime el elemento de la posicion 2
print(values[2])

# GLOSARIO
# - indice 0: primer elemento.
# - indice negativo: cuenta desde el final.
# - slice 1:4: toma desde 1 hasta antes de 4.