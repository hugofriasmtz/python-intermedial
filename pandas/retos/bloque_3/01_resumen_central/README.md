# 01 - Resumen Central

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos encontrar este tipo de resultados porque pandas nos permite resumir una columna con cálculos que representan su valor típico, su posición dentro de la distribución y su comportamiento general; eso nos ayuda a entender por qué una métrica como el precio, la calificación o la categoría puede contarnos una historia útil antes de pasar a otros métodos.

---

## ¿Qué haremos?

Practicaremos **calcular medidas de tendencia central** usando datos de una tienda en línea:

- **¿Cuál es el precio típico de los productos?** → `mean()` o `median()`
- **¿Cuál es la categoría más frecuente?** → `mode()`
- **¿Cuál es el 75% percentil del precio?** → `quantile(0.75)`
- **¿Cómo obtengo un resumen rápido de todas las métricas?** → `describe()`

> [!IMPORTANT]
> `mean()` es sensible a valores extremos; `median()` es más robusta. Elige según tu pregunta.

---

## Que vas a aprender

- Diferencia entre media, mediana y moda.
- Cuándo cada una es más útil.
- Cómo usar percentiles para entender la distribución.
- Por qué `describe()` es tu mejor amigo para exploración rápida.

---

## 1. Media, mediana y moda

```python
import pandas as pd

df = pd.DataFrame({
    "producto": ["Laptop", "Mouse", "Teclado", "Audífonos", "Monitor", "Silla"],
    "categoria": ["Tecnología", "Tecnología", "Tecnología", "Tecnología", "Tecnología", "Hogar"],
    "precio": [1200, 25, 55, 80, 300, 180],
    "ciudad": ["Ciudad de México", "Guadalajara", "Monterrey", "Puebla", "Mérida", "Tijuana"],
    "calificacion": [4.8, 4.3, 4.5, 4.6, 4.7, 4.2]
})

# Precio promedio
print(df["precio"].mean())
# Output: 306.67

# Mediana de precios
print(df["precio"].median())
# Output: 140.0

# Moda de categorías
print(df["categoria"].mode())
# Output:
# 0    Tecnología

# Cuantil 75% del precio
print(df["precio"].quantile(0.75))
# Output: 255.0

# Resumen rápido
print(df["precio"].describe())
# Output:
# count      6.000000
# mean     306.666667
# std      423.418...
# min       25.000000
# 25%       66.250000
# 50%      140.000000
# 75%      255.000000
# max     1200.000000
```

### Cuándo usar media y mediana

- **Media**: cuando los precios no tienen extremos muy altos.
- **Mediana**: cuando hay productos muy caros que distorsionan el promedio.
- **Moda**: para saber qué categoría aparece más.

---

## 2. Percentiles y cuantiles

> [!NOTE]
> `quantile(0.5)` es la mediana. Los cuantiles sirven para cortar la distribución en partes y ubicar valores dentro del conjunto.

```python
q1 = df["precio"].quantile(0.25)
q2 = df["precio"].quantile(0.50)
q3 = df["precio"].quantile(0.75)
p99 = df["precio"].quantile(0.99)

print(f"25% percentil: {q1}")
print(f"50% percentil: {q2}")
print(f"75% percentil: {q3}")
print(f"99% percentil: {p99}")
```

### Cuándo usar percentiles

- Para ubicar un precio dentro del resto del catálogo.
- Para comparar una tienda con otra usando cortes similares.

---

## 3. Describe (resumen completo)

```python
print(df["precio"].describe())
```

### Cuándo usar describe

- Para ver media, desviación, mínimo, cuartiles y máximo en una sola línea.
- Para explorar rápidamente una columna numérica.

---

## 4. Por grupos

> [!NOTE]
> `groupby()` primero separa y luego resume. Úsalo cuando quieras comparar una métrica dentro de cada categoría.

```python
print(df.groupby("categoria")["precio"].mean())
print(df.groupby("ciudad")["precio"].describe())
```

### Cuándo usar por grupos

- Para comparar precios medios por categoría.
- Para resumir precios por ciudad o canal de venta.

---

## Errores comunes

- Usar `mean()` cuando hay outliers extremos (usa `median()`).
- Confundir `quantile(0.5)` con la mediana, aunque dan lo mismo.
- Olvidar que `mode()` devuelve una Serie, no un escalar.
