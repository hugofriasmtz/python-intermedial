# 02 - Rango y Dispersión

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos ver este resultado porque no solo importa el valor típico de una columna, sino también qué tan separadas están sus observaciones; por eso usamos medidas de dispersión que nos ayudan a entender si los precios, el stock o cualquier otra variable están muy concentrados o demasiado variados.

---

## ¿Qué haremos?

Practicaremos **medir la dispersión de datos** con precios y stock de una tienda en línea:

- **¿Qué tan dispersos están los precios?** → `std()`, `var()`
- **¿Cuál es el rango de valores?** → `max()` - `min()`
- **¿Cuál es el rango intercuartílico?** → Q3 - Q1
- **¿Hay outliers (valores extremos)?** → regla 1.5 × IQR

> [!IMPORTANT]
> Alta desviación estándar = datos muy dispersos. Baja = datos agrupados cerca del promedio.

---

## Que vas a aprender

- Diferencia entre varianza y desviación estándar.
- Cómo usar IQR para detectar outliers.
- Cuándo la dispersión es importante para tu análisis.
- Cómo comparar dispersión entre grupos.

---

## 1. Rango, varianza, desviación estándar

```python
import pandas as pd

df = pd.DataFrame({
    "producto": ["Laptop", "Mouse", "Teclado", "Audífonos", "Monitor", "Silla"],
    "precio": [1200, 25, 55, 80, 300, 180],
    "stock": [12, 180, 90, 60, 25, 40],
    "categoria": ["Tecnología", "Tecnología", "Tecnología", "Tecnología", "Tecnología", "Hogar"]
})

# Rango de precios
print(df["precio"].max() - df["precio"].min())
# Output: 1175

# Varianza de precios
print(df["precio"].var())
# Output: 179282.66666666666

# Desviación estándar
print(df["precio"].std())
# Output: 423.418...
```

### Interpretación

- **Rango**: simple pero sensible a outliers.
- **Varianza**: unidades al cuadrado.
- **Desviación estándar**: mismas unidades que los datos.

---

## 2. Rango intercuartílico (IQR)

> [!NOTE]
> El IQR mira el centro de la distribución. Suele ser más útil que el rango cuando hay valores extremos muy grandes.

```python
q1 = df["precio"].quantile(0.25)
q3 = df["precio"].quantile(0.75)
iqr = q3 - q1

# IQR
print(iqr)
# Output: 188.75

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
# Límites para outliers
print(limite_inferior)
print(limite_superior)
# Output: -216.875
# Output: 538.125

outliers = df[(df["precio"] < limite_inferior) | (df["precio"] > limite_superior)]
print(outliers)
# Output:
#   producto  precio  stock categoria
# 0  Laptop    1200    12   Tecnología
```

### Cuándo usar IQR

- Para detectar precios fuera de rango.
- Para datos asimétricos o con extremos muy altos.

---

## 3. Coeficiente de variación

> [!NOTE]
> El coeficiente de variación convierte la dispersión en porcentaje. Así puedes comparar precio y stock aunque estén en escalas distintas.

```python
cv_precio = (df["precio"].std() / df["precio"].mean()) * 100
cv_stock = (df["stock"].std() / df["stock"].mean()) * 100

# CV de precio
print(round(cv_precio, 1))
# Output: 138.1

# CV de stock
print(round(cv_stock, 1))
# Output: 76.2
```

### Cuándo usar coeficiente de variación

- Para comparar columnas con escalas distintas.
- Para saber cuál variable es más irregular proporcionalmente.

---

## 4. Dispersión por grupos

> [!NOTE]
> Cuando agrupas, cada grupo calcula su propia variación. Esto ayuda a detectar categorías con precios mucho más inestables.

```python
# Desviación estándar por categoría
print(df.groupby("categoria")["precio"].std())
# Output:
# categoria
# Hogar         NaN
# Tecnología    423.4...

# Varianza por categoría
print(df.groupby("categoria")["stock"].var())
# Output:
# categoria
# Hogar         NaN
# Tecnología    5798.0...
```

### Cuándo usar por grupos

- Para comparar variación por categoría.
- Para descubrir qué grupo tiene precios más inestables.

---

## Errores comunes

- Confundir varianza con desviación estándar.
- No usar IQR para detectar outliers.
- Comparar desviaciones estándar de columnas con escalas diferentes; usa CV.
