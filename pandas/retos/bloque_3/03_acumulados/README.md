# 03 - Acumulados

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos observar este tipo de resultados porque algunas columnas no solo se leen fila por fila, sino que también se interpretan como una secuencia; así, los acumulados nos muestran cómo va creciendo una cifra, cómo cambia un máximo o cómo se comporta un proceso paso a paso.

---

## ¿Qué haremos?

Practicaremos **calcular acumulaciones** con pedidos e ingresos de una tienda en línea:

- **¿Cuál es el total acumulado hasta cada fila?** → `cumsum()`
- **¿Cuál es el mayor valor visto hasta ahora?** → `cummax()`
- **¿Cuál es el menor valor visto hasta ahora?** → `cummin()`
- **¿Cómo multiplico factores paso a paso?** → `cumprod()`

> [!IMPORTANT]
> Los acumulados respetan el orden del DataFrame. Ordena primero si necesitas un orden específico.

---

## ¿Qué vas a aprender?

- Casos de uso para cada función acumulada.
- Cómo interpretar resultados acumulados.
- Cuándo usar acumulados por grupo.
- Cómo leer un producto acumulado.

**Documentación:** [cumsum](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cumsum.html), [cummax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cummax.html), [cummin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cummin.html) y [cumprod](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cumprod.html)

---

## 1. Suma acumulada

> [!NOTE]
> `cumsum()` depende del orden de las filas. Si cambias el orden, cambia la historia acumulada.

```python
import pandas as pd

df = pd.DataFrame({
    "semana": ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
    "pedidos": [12, 15, 10, 18]
})

df["pedidos_acumulados"] = df["pedidos"].cumsum()

print(df)
# Output:
#      semana  pedidos  pedidos_acumulados
# 0  Semana 1       12                  12
# 1  Semana 2       15                  27
# 2  Semana 3       10                  37
# 3  Semana 4       18                  55
```

### Cuándo usarla

- Para seguir el total de pedidos o ventas a lo largo del tiempo.
- Para ver cómo crece una métrica fila por fila.

---

## 2. Máximo y mínimo acumulado

```python
df["maximo_historico"] = df["pedidos"].cummax()
df["minimo_historico"] = df["pedidos"].cummin()

print(df[["semana", "pedidos", "maximo_historico", "minimo_historico"]])
# Output:
#      semana  pedidos  maximo_historico  minimo_historico
# 0  Semana 1       12                12                12
# 1  Semana 2       15                15                12
# 2  Semana 3       10                15                10
# 3  Semana 4       18                18                10
```

### Cuándo usar máximos y mínimos

- Para detectar récords de pedidos o ingresos.
- Para ver el peor valor observado hasta cada fila.

---

## 3. Producto acumulado

> [!NOTE]
> `cumprod()` no suma: multiplica paso a paso. Es útil para factores de crecimiento o ajustes encadenados.

```python
df2 = pd.DataFrame({
    "semana": [1, 2, 3, 4],
    "factor_crecimiento": [1.00, 1.05, 1.10, 1.02]
})

df2["indice"] = df2["factor_crecimiento"].cumprod()

print(df2)
# Output:
#    semana  factor_crecimiento  indice
# 0       1                1.00  1.0000
# 1       2                1.05  1.0500
# 2       3                1.10  1.1550
# 3       4                1.02  1.1781
```

### Cuándo usar producto acumulado

- Para combinar factores de crecimiento.
- Para calcular efectos acumulados de descuentos o ajustes.

---

## 4. Acumulados por grupo

> [!NOTE]
> Primero se separa por grupo y luego se acumula dentro de cada uno. Así cada canal empieza su propia cuenta desde cero.

```python
df_ciudades = pd.DataFrame({
    "canal": ["Web", "Web", "App", "App"],
    "semana": [1, 2, 1, 2],
    "pedidos": [12, 15, 10, 14]
})

df_ciudades["acumulado_por_canal"] = df_ciudades.groupby("canal")["pedidos"].cumsum()

print(df_ciudades)
# Output:
#   canal  semana  pedidos  acumulado_por_canal
# 0   Web       1       12                   12
# 1   Web       2       15                   27
# 2   App       1       10                   10
# 3   App       2       14                   24
```

### Cuándo usar acumulados por grupo

- Para acumular por canal, ciudad o categoría.
- Para comparar el crecimiento entre grupos.

---

## Errores comunes

- No ordenar antes de acumular: el resultado depende del orden del DataFrame.
- Confundir `cumsum()` con `sum()`.
- Olvidar usar `groupby()` cuando tienes múltiples series.
