# 3.5 - Merge con MultiIndex

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En esta lección vas a unir dos tablas que usan `MultiIndex` como llave compuesta. Aquí lo importante es que ambos niveles coincidan en orden, nombre y tipo para que la fusión funcione de forma predecible.

---

## ¿Qué haremos?

Tomaremos dos tablas con índice múltiple y las fusionaremos con `merge()` usando `left_index=True` y `right_index=True`. Después auditaremos el resultado para ver qué llaves coincidieron y cuáles quedaron solo en un lado.

- **¿Cómo uno dos MultiIndex?** -> `left_index=True` y `right_index=True`
- **¿Cómo audito coincidencias?** -> `indicator=True`
- **¿Qué pasa si falta una llave compuesta?** -> `how='outer'`
- **¿Cómo evito errores por orden de niveles?** -> revisar secuencia y nombres

> [!TIP]
> Con `MultiIndex`, una unión correcta depende tanto del contenido como del orden de los niveles.

> [!IMPORTANT]
> Si los niveles no coinciden exactamente, pandas no podrá emparejar correctamente las filas.

---

## ¿Qué vas a aprender?

- Cómo unir tablas con índice múltiple usando `left_index` y `right_index`.
- Cómo detectar filas `left_only`, `right_only` y `both` con `_merge`.
- Cómo verificar el alineamiento y el orden de niveles.
- Cómo normalizar tipos antes de unir.
- Cómo interpretar resultados con llaves compuestas faltantes.

**Documentación:** [Guía — MultiIndex / Advanced indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html) — [API: pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Fusionar tablas con `MultiIndex`

La unión funciona mejor cuando ambos DataFrames tienen la misma estructura de índices.

Vamos a usar ventas y objetivos por ciudad y sucursal.

### Parámetros clave

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `left_index` | Usa el índice del DataFrame izquierdo como llave. | Cuando el izquierdo tiene `MultiIndex`. |
| `right_index` | Usa el índice del DataFrame derecho como llave. | Cuando el derecho también tiene `MultiIndex`. |
| `how` | Define el tipo de unión. | Para conservar coincidencias, auditar llaves o limitar el resultado. |
| `indicator` | Agrega `_merge`. | Para ver qué filas vinieron de cada lado. |

```python
import pandas as pd

df_ventas = pd.DataFrame({
    "ciudad": ["Ciudad de México", "Ciudad de México", "Guadalajara", "Guadalajara"],
    "sucursal": ["Centro", "Sur", "Norte", "Poniente"],
    "ventas": [120, 90, 80, 70]
}).set_index(["ciudad", "sucursal"])

df_objetivos = pd.DataFrame({
    "ciudad": ["Ciudad de México", "Ciudad de México", "Guadalajara", "Mérida"],
    "sucursal": ["Centro", "Sur", "Norte", "Centro"],
    "objetivo": [110, 95, 85, 60]
}).set_index(["ciudad", "sucursal"])

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
#                             ventas  objetivo     _merge
# ciudad            sucursal
# Ciudad de México  Centro      120.0    110.0       both
#                   Sur         90.0     95.0       both
# Guadalajara       Norte       80.0     85.0       both
#                   Poniente    70.0      NaN  left_only
# Mérida            Centro       NaN     60.0  right_only
```

### ¿Por qué sirve esto?

- Porque permite unir llaves compuestas sin aplanar el índice primero.
- Porque deja claro qué combinaciones existen en ambas tablas.
- Porque ayuda a detectar rápidamente llaves compuestas faltantes.

Ejemplo corto: si una combinación de ciudad y sucursal no existe en una tabla, aparecerá como `left_only` o `right_only` según el lado.

---

## 2. Revisar compatibilidad de niveles

Antes de unir, conviene comprobar que ambos `MultiIndex` estén alineados.

```python
print(df_ventas.index.names)
print(df_objetivos.index.names)
print(df_ventas.index.nlevels)
```

Posibles revisiones útiles:

- `index.names`: confirma que los nombres de los niveles coincidan.
- `index.nlevels`: confirma que ambos tengan la misma cantidad de niveles.
- `index.is_unique`: confirma que cada combinación sea única.

---

## 3. ¿Cuándo usar `merge()` con `MultiIndex`?

- Usa `outer` cuando quieres auditar todas las combinaciones.
- Usa `inner` cuando solo te interesan coincidencias completas.
- Usa `indicator=True` para revisar el origen de cada fila.
- Usa `astype()` si necesitas normalizar tipos antes de unir.

Como regla práctica, pregúntate esto antes de fusionar:

- ¿Los niveles tienen el mismo orden en ambas tablas?
- ¿Los nombres de los niveles coinciden?
- ¿Las combinaciones de niveles son únicas?

---

## Errores comunes

1. Cambiar el orden de los niveles: un `MultiIndex` solo coincide bien si la secuencia es la misma.

2. Tener tipos distintos en un nivel: por ejemplo, texto en un lado y números en el otro.

3. No verificar unicidad compuesta: las combinaciones repetidas generan resultados ambiguos.

4. Olvidar `indicator=True` cuando quieres auditar filas faltantes.

5. Asumir que `outer` solo conserva coincidencias: también deja las llaves exclusivas de cada lado.
