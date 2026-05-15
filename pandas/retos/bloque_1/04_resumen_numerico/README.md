# 04 - Resumen Numerico

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Con columnas numéricas, antes de empezar el análisis, necesitas responder preguntas rápidas:

- **¿Cuál es el total?** → `sum()`
- **¿Cuál es el promedio?** → `mean()`
- **¿Cuál es el valor del medio?** → `median()` (más resistente a extremos que `mean()`)
- **¿Cuál es el mínimo y máximo?** → `min()`, `max()`
- **¿Cuántos datos tengo?** → `count()` (ignora nulos)
- **¿Cuántos valores distintos?** → `nunique()`

Estas preguntas te revelan patrones, anomalías y problemas sin ver todas las filas.

> [!TIP]
> `df.describe()` te da varias métricas comunes de una sola vez para columnas numéricas.

---

## Que vas a aprender

- Cuándo usar `mean()` vs `median()`
- Por qué `count()` es diferente a `len()`
- Cómo `describe()` ahorra tiempo en resúmenes
- Interpretar valores extremos

---

## 1. Resumen rápido

Primero, nuestro DataFrame de ejemplo:

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

Ahora, resumamos la columna de salarios:

```python
print(df["salario"].sum())
# Output: 21000

print(df["salario"].mean())
# Output: 3500.0

print(df["salario"].median())
# Output: 3400.0

print(df["salario"].min())
# Output: 2800

print(df["salario"].max())
# Output: 4500
```

### Para qué sirve el resumen rápido

- Ver valores centrales.
- Detectar extremos (salario mínimo y máximo).
- Resumir una columna rápidamente sin ver todas las filas.

**Documentación:** [Series methods](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

---

## 2. Conteos útiles

```python
# Cuántos registros tenemos:
print(df["nombre"].count())
# Output: 6

# Cuántos valores distintos en ciudad:
print(df["ciudad"].nunique())
# Output: 6 (todas las ciudades son distintas)

# Cuántas ciudades únicas y cuáles son:
print(df["ciudad"].unique())
# Output: ['Bogotá' 'Ciudad de México' 'Santiago' 'Medellín' 'La Paz' 'Caracas']
```

### Para qué sirven los conteos

- Saber cuántos datos válidos tienes (excluyendo nulos).
- Saber cuántos valores distintos hay (para detectar repeticiones o variedad).
- Identificar qué valores se repiten en una columna.

---

## 3. Mini practica

Compara media y mediana de `goles`. Si son muy distintas, la columna puede estar sesgada.
