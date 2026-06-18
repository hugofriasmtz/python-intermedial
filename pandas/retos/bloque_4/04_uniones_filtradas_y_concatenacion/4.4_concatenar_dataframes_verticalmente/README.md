# 4.4 - Concatenate DataFrames together vertically

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La practica consistente transforma lo dificil en dominio. Cada linea de codigo es un paso adelante."

En esta parte vas a apilar tablas una debajo de otra con `pd.concat()`. La idea es sumar filas cuando los DataFrames comparten la misma estructura de columnas.

---

## ¿Que haremos?

Partiremos de tres tablas sencillas (`inv_jan`, `inv_feb`, `inv_mar`) y las combinaremos verticalmente. Luego veremos como controlar el indice y como conservar el origen de cada bloque.

> [!TIP]
> Si las tablas tienen las mismas columnas y solo quieres sumar filas, `concat()` es la opcion mas directa.

- **¿Como apilo varias tablas?** -> `pd.concat([df1, df2, df3], axis=0)`
- **¿Que pasa con el indice original?** -> se conserva por defecto
- **¿Como renumero las filas al concatenar?** -> `ignore_index=True`
- **¿Como identifico de donde viene cada bloque?** -> `keys=[...]`

> [!IMPORTANT]
> `concat()` apila objetos a lo largo de un eje; no empareja llaves como `merge()`.

---

## ¿Que vas a aprender?

- Concatenar DataFrames verticalmente.
- Reindexar el resultado con `ignore_index=True`.
- Etiquetar bloques de origen con `keys`.
- Entender cuando usar `concat()` en vez de `merge()`.

**Documentacion:** [pandas.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)

---

## 1. Concatenacion vertical basica

La forma mas comun de trabajar con `concat()` es apilar tablas con la misma estructura.

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

### ¿Por que sirve esto?

- Porque suma filas sin mezclar llaves.
- Porque conserva la forma de cada tabla.
- Porque es ideal cuando tienes datos separados por mes, lote o fuente.

Si quieres un indice continuo, usa `ignore_index=True`.

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

Este enfoque deja el resultado mas facil de leer cuando ya no necesitas los indices originales.

---

## 2. Revisar si el indice quedo bien

Despues de concatenar, conviene revisar el indice para confirmar si quieres conservarlo o renumerarlo.

```python
print(inv_all.index)
print(inv_all_reset.index)
# Output:
# Int64Index([0, 1, 2, 0, 1, 2, 0, 1, 2], dtype='int64')
# RangeIndex(start=0, stop=9, step=1)
```

Posibles revisiones utiles:

- `ignore_index=True`: crea un indice nuevo y consecutivo.
- `keys=[...]`: etiqueta el origen de cada bloque.
- `sort=True`: ordena columnas si no son exactamente iguales.

Si quieres conservar etiquetas por mes, usa `keys`.

```python
inv_labeled = pd.concat([inv_jan, inv_feb, inv_mar], keys=["jan", "feb", "mar"])
print(inv_labeled)
# Output:
#       iid  cid invoice_date  total
# jan 0   1    2   2009-01-01   1.98
#     1   2    4   2009-01-02   3.96
#     2   3    8   2009-01-03   5.94
# feb 0   7   38   2009-02-01   1.98
# ...
```

Este patron es util cuando quieres saber de que bloque viene cada fila.

---

## 3. Columnas distintas al concatenar

A veces una tabla trae columnas extra y otra no. En ese caso pandas alinea por nombre de columna y completa con `NaN`.

```python
inv_feb_extra = pd.DataFrame({
    "iid": [7, 8, 9],
    "cid": [38, 40, 42],
    "invoice_date": ["2009-02-01", "2009-02-01", "2009-02-02"],
    "total": [1.98, 1.98, 3.96],
    "bill_ctry": ["Germany", "France", "France"],
})

inv_mix = pd.concat([inv_jan, inv_feb_extra], sort=True)
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

---

## 4. ¿Cuando usar `concat()` vertical?

- Cuando varias tablas tienen las mismas columnas.
- Cuando quieres acumular filas por periodos.
- Cuando no necesitas emparejar llaves entre tablas.

Como regla practica, preguntate esto antes de concatenar:

- ¿Las tablas tienen la misma estructura?
- ¿Quiero conservar el indice original o crear uno nuevo?
- ¿Necesito saber de donde vino cada bloque?

---

## Errores comunes

1. Esperar comportamiento de `merge()` al usar `concat()`.
2. Olvidar `ignore_index=True` cuando necesitas indice continuo.
3. Concatenar columnas incompatibles sin revisar `NaN`.
4. No validar el resultado con `head()` y `shape`.
5. No usar `keys` cuando quieres conservar el origen de cada bloque.
