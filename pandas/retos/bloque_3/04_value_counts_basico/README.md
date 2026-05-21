# 04 - Value Counts Básico

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos obtener este resultado porque muchas columnas son categóricas y lo que necesitamos primero es saber cuántas veces aparece cada valor; esa idea nos ayuda a reconocer categorías dominantes, revisar nulos y entender qué tan repetidos están los datos antes de hacer análisis más profundos.

---

## ¿Qué haremos?

Practicaremos **contar frecuencias de valores** en una tienda en línea:

- **¿Cuántas veces aparece cada valor?** → `value_counts()`
- **¿Cuál es la categoría o ciudad más frecuente?** → `value_counts().iloc[0]`
- **¿Cómo ordeno de mayor a menor frecuencia?** → comportamiento por defecto
- **¿Cómo veo también los nulos?** → `value_counts(dropna=False)`

> [!IMPORTANT]
> `value_counts()` por defecto ordena de mayor a menor frecuencia y excluye nulos.

---

## Que vas a aprender

- Cómo `value_counts()` resume categorías.
- Cuándo usar `dropna=False` para incluir nulos.
- Cómo combinar `value_counts()` con filtros.
- Por qué `value_counts()` es mejor que `groupby().count()` para este caso.

---

## 1. Conteo simple

> [!NOTE]
> `value_counts()` devuelve una Serie ordenada de mayor a menor frecuencia. No devuelve un DataFrame.

```python
import pandas as pd

df = pd.DataFrame({
    "producto": ["Laptop", "Mouse", "Laptop", "Teclado", "Audífonos", "Silla"],
    "categoria": ["Tecnología", "Tecnología", "Tecnología", "Tecnología", "Tecnología", "Hogar"],
    "ciudad": ["Ciudad de México", "Guadalajara", "Monterrey", "Puebla", "Mérida", "Tijuana"],
})

print(df["categoria"].value_counts())
# Output:
# categoria
# Tecnología    5
# Hogar         1

print(df["ciudad"].value_counts())
# Output:
# Ciudad de México    1
# Guadalajara         1
# Monterrey           1
# Puebla              1
# Mérida              1
# Tijuana             1
```

### Cuándo usar top N

- Para contar cuántas veces aparece cada categoría.
- Para resumir una columna categórica rápidamente.

---

## 2. Top N valores más frecuentes

```python
top_3_ciudades = df["ciudad"].value_counts().head(3)
mas_frecuente = df["categoria"].value_counts().index[0]

print(top_3_ciudades)
# Output:
# Ciudad de México    1
# Guadalajara         1
# Monterrey           1

print(f"Categoría más frecuente: {mas_frecuente}")
# Output: Categoría más frecuente: Tecnología
```

### Cuándo usar nulos

- Cuando te importan solo las categorías más repetidas.
- Para mostrar rankings rápidos.

---

## 3. Incluir nulos

> [!NOTE]
> Los nulos no cuentan por defecto. `dropna=False` sirve para verlos y no esconder datos faltantes.

```python
df_con_nulos = df.copy()
df_con_nulos.loc[0, "ciudad"] = None

print(df_con_nulos["ciudad"].value_counts())
print(df_con_nulos["ciudad"].value_counts(dropna=False))
# Output incluye NaN cuando usas dropna=False
```

### Cuándo usar ordenamiento personalizado

- Cuando necesitas auditar datos faltantes.
- Cuando no quieres ocultar valores nulos en el conteo.

---

## 4. Ordenamiento personalizado

> [!NOTE]
> Si quieres ordenar por la etiqueta y no por la frecuencia, usa `sort_index()`. Es distinto de ordenar por cantidad.

```python
print(df["ciudad"].value_counts(ascending=True))
print(df["ciudad"].value_counts().sort_index())
```

### Cuándo usarlo

- Cuando quieres ver categorías menos frecuentes primero.
- Cuando prefieres ordenar alfabéticamente.

---

## Errores comunes

- Olvidar que `value_counts()` devuelve una Serie, no un DataFrame.
- No considerar nulos: pueden estar ocultos si no usas `dropna=False`.
- Confundir `value_counts()` con `groupby().count()`.
