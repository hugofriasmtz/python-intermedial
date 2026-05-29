# 06 - Pivot Table

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **crear tablas cruzadas (pivot tables)** para responder preguntas complejas:

- **¿Cuál es el promedio de cada carrera en cada ciudad?** → pivot_table con suma o promedio
- **¿Cómo organizo datos en filas y columnas de forma dinámica?** → `pd.pivot_table()`
- **¿Cómo agrego múltiples métricas en una tabla cruzada?** → `aggfunc`

> [!IMPORTANT]
> `pivot_table()` es como una tabla dinámica en Excel: agrupa por filas, distribuye en columnas y resume con una función.

---

## ¿Qué vas a aprender?

- Estructura básica de pivot_table: índices (filas), columnas, valores, función de agregación.
- Cuándo usar `pivot_table()` en lugar de `groupby()`.
- Cómo manejar múltiples agregaciones en una sola tabla.
- Cómo tratar datos faltantes en tablas cruzadas.

**Documentación:** [pivot_table](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html)

---

## 1. Pivot table simple

Organiza datos en una tabla de dos dimensiones.

```python
import pandas as pd

# DataFrame de estudiantes con repeticiones (ficticio)
df = pd.DataFrame({
    "periodo": ["2023-1", "2023-1", "2023-2", "2024-1", "2024-1", "2024-2"],
    "ciudad": ["Bogotá", "Santiago", "Bogotá", "Bogotá", "Santiago", "Santiago"],
    "carrera": ["Ingeniería de Sistemas", "Psicología", "Ingeniería de Sistemas", "Ingeniería de Sistemas", "Psicología", "Psicología"],
    "promedio": [4.5, 4.2, 4.7, 4.8, 4.4, 4.6]
})

# Tabla cruzada: carrera (filas) x ciudad (columnas), valor = promedio académico
result = pd.pivot_table(
    df,
    values="promedio",
    index="carrera",
    columns="ciudad",
    aggfunc="mean"
)
print(result)
# Output:
# ciudad        Bogotá  Santiago
# carrera
# Ingeniería de Sistemas   4.7   NaN
# Psicología               NaN   4.4
```

### Interpretar el resultado

- Filas: valores únicos de `index` (puesto).
- Columnas: valores únicos de `columns` (ciudad).
- Celdas: agregación (promedio, suma, etc.) de `values`.
- `NaN` cuando no hay combinación.

---

## 2. Múltiples funciones de agregación

```python
# Promedio académico Y máximo por carrera y ciudad
result = pd.pivot_table(
    df,
    values="promedio",
    index="carrera",
    columns="ciudad",
    aggfunc=["mean", "max"]
)
print(result)
# Output: columnas jerárquicas con (función, ciudad)
```

---

## 3. Múltiples valores

```python
# Dos métricas: promedio y semestre
df_extendido = df.copy()
df_extendido["semestre"] = [8, 5, 8, 8, 5, 5]

result = pd.pivot_table(
    df_extendido,
    values=["promedio", "semestre"],
    index="carrera",
    columns="ciudad",
    aggfunc="mean"
)
print(result)
# Output: columnas jerárquicas con (métrica, ciudad)
```

---

## 4. Rellenar NaN

Usa `fill_value` para reemplazar valores faltantes.

```python
result = pd.pivot_table(
    df,
    values="promedio",
    index="carrera",
    columns="ciudad",
    aggfunc="mean",
    fill_value=0
)
# Output: NaN reemplazados por 0
```

---

## Cuándo usar pivot_table vs groupby

- **pivot_table**: cuando necesitas una vista de dos dimensiones (matriz).
- **groupby**: cuando necesitas un resultado más flexible o resumido por una sola dimensión.

---

## Errores comunes

- Olvidar `aggfunc`: por defecto es `mean`, pero puede no ser lo que necesitas.
- No manejar `NaN`: una tabla con muchos NaN es difícil de leer.
- Confundir `index` (filas) con `columns` (columnas).
