"""Reto 7: Valores nulos basicos

Objetivo:
- Detectar y tratar valores faltantes de forma inicial.

Instrucciones:
1) Crea un DataFrame con algunos valores None.
2) Revisa que datos faltan con isna().
3) Cuenta nulos por columna.
4) Rellena nulos de una columna numerica con un valor fijo.
5) Opcional: elimina filas con nulos.
"""

import pandas as pd

data = {
    "nombre": ["Ana", "Luis", "Carla", "Pedro"],
    "edad": [24, None, 29, None],
    "ciudad": ["Bogota", "Quito", None, "Santiago"]
}

df = pd.DataFrame(data)

# TODO: revisar nulos con isna()
# TODO: contar nulos por columna
# TODO: rellenar nulos en edad
# TODO: (opcional) eliminar filas con nulos
