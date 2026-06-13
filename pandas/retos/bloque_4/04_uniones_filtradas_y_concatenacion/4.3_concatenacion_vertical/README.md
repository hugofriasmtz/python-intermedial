# 4.3 - Concatenación vertical

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En esta lección vamos a combinar varios DataFrames uno debajo del otro. La idea es apilar tablas con la misma estructura para formar una sola tabla más larga usando `pandas.concat()`.

---

## ¿Qué haremos?

Partiremos de tres tablas con las mismas columnas: `inv_jan`, `inv_feb` e `inv_mar`. Después veremos cómo concatenarlas verticalmente, cómo ignorar el índice original cuando hace falta y cómo etiquetar cada tabla de origen.

- **¿Cómo junto varias tablas una debajo de la otra?** -> `pd.concat([...])`
- **¿Qué pasa con el índice original?** -> se conserva por defecto
- **¿Cómo renumero las filas al concatenar?** -> `ignore_index=True`
- **¿Cómo identifico de qué tabla viene cada bloque?** -> `keys=['jan', 'feb', 'mar']`

> [!TIP]
> Usa concatenación vertical cuando las tablas tienen las mismas columnas y quieres sumar filas, no combinar campos.

### Idea visual

![Concatenacion vertical en pandas](https://pandas.pydata.org/docs/_images/merging_concat_basic.png)

> [!IMPORTANT]
> `pd.concat()` apila objetos a lo largo de un eje. Para concatenación vertical usa `axis=0`, que además es el valor por defecto.

---

## ¿Qué vas a aprender?

- Cómo apilar tres DataFrames con `pd.concat()`.
- Cómo conservar o reiniciar el índice con `ignore_index`.
- Cómo etiquetar el origen de cada bloque con `keys`.
- Qué ocurre cuando las tablas no comparten exactamente las mismas columnas.
- Cómo usar `sort=True` o `join='inner'` cuando las columnas difieren.

**Documentación:** [pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

---

## 1. Concatenar tablas con las mismas columnas

Cuando las tablas comparten la misma estructura, concatenarlas verticalmente es directo.

```python
import pandas as pd

inv_jan = pd.DataFrame({
    "iid": [1, 2, 3],
    "cid": [2, 4, 8],
    "invoice_date": ["2009-01-01", "2009-01-02", "2009-01-03"],
    "total": [1.98, 3.96, 5.94],
})

inv_feb = pd.DataFrame({
    "iid": [7, 8, 9],
    "cid": [38, 40, 42],
    "invoice_date": ["2009-02-01", "2009-02-01", "2009-02-02"],
    "total": [1.98, 1.98, 3.96],
})

inv_mar = pd.DataFrame({
    "iid": [14, 15, 16],
    "cid": [17, 19, 21],
    "invoice_date": ["2009-03-04", "2009-03-04", "2009-03-05"],
    "total": [1.98, 1.98, 3.96],
})

# Apilamos las tres tablas una debajo de la otra.
inv_all = pd.concat([inv_jan, inv_feb, inv_mar])

print(inv_all)
# Output:
#    iid  cid invoice_date  total
# 0    1    2   2009-01-01   1.98
# 1    2    4   2009-01-02   3.96
# 2    3    8   2009-01-03   5.94
# 0    7   38   2009-02-01   1.98
# 1    8   40   2009-02-01   1.98
# 2    9   42   2009-02-02   3.96
# 0   14   17   2009-03-04   1.98
# 1   15   19   2009-03-04   1.98
# 2   16   21   2009-03-05   3.96
```

### ¿Por qué sirve esto?

- Porque suma filas sin mezclar columnas.
- Porque mantiene la estructura original de cada tabla.
- Porque te permite trabajar con datos mensuales, semanales o por lotes como una sola tabla.

Si luego quieres que el índice quede continuo, usa `ignore_index=True`.

```python
inv_all_reset = pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True)

print(inv_all_reset)
# Output:
#    iid  cid invoice_date  total
# 0    1    2   2009-01-01   1.98
# 1    2    4   2009-01-02   3.96
# 2    3    8   2009-01-03   5.94
# 3    7   38   2009-02-01   1.98
# 4    8   40   2009-02-01   1.98
# 5    9   42   2009-02-02   3.96
# 6   14   17   2009-03-04   1.98
# 7   15   19   2009-03-04   1.98
# 8   16   21   2009-03-05   3.96
```

Este enfoque es útil cuando quieres un índice limpio y consecutivo después de apilar las tablas.

---

## 2. Revisar si el índice quedó bien

Después de concatenar, conviene revisar el índice para confirmar si quieres conservarlo o renumerarlo.

```python
indice_original = inv_all.index
indice_nuevo = inv_all_reset.index

print(indice_original)
print(indice_nuevo)
# Output:
# Int64Index([0, 1, 2, 0, 1, 2, 0, 1, 2], dtype='int64')
# RangeIndex(start=0, stop=9, step=1)
```

Posibles revisiones útiles:

- `ignore_index=True`: genera un índice nuevo y consecutivo.
- `keys=[...]`: crea un índice jerárquico para identificar el origen de cada bloque.
- `verify_integrity=True`: valida que no se repitan índices si necesitas seguridad extra.

Este paso importa porque un índice repetido no siempre es un problema, pero puede confundir si luego vas a seleccionar filas por posición.

Si quieres conservar etiquetas por tabla de origen, usa `keys`.

```python
inv_labeled = pd.concat(
    [inv_jan, inv_feb, inv_mar],
    ignore_index=False,
    keys=["jan", "feb", "mar"],
)

print(inv_labeled)
# Output:
#       iid  cid invoice_date  total
# jan 0   1    2   2009-01-01   1.98
#     1   2    4   2009-01-02   3.96
#     2   3    8   2009-01-03   5.94
# feb 0   7   38   2009-02-01   1.98
#     1   8   40   2009-02-01   1.98
#     2   9   42   2009-02-02   3.96
# mar 0  14   17   2009-03-04   1.98
#     1  15   19   2009-03-04   1.98
#     2  16   21   2009-03-05   3.96
```

Este patrón es útil cuando quieres saber de qué mes proviene cada bloque de filas.

---

## 3. Índices compuestos cuando una sola columna no alcanza

A veces una sola tabla trae columnas extra y otra no. En ese caso puedes concatenar igual y dejar que pandas alinee por nombre de columna.

```python
inv_jan = pd.DataFrame({
    "iid": [1, 2, 3],
    "cid": [2, 4, 8],
    "invoice_date": ["2009-01-01", "2009-01-02", "2009-01-03"],
    "total": [1.98, 3.96, 5.94],
})

inv_feb = pd.DataFrame({
    "iid": [7, 8, 9],
    "cid": [38, 40, 42],
    "invoice_date": ["2009-02-01", "2009-02-01", "2009-02-02"],
    "total": [1.98, 1.98, 3.96],
    "bill_ctry": ["Germany", "France", "France"],
})

# Concatenamos aunque las columnas no sean exactamente iguales.
inv_mix = pd.concat([inv_jan, inv_feb], sort=True)

print(inv_mix)
# Output:
#   bill_ctry  cid  iid invoice_date  total
# 0       NaN    2    1   2009-01-01   1.98
# 1       NaN    4    2   2009-01-02   3.96
# 2       NaN    8    3   2009-01-03   5.94
# 0   Germany   38    7   2009-02-01   1.98
# 1    France   40    8   2009-02-01   1.98
# 2    France   42    9   2009-02-02   3.96
```

Este patrón te deja preparado para trabajar con tablas que no son idénticas pero sí compatibles.

---

## 4. ¿Cuándo usar `set_index()`?

- Usa `pd.concat()` cuando quieras apilar DataFrames verticalmente.
- Usa `ignore_index=True` cuando necesites un índice nuevo y consecutivo.
- Usa `keys=[...]` cuando quieras conservar el origen de cada tabla.
- Usa `sort=True` cuando las columnas no sean exactamente iguales y quieras ordenar el resultado.
- Usa `join='inner'` cuando quieras quedarte solo con las columnas compartidas.

Como regla práctica, pregúntate esto antes de concatenar:

- ¿Las tablas tienen las mismas columnas?
- ¿Quiero conservar el índice original o crear uno nuevo?
- ¿Necesito saber de qué tabla vino cada bloque?
- ¿Las columnas extra deben conservarse o descartarse?

---

## Errores comunes

1. Concatenar tablas con columnas distintas sin revisar el resultado: pandas rellena con `NaN` las columnas faltantes.

2. Olvidar `ignore_index=True` cuando quieres un índice limpio y consecutivo.

3. Usar `keys` sin necesidad: solo úsalo cuando de verdad quieras marcar el origen de cada bloque.

4. Confiar en que `pd.concat()` reordena columnas siempre como esperas: si el orden importa, revisa `sort=True` o alinea antes.

5. Pensar que concatenar verticalmente mezcla filas por llave: en realidad apila filas una debajo de la otra.
