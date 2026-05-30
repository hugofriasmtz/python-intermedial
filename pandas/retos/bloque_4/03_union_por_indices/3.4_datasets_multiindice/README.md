# 3.4 - MultiIndex (índice múltiple)

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En esta lección vas a crear y navegar un `MultiIndex` para representar llaves compuestas. Esto te permite organizar mejor tablas donde una sola columna no basta para identificar cada fila.

---

## ¿Qué haremos?

Tomaremos una tabla con más de una llave natural y la convertiremos en un `MultiIndex`. Luego revisaremos cómo consultar sus niveles, cómo seleccionar filas con `loc` y cómo validar que la combinación sea realmente única.

- **¿Cómo creo un índice múltiple?** -> `set_index([col1, col2])`
- **¿Cómo reviso sus niveles?** -> `index.names` y `index.levels`
- **¿Cómo selecciono una combinación específica?** -> `loc` con tuplas
- **¿Cómo valido que no haya repetidos?** -> `verify_integrity=True`

> [!TIP]
> Cuando una sola llave no alcanza, un `MultiIndex` organiza mejor la información y prepara la tabla para uniones más precisas.

### Idea visual

![Diagrama de indice en pandas](https://pandas.pydata.org/docs/_images/02_04.svg)

> [!IMPORTANT]
> En un `MultiIndex`, el orden de los niveles importa tanto como los nombres de las columnas originales.

---

## ¿Qué vas a aprender?

- Cómo crear un `MultiIndex` con `set_index([col1, col2])`.
- Cómo consultar nombres y niveles con `index.names` e `index.levels`.
- Cómo seleccionar registros con `loc` y una tupla.
- Cómo validar unicidad compuesta con `verify_integrity`.
- Cómo preparar tablas para uniones por índice múltiple.

**Documentación:** [Guía — MultiIndex / Advanced indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html) — [API: pandas.MultiIndex](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.html)

---

## 1. Crear un índice múltiple

Cuando una sola columna no identifica la fila completa, puedes usar dos o más columnas.

Vamos a trabajar con ventas por ciudad y sucursal.

### Parámetros clave

| Parámetro | Qué hace | Cuándo usarlo |
| --- | --- | --- |
| `keys` | Lista de columnas que formarán el índice. | Cuando necesitas una llave compuesta. |
| `verify_integrity` | Verifica que la combinación no esté duplicada. | Cuando la unicidad es obligatoria. |
| `append` | Añade las columnas al índice existente. | Cuando ya tienes un índice y quieres ampliarlo. |
| `drop` | Elimina las columnas originales después del cambio. | Si ya no necesitas ver esas columnas por separado. |

```python
import pandas as pd

df = pd.DataFrame({
    "ciudad": ["Ciudad de México", "Ciudad de México", "Guadalajara", "Guadalajara"],
    "sucursal": ["Centro", "Sur", "Norte", "Poniente"],
    "ventas": [120, 90, 80, 70]
})

multi = df.set_index(["ciudad", "sucursal"])
print(multi)
# Output:
#                               ventas
# ciudad            sucursal
# Ciudad de México  Centro        120
#                   Sur            90
# Guadalajara       Norte          80
#                   Poniente       70
```

### ¿Por qué sirve esto?

- Porque combina dos llaves naturales en una sola estructura de acceso.
- Porque facilita búsquedas más precisas con la pareja completa de valores.
- Porque deja lista la tabla para uniones por índice múltiple.

Ejemplo corto: si quieres una fila específica, puedes buscarla con la combinación exacta de niveles.

```python
print(multi.loc[("Ciudad de México", "Centro")])
```

---

## 2. Revisar niveles y nombres

Cuando trabajas con `MultiIndex`, conviene inspeccionar cómo quedó estructurado.

```python
print(multi.index.names)
print(multi.index.levels)
```

Posibles revisiones útiles:

- `index.names`: muestra el nombre de cada nivel.
- `index.levels`: muestra los valores únicos de cada nivel.
- `index.nlevels`: indica cuántos niveles tiene el índice.

Este paso importa porque un nombre mal puesto o un orden equivocado puede complicar una unión posterior.

---

## 3. ¿Cuándo usar `MultiIndex`?

- Usa `MultiIndex` cuando una sola columna no alcanza para identificar filas.
- Usa `verify_integrity=True` cuando necesitas unicidad estricta.
- Usa `sort_index()` si quieres una lectura más ordenada por niveles.
- Usa `reset_index()` si necesitas volver a columnas planas para exportar o presentar.

Como regla práctica, pregúntate esto antes de crear uno:

- ¿La combinación de columnas identifica la fila de forma única?
- ¿Voy a unir esta tabla con otra que usa la misma secuencia de niveles?
- ¿Me conviene navegar la tabla por tuplas?

---

## Errores comunes

1. Cambiar el orden de los niveles: `("ciudad", "sucursal")` no es igual a `("sucursal", "ciudad")`.

2. Dejar niveles sin nombre: después cuesta interpretar el índice y unirlo con otras tablas.

3. No verificar unicidad compuesta: si hay repetidos, el resultado puede ser ambiguo.

4. Suponer que `loc` acepta cualquier orden: en `MultiIndex`, la tupla debe seguir la secuencia de niveles.

5. Olvidar que un `MultiIndex` también necesita tipos consistentes entre tablas si luego lo vas a unir.
