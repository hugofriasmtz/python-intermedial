# 03 - Groupby Básico

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **agrupar datos y resumirlos** respondiendo preguntas académicas:

- **¿Cómo calculo el promedio por ciudad?** → `groupby('ciudad').mean()`
- **¿Cómo cuento cuántos estudiantes hay en cada ciudad?** → `groupby('ciudad').size()`
- **¿Cómo resumo varias métricas a la vez?** → `groupby().agg({'col': función})`
- **¿Cuál es el promedio máximo en cada ciudad?** → `groupby('ciudad').max()`

> [!IMPORTANT]
> `groupby()` no ordena el DataFrame; solo agrupa. El orden será el orden de aparición del grupo en los datos.

---

## ¿Qué vas a aprender?

- Por qué `groupby()` es más eficiente que bucles manuales.
- Funciones de agregación: `sum()`, `mean()`, `count()`, `max()`, `min()`.
- Cuándo usar `size()` vs `count()` para contar grupos.
- Cómo darle un nombre a la columna resultante.

**Documentación:** [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html), [agg](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.agg.html) y [reset_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html)

---

## 1. Groupby simple

Agrupa por una columna y aplica una función a las demás columnas numéricas.

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "carrera": ["Ingeniería de Sistemas", "Economía", "Psicología", "Arquitectura", "Medicina", "Derecho"],
    "promedio": [4.8, 4.1, 4.5, 3.9, 4.9, 4.0],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "semestre": [8, 6, 5, 7, 9, 4]
})

# Promedio por ciudad
print(df.groupby("ciudad")["promedio"].mean())
# Output:
# ciudad
# Bogotá              4.8
# Caracas             4.0
# Ciudad de México    4.1
# La Paz              4.9
# Medellín            3.9
# Santiago            4.5

# Cuántos estudiantes por ciudad
print(df.groupby("ciudad").size())
# Output:
# ciudad
# Bogotá              1
# Caracas             1
# Ciudad de México    1
# ...
# (resultado: 1 estudiante por ciudad)
```

### ¿Funciones de agregación comunes?

- `sum()`: suma total.
- `mean()`: promedio.
- `count()`: cuenta valores no nulos.
- `max()` / `min()`: máximo/mínimo.
- `std()`: desviación estándar.

---

## 2. Resumen con agg()

Cuando necesitas aplicar varias funciones a la vez o funciones específicas a columnas específicas.

```python
# Resumen: promedio y máximo por ciudad
print(df.groupby("ciudad")["promedio"].agg(["mean", "max"]))
# Output:
#                      mean   max
# ciudad
# Bogotá              4500  4500
# Caracas             3100  3100
# ...

# Resumen de múltiples columnas con diferentes funciones
print(df.groupby("ciudad").agg({
    "promedio": ["mean", "max"],
    "semestre": "mean"
}))
# Output:
#                      salario  años_experiencia
#                         mean  max           mean
# ciudad
# Bogotá              4500 4500              8.0
# Caracas             3100 3100              7.0
# ...
```

---

## 3. Dar nombres claros al resultado

Usa `reset_index()` para convertir el resultado en un DataFrame más legible.

```python
# Sin reset_index: Series con índice nombrado
result = df.groupby("ciudad")["promedio"].mean()

# Con reset_index: DataFrame con columnas normales
result = df.groupby("ciudad")["promedio"].mean().reset_index()
result.columns = ["ciudad", "promedio_academico"]
print(result)
# Output:
#                  ciudad  promedio_academico
# 0                Bogotá            4500.0
# 1                Caracas            3100.0
# ...
```

---

## Errores comunes

- Confundir `size()` (cuenta todas las filas del grupo) con `count()` (cuenta valores no nulos).
- Olvidar `reset_index()` cuando necesitas un DataFrame normal.
- Intentar acceder a columnas del grupo después de `groupby()` sin seleccionarlas primero.
