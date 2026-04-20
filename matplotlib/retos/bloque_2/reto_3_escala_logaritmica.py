"""Reto 3: Escala logaritmica

Objetivo:
- Mostrar datos que crecen mucho usando una escala logaritmica.

Instrucciones:
1) Grafica los datos dados.
2) Cambia el eje X o Y a escala logaritmica.
3) Agrega titulo y etiquetas claras.
4) Observa como cambia la lectura de los datos.

Pista:
- Este tipo de escala sirve cuando los valores aumentan muy rapido.
"""

import matplotlib.pyplot as plt

anio = [1, 2, 3, 4, 5, 6]
usuarios = [10, 100, 1000, 10000, 100000, 1000000]

plt.figure(figsize=(8, 4.5))
plt.plot(anio, usuarios, marker="o", color="tab:purple")
plt.yscale("log")

plt.title("Crecimiento de usuarios (escala logaritmica)")
plt.xlabel("Anio")
plt.ylabel("Usuarios")
plt.grid(alpha=0.3, which="both")
plt.show()
