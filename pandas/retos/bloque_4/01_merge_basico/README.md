# 01 - Merge Básico

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

En las operaciones de `merge` importa el valor de la llave y qué filas se conservan o quedan sin emparejar. En esta lección aprenderás a usar `pd.merge()` para combinar tablas, distinguir `inner` de `left` y cómo interpretar los `NaN` cuando faltan coincidencias.

---

## ¿Qué haremos?

Aprenderás a unir dos tablas cuando comparten una columna común. Este es el caso más básico y más importante de `merge()` y también el punto de partida para entender por qué una unión a la izquierda conserva la tabla principal.

Antes de unir tablas, piensa en esto:

-- Una tabla tiene los datos principales (izquierda).
-- La otra tabla aporta información relacionada (derecha).
-- La columna común es la llave que conecta ambas tablas.
-- El resultado puede conservar solo coincidencias o todas las filas de una tabla.

- **¿Cómo uno dos tablas por un ID?** -> `pd.merge(..., on='id')`
- **¿Qué pasa si ambas tablas tienen filas que coinciden?** -> `how='inner'`
- **¿Cómo conservo todas las filas de una tabla principal?** -> `how='left'`

> [!IMPORTANT]
> `merge()` por defecto hace un `inner join`: solo deja las filas que existen en ambas tablas.

### Idea visual

![Diagrama de union tipo merge](https://static.pingcap.com/files/2024/05/23092234/inner-join.png)

---

## ¿Qué vas a aprender?

- Qué hace `pd.merge()`.
- Para qué sirve el parámetro `on`.
- La diferencia entre `inner` y `left` en una unión simple.
- Cómo leer el resultado de una tabla combinada.
- Cómo interpretar una salida de consola fila por fila.

**Documentación:** [merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)

---

## 1. Unir dos tablas con una llave común

Cuando dos tablas comparten una columna como `socio_id` (la llave), puedes unirlas con `merge()`.

En este ejemplo usamos una biblioteca municipal con socios y prestamos.

```python
import pandas as pd

df_socios = pd.DataFrame({
    "socio_id": [1, 2, 3, 4, 5],
    "nombre": ["Hugo", "Karen", "Marcos", "Felipe", "Catalina"],
    "ciudad": ["Ciudad de México", "Guadalajara", "Monterrey", "Tijuana", "Mérida"]
})

df_prestamos = pd.DataFrame({
    "socio_id": [1, 2, 4, 6],
    "libro": ["Cien años de soledad", "La sombra del viento", "Rayuela", "El principito"],
    "dias_prestamo": [7, 14, 10, 5]
})

resultado = df_socios.merge(df_prestamos, on="socio_id")
print(resultado)
# Output:
#    socio_id    nombre             ciudad                  libro  dias_prestamo
# 0         1      Hugo  Ciudad de México  Cien años de soledad              7
# 1         2     Karen       Guadalajara   La sombra del viento             14
# 2         4    Felipe           Tijuana                 Rayuela             10
```

### ¿Por qué usarlo?

- Porque te permite juntar información que está separada en dos tablas.
- Porque evita copiar datos manualmente.
- Porque funciona muy bien cuando tienes una llave común.

### Lo que pasó aquí

- La fila con `socio_id = 1` aparece en ambas tablas, por eso se conserva.
- La fila con `socio_id = 2` también aparece en ambas tablas, por eso se conserva.
- La fila con `socio_id = 4` también aparece en ambas tablas, por eso se conserva.
- La fila con `socio_id = 3` no tiene préstamo y no aparece en un `inner join`.
- La fila con `socio_id = 5` tampoco aparece porque no tiene préstamo.
- La fila con `socio_id = 6` está solo en préstamos y tampoco aparece.

---

## 2. Tipos de union basicos

Esta tabla resume lo esencial:

| Tipo | Que conserva |
| --- | --- |
| `inner` | Solo las filas que coinciden en ambas tablas |
| `left` | Todas las filas de la tabla izquierda |
| `right` | Todas las filas de la tabla derecha |
| `outer` | Todas las filas de ambas tablas |

### `inner`

Conserva solo las filas que aparecen en ambas tablas.

```python
resultado = df_socios.merge(df_prestamos, on="socio_id", how="inner")
print(resultado)
# Output:
#    socio_id    nombre             ciudad                  libro  dias_prestamo
# 0         1      Hugo  Ciudad de Mexico  Cien anios de soledad              7
# 1         2     Karen       Guadalajara   La sombra del viento             14
# 2         4    Felipe           Tijuana                 Rayuela             10
```

### `left`

Conserva todas las filas de la tabla izquierda y agrega lo que encuentre en la derecha.

```python
resultado = df_socios.merge(df_prestamos, on="socio_id", how="left")
print(resultado)
# Output:
#    socio_id    nombre             ciudad                  libro  dias_prestamo
# 0         1      Hugo  Ciudad de México  Cien años de soledad            7.0
# 1         2     Karen       Guadalajara   La sombra del viento           14.0
# 2         3    Marcos         Monterrey                    NaN            NaN
# 3         4    Felipe           Tijuana                 Rayuela           10.0
# 4         5  Catalina           Mérida                    NaN            NaN
```

### `right`

Conserva todas las filas de la tabla derecha.

```python
resultado = df_socios.merge(df_prestamos, on="socio_id", how="right")
print(resultado)
# Output:
#    socio_id nombre             ciudad                  libro  dias_prestamo
# 0         1   Hugo  Ciudad de México  Cien años de soledad              7
# 1         2  Karen       Guadalajara   La sombra del viento             14
# 2         4 Felipe           Tijuana                 Rayuela             10
# 3         6    NaN               NaN          El principito              5
```

### `outer`

Conserva todas las filas de ambas tablas.

```python
resultado = df_socios.merge(df_prestamos, on="socio_id", how="outer")
print(resultado)
# Output:
#    socio_id    nombre             ciudad                  libro  dias_prestamo
# 0         1      Hugo  Ciudad de México  Cien años de soledad            7.0
# 1         2     Karen       Guadalajara   La sombra del viento           14.0
# 2         3    Marcos         Monterrey                    NaN            NaN
# 3         4    Felipe           Tijuana                 Rayuela           10.0
# 4         5  Catalina           Mérida                    NaN            NaN
# 5         6       NaN               NaN          El principito            5.0
```

---

## 3. ¿Cuándo usar cada uno?

- Usa `inner` cuando solo te interesan coincidencias completas.
- Usa `left` cuando tu tabla principal es la primera.
- Usa `right` cuando tu tabla principal es la segunda.
- Usa `outer` cuando no quieres perder ninguna fila.

Si tu objetivo es analizar socios y no perder ninguno aunque no tenga prestamo, `left` suele ser la mejor opcion.

---

## 4. Error común

Si las columnas no tienen el mismo nombre, `on` no alcanza. En ese caso necesitas otro capítulo para `left_on` y `right_on`.

También hay que cuidar que la llave no repita demasiadas veces, porque eso puede multiplicar filas.

---

## Errores comunes

1. Tipos de dato distintos en la columna llave (ej. `int` vs `str`): impide coincidencias y genera demasiados `NaN`.

2. Usar `on` cuando las llaves tienen nombres distintos (usa `left_on`/`right_on`).

3. Llaves duplicadas sin control: pueden multiplicar filas inesperadamente.

4. Olvidar `suffixes` cuando hay columnas no llave con el mismo nombre, lo que genera columnas ambiguas.

5. No auditar la unión con `indicator=True` ni revisar `head()`/`info()` tras el `merge`, lo que puede dejar `NaN` sin detectar.
