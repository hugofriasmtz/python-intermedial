# 3.2 - Unir datasets que comparten índice

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En esta parte vas a unir dos DataFrames que ya tienen la llave en el índice. La idea es entender cuándo `join()` es suficiente, cómo controlar coincidencias parciales y cómo evitar confusiones cuando ambas tablas comparten nombres de columnas.

---

## ¿Qué haremos?

Tomaremos dos tablas indexadas por la misma llave y las combinaremos con `join()`. Después veremos cómo detectar filas sin coincidencia, cómo elegir el tipo de unión y cómo aplicar sufijos si aparecen columnas repetidas.

- **¿Cómo uno tablas que ya tienen índice?** -> `join()`
- **¿Qué pasa si faltan filas en una de las tablas?** -> `how='left'`, `how='outer'`
- **¿Cómo distingo columnas repetidas?** -> `lsuffix` y `rsuffix`
- **¿Cómo reviso si la llave quedó bien indexada?** -> `index.is_unique`

> [!TIP]
> Si ambas tablas ya comparten el índice, `join()` suele ser la forma más directa de combinarlas.

### Idea visual

![Diagrama de union por izquierda](https://static.pingcap.com/files/2024/05/23092316/left-outer-join.png)

> [!IMPORTANT]
> Cuando la llave vive en el índice, la alineación de filas importa tanto como el contenido de las columnas.

---

## ¿Qué vas a aprender?

- Cómo usar `join()` para combinar tablas indexadas.
- Cómo elegir entre `left`, `right`, `inner` y `outer`.
- Cómo aplicar `lsuffix`/`rsuffix` cuando hay columnas repetidas.
- Cómo detectar `NaN` resultantes de llaves sin coincidencia.
- Cómo validar que el índice sea único antes de unir.

**Documentación:** [Guía — Merge, join y concatenate](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) — [API: pandas.DataFrame.join](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.join.html)

---

## 1. Unir tablas con el mismo índice

La forma más simple de combinar dos tablas indexadas es dejar que pandas alinee las filas por el índice.

Vamos a trabajar con socios de una biblioteca municipal.

### Parámetros clave de `join()`

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `other` | DataFrame que se va a unir al DataFrame principal. | Cuando ya tienes la otra tabla lista para alinear por índice. |
| `how` | Tipo de unión: `left`, `right`, `inner`, `outer`. | Cuando quieres conservar filas de una tabla, de ambas o solo coincidencias. |
| `lsuffix` | Sufijo para columnas repetidas del DataFrame izquierdo. | Cuando ambas tablas comparten columnas no llave. |
| `rsuffix` | Sufijo para columnas repetidas del DataFrame derecho. | Cuando ambas tablas comparten columnas no llave. |
| `sort` | Ordena el índice del resultado. | Cuando necesitas una salida ordenada para leer o comparar. |

```python
import pandas as pd

df_base = pd.DataFrame({
    "socio_id": [1, 2, 3, 4, 5],
    "nombre": ["Hugo", "Karen", "Marcos", "Felipe", "Catalina"]
}).set_index("socio_id")

df_ciudad = pd.DataFrame({
    "socio_id": [1, 2, 4, 6],
    "ciudad": ["Ciudad de México", "Guadalajara", "Tijuana", "Mérida"]
}).set_index("socio_id")

resultado = df_base.join(df_ciudad, how="left")
print(resultado)
# Output:
#            nombre           ciudad
# socio_id
# 1           Hugo  Ciudad de México
# 2          Karen       Guadalajara
# 3         Marcos              NaN
# 4         Felipe           Tijuana
# 5       Catalina              NaN
```

### ¿Por qué sirve esto?

- Porque pandas alinea directamente por el índice sin que tengas que repetir la llave como columna.
- Porque `join()` es cómodo cuando el índice ya representa la identidad de cada fila.
- Porque te deja unir varias tablas indexadas con menos ruido que un `merge()` equivalente.

Ejemplo corto: si `df_base.index` y `df_ciudad.index` contienen la misma llave, `join()` empareja filas con el mismo valor de índice.

Si quieres revisar todas las llaves posibles, usa `how='outer'`.

```python
auditoria = df_base.join(df_ciudad, how="outer")
print(auditoria)
# Output:
#            nombre           ciudad
# socio_id
# 1           Hugo  Ciudad de México
# 2          Karen       Guadalajara
# 3         Marcos              NaN
# 4         Felipe           Tijuana
# 5       Catalina              NaN
# 6            NaN            Mérida
```

Este enfoque ayuda a detectar rápidamente qué llaves faltan en cada tabla.

---

## 2. Resolver columnas repetidas

Si ambas tablas comparten nombres de columnas que no son la llave, puedes aplicar sufijos para evitar ambigüedad.

```python
df_detalle = pd.DataFrame({
    "socio_id": [1, 2, 4],
    "nombre": ["Hugo A.", "Karen B.", "Felipe C."],
    "estado": ["Activo", "Activo", "Pendiente"]
}).set_index("socio_id")

resultado = df_base.join(
    df_detalle,
    how="left",
    lsuffix="_base",
    rsuffix="_detalle"
)
print(resultado)
```

Si el nombre de la columna se repite, los sufijos dejan claro de qué tabla viene cada valor.

---

## 3. ¿Cuándo usar `join()`?

- Usa `join()` cuando la llave ya está en el índice.
- Usa `outer` cuando quieres auditar todas las llaves de ambas tablas.
- Usa `inner` cuando solo te interesan coincidencias completas.
- Usa `lsuffix` y `rsuffix` si hay columnas repetidas.

Como regla práctica, pregúntate esto antes de unir:

- ¿Las dos tablas ya están indexadas por la misma llave?
- ¿Quiero conservar solo la tabla izquierda o auditar todas las llaves?
- ¿Existen columnas con el mismo nombre que deban diferenciarse?

---

## Errores comunes

1. Unir índices con tipos distintos: un índice numérico no coincide con uno de texto. Conviene normalizar con `astype` antes de unir.

2. Tener índices duplicados: si no son únicos, el resultado puede repetir filas. Revisa `index.is_unique` antes de continuar.

3. Olvidar los sufijos: cuando ambas tablas comparten columnas, el resultado se vuelve confuso sin `lsuffix` y `rsuffix`.

4. Elegir `left` cuando esperabas ver llaves faltantes: si quieres auditar todo, usa `outer`.

5. Asumir que `join()` usa columnas: `join()` alinea por índice, no por columnas comunes.
