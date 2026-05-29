# 06 - Drop Duplicates Simple

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En los DataFrames podemos obtener este resultado porque en datos reales es común repetir filas o registros casi iguales; eliminar duplicados nos ayuda a quedarnos con una versión limpia de la información y a entender qué significa conservar la primera o la última ocurrencia.

---

## ¿Qué haremos?

Practicaremos **eliminar filas duplicadas** en el catálogo de una tienda en línea:

- **¿Cómo encuentro y elimino filas idénticas?** → `drop_duplicates()`
- **¿Cómo elimino duplicados basándome en una sola columna?** → `drop_duplicates(subset=['col'])`
- **¿Cómo mantengo la primera o última ocurrencia?** → `keep='first'` o `keep='last'`

> [!IMPORTANT]
> `drop_duplicates()` es sensible a TODAS las columnas por defecto. Especifica `subset` para ser selectivo.

---

## ¿Qué vas a aprender?

- Diferencia entre filas duplicadas y valores duplicados en una columna.
- Cuándo mantener la primera vs última ocurrencia.
- Cómo detectar duplicados sin eliminarlos.
- Cuándo necesitas eliminar duplicados.

**Documentación:** [drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) y [duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html)

---

## 1. Eliminar filas completamente idénticas

> [!NOTE]
> `drop_duplicates()` conserva la primera fila repetida por defecto. Si dos filas son idénticas, la segunda desaparece.

```python
import pandas as pd

df = pd.DataFrame({
    "producto": ["Laptop", "Laptop", "Mouse", "Teclado", "Mouse"],
    "categoria": ["Tecnología", "Tecnología", "Tecnología", "Tecnología", "Tecnología"],
    "precio": [1200, 1200, 25, 55, 25]
})

print(f"Filas antes: {len(df)}")
# Output: Filas antes: 5

df_limpio = df.drop_duplicates()
print(f"Filas después: {len(df_limpio)}")
# Output: Filas después: 3

print(df_limpio)
# Output:
#   producto    categoria  precio
# 0  Laptop   Tecnología    1200
# 2  Mouse    Tecnología      25
# 3  Teclado  Tecnología      55
```

### Cuándo usar registros únicos

- ¿Cuándo tienes registros repetidos idénticos?

---

## 2. Eliminar duplicados por columna específica

> [!NOTE]
> `subset=["producto"]` significa que esa columna define la unicidad. El resto de columnas solo acompaña la fila que se conserva.

```python
df_productos = df.drop_duplicates(subset=["producto"], keep="first")
print(df_productos)
print(f"Productos únicos: {len(df_productos)}")
# Output: Productos únicos: 3
```

### Cuándo usar última ocurrencia

- ¿Cuándo quieres conservar un registro por producto?

---

## 3. Mantener última ocurrencia

```python
df_ultima = df.drop_duplicates(subset=["producto"], keep="last")
print(df_ultima)
# Output conserva el último producto repetido
```

### Cuándo usar auditoría previa

- ¿Cuándo el último registro es el que te interesa conservar?

---

## 4. Detectar sin eliminar

> [!NOTE]
> `duplicated()` no borra nada: solo marca con `True` las filas repetidas después de la primera aparición.

```python
duplicados = df.duplicated()
print(duplicados)
print(df[duplicados])
print(f"Total duplicados: {duplicados.sum()}")
# Output: Total duplicados: 2
```

### Cuándo usar columnas múltiples

- ¿Cuándo primero quieres auditar los duplicados antes de borrarlos?

---

## 5. Por múltiples columnas

```python
df_por_combo = df.drop_duplicates(subset=["producto", "categoria"])
print(df_por_combo)
# Output: filas únicas por producto y categoría
```

### Cuándo usarlo

- ¿Cuándo la unicidad depende de más de una columna?

---

## Errores comunes

- No especificar `subset`.
- Confundir `keep="first"`, `keep="last"` y `keep=False`.
- Olvidar que `drop_duplicates()` no modifica el DataFrame original.
