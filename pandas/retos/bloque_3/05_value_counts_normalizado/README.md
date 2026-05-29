# 05 - Value Counts Normalizado

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos ver este resultado porque no siempre basta con contar cuántas veces aparece algo; a veces necesitamos comparar proporciones, porcentajes y pesos relativos para entender mejor cómo se reparte una categoría entre regiones, grupos o condiciones distintas.

---

## ¿Qué haremos?

Practicaremos **calcular proporciones y porcentajes** en una tienda en línea:

- **¿Cuál es el porcentaje de productos por categoría?** → `value_counts(normalize=True) * 100`
- **¿Cómo veo proporciones?** → `value_counts(normalize=True)`
- **¿Cómo redondeo porcentajes de forma legible?** → `.round(2)`

> [!IMPORTANT]
> Normalizar es útil cuando comparas distribuciones de tamaños diferentes.

---

## ¿Qué vas a aprender?

- Diferencia entre conteos absolutos y proporciones.
- Cuándo normalizar es más informativo que contar.
- Cómo formatear porcentajes de forma legible.
- Cómo comparar distribuciones entre grupos.

**Documentación:** [value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html)

---

## 1. Proporciones simples

> [!NOTE]
> `normalize=True` devuelve proporciones entre 0 y 1. Si quieres porcentaje, multiplica por 100.

```python
import pandas as pd

df = pd.DataFrame({
    "producto": ["Laptop", "Mouse", "Laptop", "Teclado", "Audífonos", "Silla"],
    "categoria": ["Tecnología", "Tecnología", "Tecnología", "Tecnología", "Tecnología", "Hogar"],
    "region": ["Norte", "Norte", "Sur", "Sur", "Centro", "Norte"]
})

print(df["categoria"].value_counts(normalize=True))
# Output:
# Tecnología    0.833333
# Hogar         0.166667

print((df["categoria"].value_counts(normalize=True) * 100).round(1))
# Output:
# Tecnología    83.3
# Hogar         16.7
```

### ¿Cuándo usar conteos y porcentajes?

- Para comparar categorías sin depender del tamaño total.
- Para ver qué tanto representa cada grupo.

---

## 2. Conteos y porcentajes juntos

> [!NOTE]
> Aquí combinamos cantidad absoluta y peso relativo. Esa mezcla ayuda a explicar mejor la distribución.

```python
conteos = df["region"].value_counts()
proporciones = df["region"].value_counts(normalize=True) * 100

resultado = pd.DataFrame({"cantidad": conteos, "porcentaje": proporciones.round(1)})
print(resultado)
# Output:
#          cantidad  porcentaje
# Norte          3        50.0
# Sur            2        33.3
# Centro         1        16.7
```

### ¿Cuándo usar filtro por proporción?

- Para presentar conteos y porcentajes en la misma tabla.
- Para reportes rápidos de distribución.

---

## 3. Filtrar por proporción

```python
umbrales = df["categoria"].value_counts(normalize=True)
valores_significativos = umbrales[umbrales > 0.10]
print(valores_significativos)
# Output:
# Tecnología    0.833333
# Hogar         0.166667
```

### ¿Cuándo usar comparación entre grupos?

- Para quedarte solo con las categorías que realmente pesan.

---

## 4. ¿Comparar distribuciones entre grupos?

> [!NOTE]
> `groupby(...).value_counts(normalize=True)` te deja comparar regiones como porcentajes, no solo como totales.

```python
print(df.groupby("region")["categoria"].value_counts(normalize=True))
resultado = df.groupby("region")["categoria"].value_counts(normalize=True).unstack(fill_value=0) * 100
print(resultado)
# Output: tabla cruzada con porcentajes por región
```

### ¿Cuándo usarlo?

- Para comparar cómo se reparte una categoría entre regiones.

---

## Errores comunes

- Olvidar que `normalize=True` da proporciones (0-1), no porcentajes (0-100).
- No redondear porcentajes.
- Confundir distribuciones de tamaños diferentes.
