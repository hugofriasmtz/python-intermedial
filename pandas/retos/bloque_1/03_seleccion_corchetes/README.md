# 03 - Seleccion con Corchetes, loc e iloc

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **extraer datos específicos** de un DataFrame respondiendo preguntas prácticas:

- **¿Cómo extraigo una columna entera?** → corchetes `df["col"]`
- **¿Cómo extraigo varias columnas a la vez?** → corchetes dobles `df[[...]]`
- **¿Cómo accedo a una fila por su etiqueta (nombre del índice)?** → `.loc`
- **¿Cómo accedo a una fila por su posición numérica?** → `.iloc`

> [!IMPORTANT]
> Evita `df["columna"] = ...` en bucles sin conocer el comportamiento de copia/vista; puede ser ineficiente.

---

## Que vas a aprender

- Por qué una columna devuelve una `Series` pero varias devuelven un `DataFrame`.
- La diferencia crítica: `.loc` usa etiquetas, `.iloc` usa posiciones.
- Por qué `.loc[1:3]` incluye 3 pero `.iloc[1:3]` no (comportamiento inclusivo vs exclusivo).
- Cuándo cada método es la mejor opción.

---

## 1. Corchetes para columnas

Los corchetes se usan cuando quieres trabajar con columnas concretas. Es la forma más directa de decir: "quiero esta información".

Primero, creamos nuestro DataFrame de ejemplo:

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "puesto": ["Programador", "Administradora", "Backend", "Frontend", "Constructor", "Ama de casa"],
    "salario": [4500, 3200, 3800, 3500, 2800, 3100],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "años_experiencia": [8, 5, 3, 6, 4, 7]
})
```

Ahora, seleccionemos columnas:

```python
print(df["nombre"])
# Output:
# 0       Hugo
# 1      Karen
# 2     Marcos
# 3      Erwin
# 4     Felipe
# 5   Catalina

print(df[["nombre", "puesto", "salario"]])
# Output:
#    nombre       puesto         salario
# 0    Hugo      Programador       4500
# 1   Karen   Administradora       3200
# 2  Marcos         Backend       3800
# 3   Erwin       Frontend       3500
# 4  Felipe      Constructor       2800
# 5 Catalina     Ama de casa       3100
```

### Cuándo usarlo

- Cuando quieres columnas específicas.
- Cuando quieres reducir ruido.
- Cuando necesitas una sola columna como `Series`.

### Qué devuelve

- `df["nombre"]` devuelve una columna individual (tipo `Series`).
- `df[["nombre", "puesto", "salario"]]` devuelve una tabla con esas columnas (tipo `DataFrame`).

---

## 2. loc e iloc

`.loc` y `.iloc` sirven para obtener filas. La diferencia es que una piensa en **etiquetas** y la otra en **posiciones**.

```python
# Usando el mismo DataFrame de empleados:

# .loc: por etiqueta de índice
print(df.loc[1])
# Output:
# nombre              Karen
# puesto           Analista
# salario              3200
# ciudad    Ciudad de México
# años_experiencia        5

# .iloc: por posición
print(df.iloc[1])
# Output: (mismo resultado, pero por posición)

# Rango con .loc (inclusive en ambos lados):
print(df.loc[1:3])
# Output: filas con etiqueta 1, 2, 3

# Rango con .iloc (exclusive en el final):
print(df.iloc[1:3])
# Output: filas en posiciones 1 y 2 (no incluye 3)
```

> [!WARNING]
> Evita el 'chained indexing' (`df[a][b] = value`) porque puede producir `SettingWithCopyWarning`; usa `.loc` para asignaciones seguras.

### Diferencia

- `.loc` trabaja con etiquetas del índice.
- `.iloc` trabaja con posiciones numéricas.
- `.loc` **incluye** el final del rango: `df.loc[1:3]` devuelve etiquetas 1, 2, 3.
- `.iloc` **excluye** el final del rango: `df.iloc[1:3]` devuelve posiciones 1, 2 (no 3).

### Resultado esperado

- `df.loc[1]` devuelve la fila con etiqueta 1 (la segunda fila).
- `df.loc[1:3]` devuelve filas desde la etiqueta 1 hasta la 3 (inclusive).
- `df.iloc[1]` devuelve la fila en posición 1 (la segunda fila).
- `df.iloc[1:3]` devuelve las filas en posiciones 1 y 2.

**Documentación:** [Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)

---

## 3. Mini practica

- Selecciona una columna.
- Selecciona 3 columnas.
- Selecciona las primeras 3 filas con `.iloc`.
- Cambia el índice y prueba `.loc`.

---

## Errores comunes

- Pensar que `.loc[1:4]` y `.iloc[1:4]` hacen lo mismo.
- Confundir filas con columnas.
- Intentar usar `.iloc` con nombres de etiquetas.
