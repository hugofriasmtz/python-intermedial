# 07 - Drop Duplicates Compuesto

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos encontrar este resultado porque una fila no siempre se define por una sola columna; muchas veces la verdadera identidad aparece al combinar dos o más campos, y por eso aprender a deduplicar por conjunto de columnas nos ayuda a conservar solo la información que realmente cambia.

---

## ¿Qué haremos?

Practicaremos **eliminar duplicados basándonos en múltiples columnas** usando pedidos de una tienda en línea:

- **¿Cómo encuentro pedidos duplicados por producto y ciudad?** → `drop_duplicates(subset=['producto','ciudad'])`
- **¿Cuál es la combinación más frecuente?** → combina con `value_counts()` o `groupby().size()`
- **¿Cómo retengo el mejor precio o la mejor fila?** → `idxmax()`

> [!IMPORTANT]
> El orden de las columnas en `subset` no afecta qué se elimina, pero sí afecta qué se mantiene con `keep='first'` o `keep='last'`.

---

## ¿Qué vas a aprender?

- Cómo deduplicar por combinaciones de columnas.
- Cuándo es útil deduplicar por múltiples criterios.
- Cómo interpretar qué fila se mantiene y por qué.
- Cómo combinar deduplicación con análisis posterior.

**Documentación:** [drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html), [value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html) y [idxmax](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.idxmax.html)

---

## 1. Eliminar duplicados por combinación

> [!NOTE]
> En `subset`, la combinación de columnas define la unicidad. Si producto y ciudad coinciden, se considera el mismo caso.

```python
import pandas as pd

df = pd.DataFrame({
    "producto": ["Laptop", "Laptop", "Mouse", "Mouse", "Teclado"],
    "ciudad": ["Ciudad de México", "Ciudad de México", "Guadalajara", "Guadalajara", "Monterrey"],
    "categoria": ["Tecnología", "Tecnología", "Tecnología", "Tecnología", "Tecnología"],
    "precio": [1200, 1250, 25, 30, 55]
})

print(df.drop_duplicates(subset=["producto", "ciudad"], keep="first"))
# Output:
#   producto             ciudad        categoria  precio
# 0  Laptop   Ciudad de México     Tecnología   1200
# 2  Mouse        Guadalajara     Tecnología     25
# 4  Teclado         Monterrey     Tecnología     55
```

### Cuándo usar última ocurrencia

- ¿Cuándo un producto puede repetirse en distintas ciudades?

---

## 2. Mantener última ocurrencia

```python
print(df.drop_duplicates(subset=["producto", "ciudad"], keep="last"))
# Output conserva el último registro de cada combinación
```

### Cuándo usar combinaciones repetidas

- ¿Cuándo el último registro contiene la versión más reciente?

---

## 3. Contar combinaciones únicas

> [!NOTE]
> `groupby().size()` cuenta cuántas veces aparece cada combinación. Es útil antes de decidir si deduplicas o no.

```python
combinaciones = df.groupby(["producto", "ciudad"]).size()
print(combinaciones)
print(combinaciones.sort_values(ascending=False))
# Output:
# producto  ciudad
# Laptop    Ciudad de México    2
# Mouse     Guadalajara         2
# Teclado   Monterrey           1
```

### Cuándo usar máximo por combinación

- Para saber qué combinaciones se repiten más.

---

## 4. Retener valores máximos

> [!NOTE]
> `idxmax()` devuelve el índice de la fila con el valor máximo. Luego `loc[]` usa ese índice para quedarte con la fila completa.

```python
df_mejor = df.loc[df.groupby(["producto", "ciudad"])["precio"].idxmax()]
print(df_mejor)
# Output conserva el precio más alto por combinación
```

### Cuándo usarlo

- ¿Cuándo quieres quedarte con el mayor precio, la mejor calificación o el valor más relevante?

---

## Errores comunes

- Confundir `subset=['a','b']` con seleccionar solo esas columnas en la salida.
- No considerar qué información se pierde al deduplicar.
- Olvidar que `idxmax()` depende del orden y de los valores disponibles.
