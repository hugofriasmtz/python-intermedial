# Unión por Derecha

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> En este capítulo profundizamos en `right join`: conservar todo lo de la tabla derecha y combinar columnas de la izquierda cuando haya coincidencias.

---

## Qué haremos

Usaremos el mismo escenario de la biblioteca municipal. La diferencia es que ahora la tabla principal será la derecha: queremos conservar todas las filas de la tabla derecha aunque no tengan pareja en la izquierda.

- **¿Qué pasa si una sede no tiene socio registrado?** -> `how='right'`
- **¿Y si las llaves se llaman distinto?** -> `left_on` / `right_on`
-- **Cómo auditar la unión?** -> `indicator=True`

> [!TIP]
> Aquí el foco es entender el `right join` con casos reales: conservar la tabla principal y manejar llaves/columnas que difieren.

### Idea visual

![Diagrama de union por derecha](https://static.pingcap.com/files/2024/05/23092336/right-outer-join.png)

> [!IMPORTANT]
> Estos parámetros aparecen mucho en proyectos reales porque las tablas no siempre vienen listas para unirlas directamente.
> El tema central aquí es la unión por derecha; los demás parámetros aparecen como apoyo para casos reales.

---

## Qué vas a aprender

- Qué significa exactamente `how='right'`.
- Cómo usar `left_on`/`right_on` cuando las columnas llave difieren.
- Cómo interpretar `_merge` con `indicator=True`.
- Qué ocurre cuando hay duplicados de llave en cualquiera de las tablas.

---

## 1. Unir columnas con nombres distintos

A veces la clave no se llama igual en ambas tablas.

Vamos a trabajar con una biblioteca municipal donde tenemos socios y lectores asignados a diferentes sedes.

### Explicación de los parámetros clave

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `left_on` | Nombre(s) de columna(s) en la tabla izquierda que actúan como llave para la unión. | Cuando la llave tiene distinto nombre entre los DataFrames. |
| `right_on` | Nombre(s) de columna(s) en la tabla derecha que coinciden con `left_on`. | Cuando la llave tiene distinto nombre entre los DataFrames. |
| `on` | Nombre(s) de columna(s) que existen con el mismo nombre en ambas tablas. | Cuando la columna llave comparte nombre en ambos DataFrames (simplifica la llamada). |
| `how` | Tipo de unión. Valores: `'left'`, `'inner'`, `'right'`, `'outer'`. | Elige según si quieres conservar filas de la izquierda, derecha, ambas, o solo coincidencias. |
| `indicator` | Agrega la columna `_merge` indicando el origen de cada fila (`left_only`, `right_only`, `both`). | Para auditar y verificar coincidencias en la unión. |
| `suffixes` | Sufijos para columnas repetidas en ambos DataFrames (ej. `('_socio','_sucursal')`). | Cuando hay columnas no llave con el mismo nombre y quieres diferenciarlas. |

## Ejemplo: biblioteca municipal (derecha principal)

```python
import pandas as pd

df_socios = pd.DataFrame({
    "socio_id": [1, 2, 3, 4, 5],
    "nombre": ["Hugo", "Karen", "Marcos", "Felipe", "Catalina"],
    "ciudad": ["Ciudad de Mexico", "Guadalajara", "Monterrey", "Tijuana", "Merida"]
})

df_sedes = pd.DataFrame({
    "id_socio": [1, 2, 4, 6],
    "sede": ["Centro", "Norte", "Sur", "Oriente"]
})

# Unión por derecha: conserva todas las filas de df_sedes
resultado = df_socios.merge(
    df_sedes,
    left_on="socio_id",
    right_on="id_socio",
    how="right"
)
print(resultado)
# Output esperado:
#    socio_id  nombre             ciudad  id_socio    sede
# 0       1.0    Hugo  Ciudad de Mexico        1   Centro
# 1       2.0   Karen       Guadalajara        2    Norte
# 2       4.0  Felipe           Tijuana        4      Sur
# 3       NaN     NaN               NaN        6  Oriente
```

### ¿Qué pasó aquí?

- `how='right'` conserva todas las filas de la tabla derecha (`df_sedes`). La fila con `id_socio=6` permanece aunque no exista un `socio_id=6` en `df_socios` (las columnas de la izquierda quedan `NaN`).
- Las filas que estaban solo en la izquierda y no tienen pareja en la derecha desaparecen del resultado.
- Si la derecha tiene varias coincidencias para una fila izquierda, esa fila izquierda se repetirá tantas veces como coincidencias.

---

## 2. Ver de dónde vino cada fila

`indicator=True` agrega una columna que muestra si la fila vino de la izquierda, de la derecha o de ambas.

```python
resultado = df_socios.merge(
    df_sedes,
    left_on="socio_id",
    right_on="id_socio",
    how="right",
    indicator=True
)
print(resultado)
# Output esperado (columna _merge):
#    socio_id  nombre             ciudad  id_socio    sede     _merge
# 0       1.0    Hugo  Ciudad de Mexico        1   Centro      both
# 1       2.0   Karen       Guadalajara        2    Norte      both
# 2       4.0  Felipe           Tijuana        4      Sur      both
# 3       NaN     NaN               NaN        6  Oriente  right_only
```

Posibles valores de `_merge`:

- `left_only`: solo estaba en la tabla izquierda.
- `right_only`: solo estaba en la tabla derecha.
- `both`: estaba en ambas.

Este parámetro es muy útil cuando quieres auditar una unión y confirmar que no perdiste registros.

---

## 3. Cuando ambas tablas tienen columnas repetidas

Si dos tablas comparten nombres de columnas que no son la llave, puedes usar `suffixes`.

En este ejemplo ambas tablas tienen una columna llamada `ciudad`.

```python
df_sucursales = pd.DataFrame({
    "socio_id": [1, 2, 4],
    "ciudad": ["Ciudad de Mexico", "Guadalajara", "Tijuana"],
    "area": ["Centro", "Norte", "Sur"]
})

resultado = df_socios.merge(
    df_sucursales,
    on="socio_id",
    how="right",
    suffixes=("_socio", "_sucursal")
)
print(resultado)
# Output:
#    socio_id    nombre   ciudad_socio   ciudad_sucursal    area
# 0         1      Hugo  Ciudad de Mexico  Ciudad de Mexico  Centro
# 1         2     Karen       Guadalajara       Guadalajara   Norte
# 2         3    Marcos         Monterrey               NaN      NaN
# 3         4    Felipe           Tijuana           Tijuana     Sur
```

Esto ayuda a distinguir columnas con el mismo nombre en ambos DataFrames.

Si no usas `suffixes`, pandas te deja nombres ambiguos y luego cuesta leer el resultado.

---

## 4. Cuando usar estos parámetros

- Usa `how='right'` cuando quieras conservar la tabla principal (derecha).
- Usa `left_on` y `right_on` cuando las llaves tienen nombres distintos.
- Usa `indicator=True` cuando quieres auditar el resultado.
- Usa `suffixes` cuando hay columnas repetidas y quieres diferenciarlas.

Como regla práctica, empieza por responder estas preguntas:

- ¿La llave tiene el mismo nombre en ambas tablas?
- ¿Quiero conservar todas las filas de la derecha?
- ¿Necesito saber de dónde salió cada fila?
- ¿Hay columnas repetidas que deban diferenciarse?
