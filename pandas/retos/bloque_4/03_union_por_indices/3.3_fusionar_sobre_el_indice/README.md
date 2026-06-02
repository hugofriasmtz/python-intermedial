# 3.3 - Fusionar usando el índice

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

Aquí vas a fusionar dos DataFrames usando el índice como llave con `merge()`. La diferencia importante frente a `join()` es que aquí controlas explícitamente `left_index` y `right_index`, lo que te da más claridad cuando comparas tablas indexadas.

---

## ¿Qué haremos?

Tomaremos dos tablas indexadas y las uniremos con `pd.merge(..., left_index=True, right_index=True)`. Después revisaremos cómo auditar coincidencias, cómo elegir el tipo de unión y cómo interpretar la columna `_merge`.

- **¿Cómo fusiono por índice con `merge()`?** -> `left_index=True` y `right_index=True`
- **¿Cómo veo de dónde vino cada fila?** -> `indicator=True`
- **¿Cómo conservo solo coincidencias?** -> `how='inner'`
- **¿Cómo reviso faltantes en cada lado?** -> `how='outer'`

> [!TIP]
> Si necesitas más control sobre la unión que con `join()`, `merge()` por índice es la opción más explícita.

> [!IMPORTANT]
> Cuando ambas tablas están indexadas, el valor del índice determina si las filas se alinean o quedan fuera del resultado.

---

## ¿Qué vas a aprender?

- Cómo usar `merge()` sobre índices.
- Cómo elegir `how` para conservar filas de izquierda, derecha, ambas o solo coincidencias.
- Cómo auditar coincidencias con `_merge`.
- Cómo validar que el índice tenga el mismo tipo en ambas tablas.
- Cómo interpretar filas `left_only` y `right_only`.

**Documentación:** [Guía — Merge, join y concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) — [API: pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Fusionar tablas indexadas

La unión por índice con `merge()` es útil cuando quieres dejar claro en el código que la llave está en el índice.

Vamos a trabajar con ventas por sucursal.

### Parámetros clave de `merge()`

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `left_index` | Usa el índice del DataFrame izquierdo como llave. | Cuando la llave está en el índice izquierdo. |
| `right_index` | Usa el índice del DataFrame derecho como llave. | Cuando la llave está en el índice derecho. |
| `how` | Define el tipo de unión. | Cuando quieres conservar coincidencias o hacer auditoría completa. |
| `indicator` | Agrega la columna `_merge`. | Cuando necesitas verificar el origen de cada fila. |
| `suffixes` | Distingue columnas repetidas. | Cuando ambas tablas comparten columnas no llave. |

```python
import pandas as pd

df_ventas = pd.DataFrame({
    "sucursal": ["Centro", "Norte", "Sur", "Poniente"],
    "ventas": [120, 95, 140, 80]
}).set_index("sucursal")

df_objetivos = pd.DataFrame({
    "sucursal": ["Centro", "Norte", "Sur", "Oriente"],
    "objetivo": [110, 100, 130, 90]
}).set_index("sucursal")

resultado = pd.merge(
    df_ventas,
    df_objetivos,
    left_index=True,
    right_index=True,
    how="outer",
    indicator=True
)

print(resultado)
# Output:
#            ventas  objetivo     _merge
# sucursal
# Centro     120.0    110.0       both
# Norte       95.0    100.0       both
# Oriente      NaN     90.0  right_only
# Poniente    80.0      NaN  left_only
# Sur        140.0    130.0       both
```

### ¿Por qué sirve esto?

- Porque hace explícito que la unión se basa en el índice.
- Porque `merge()` te permite auditar mejor el resultado cuando comparas tablas con datos faltantes.
- Porque es útil cuando luego quieres escalar a casos con más condiciones de unión.

Ejemplo corto: si ambos índices comparten valores iguales, `merge()` los alinea y construye una sola fila para cada llave común.

Si solo quieres coincidencias completas, usa `how='inner'`.

```python
solo_coincidencias = pd.merge(
    df_ventas,
    df_objetivos,
    left_index=True,
    right_index=True,
    how="inner"
)

print(solo_coincidencias)
```

Este enfoque elimina las llaves que no aparecen en ambas tablas.

---

## 2. Auditar el resultado

`indicator=True` agrega una columna que indica de qué lado vino cada fila.

```python
auditoria = pd.merge(
    df_ventas,
    df_objetivos,
    left_index=True,
    right_index=True,
    how="outer",
    indicator=True
)

print(auditoria["_merge"].value_counts())
```

Valores posibles de `_merge`:

- `left_only`: solo estaba en la tabla izquierda.
- `right_only`: solo estaba en la tabla derecha.
- `both`: estaba en ambas.

---

## 3. ¿Cuándo usar `merge()` por índice?

- Usa `merge()` por índice cuando quieres dejar explícito que la llave está en el índice.
- Usa `outer` cuando necesitas auditar todo lo que sobra en cada tabla.
- Usa `inner` cuando solo quieres resultados completos.
- Usa `indicator=True` cuando necesitas verificar el emparejamiento.

Como regla práctica, pregúntate esto antes de fusionar:

- ¿El índice representa la llave real de la tabla?
- ¿Necesito una auditoría de coincidencias?
- ¿Quiero mantener filas sin pareja o descartarlas?

---

## Errores comunes

1. Olvidar `left_index`/`right_index` y terminar haciendo un merge por columnas por error.

2. Tener índices con tipos distintos: un índice textual no coincide con uno numérico.

3. No usar `indicator=True` cuando quieres auditar filas faltantes.

4. Suponer que `outer` solo devuelve coincidencias: en realidad también conserva llaves exclusivas de cada lado.

5. Ignorar los duplicados en el índice: si el índice no es único, el resultado puede multiplicar filas.
