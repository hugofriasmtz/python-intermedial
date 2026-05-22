# 01 - Merge Basico

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La practica consistente transforma lo dificil en dominio. Cada linea de codigo es un paso adelante."

---

## Que haremos

Aprenderas a unir dos tablas cuando comparten una columna comun. Este es el caso mas basico y mas importante de `merge()` y tambien el punto de partida para entender por que una union a la izquierda conserva la tabla principal.

Antes de unir tablas, piensa en esto:

- Una tabla tiene datos de la parte izquierda del problema.
- La otra tabla agrega informacion relacionada.
- La columna comun es la llave que conecta ambas tablas.
- El resultado puede conservar solo coincidencias o todas las filas de una tabla.

- **¿Como uno dos tablas por un ID?** -> `pd.merge(..., on='id')`
- **¿Que pasa si ambas tablas tienen filas que coinciden?** -> `how='inner'`
- **¿Como conservo todas las filas de una tabla principal?** -> `how='left'`

> [!IMPORTANT]
> `merge()` por defecto hace un `inner join`: solo deja las filas que existen en ambas tablas.

### Idea visual

![Diagrama de union tipo merge](https://static.pingcap.com/files/2024/05/23092234/inner-join.png)

---

## Que vas a aprender

- Que hace `pd.merge()`.
- Para que sirve el parametro `on`.
- La diferencia entre `inner` y `left` en una union simple.
- Como leer el resultado de una tabla combinada.
- Como interpretar una salida de consola fila por fila.

---

## 1. Unir dos tablas con una clave comun

Cuando dos tablas comparten una columna como `socio_id`, puedes unirlas con `merge()`.

En este ejemplo usamos una biblioteca municipal con socios y prestamos.

```python
import pandas as pd

df_socios = pd.DataFrame({
    "socio_id": [1, 2, 3, 4, 5],
    "nombre": ["Hugo", "Karen", "Marcos", "Felipe", "Catalina"],
    "ciudad": ["Ciudad de Mexico", "Guadalajara", "Monterrey", "Tijuana", "Merida"]
})

df_prestamos = pd.DataFrame({
    "socio_id": [1, 2, 4, 6],
    "libro": ["Cien anios de soledad", "La sombra del viento", "Rayuela", "El principito"],
    "dias_prestamo": [7, 14, 10, 5]
})

resultado = df_socios.merge(df_prestamos, on="socio_id")
print(resultado)
# Output:
#    socio_id    nombre             ciudad                  libro  dias_prestamo
# 0         1      Hugo  Ciudad de Mexico  Cien anios de soledad              7
# 1         2     Karen       Guadalajara   La sombra del viento             14
# 2         4    Felipe           Tijuana                 Rayuela             10
```

### ¿Por que usarlo?

- Porque te permite juntar informacion que esta separada en dos tablas.
- Porque evita copiar datos manualmente.
- Porque funciona muy bien cuando tienes una llave comun.

### Lo que paso aqui

- La fila con `socio_id = 1` aparece en ambas tablas, por eso se conserva.
- La fila con `socio_id = 2` tambien aparece en ambas tablas, por eso se conserva.
- La fila con `socio_id = 4` tambien aparece en ambas tablas, por eso se conserva.
- La fila con `socio_id = 3` no tiene prestamo y no aparece en un `inner join`.
- La fila con `socio_id = 5` tampoco aparece porque no tiene prestamo.
- La fila con `socio_id = 6` esta solo en prestamos y tampoco aparece.

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
# 0         1      Hugo  Ciudad de Mexico  Cien anios de soledad            7.0
# 1         2     Karen       Guadalajara   La sombra del viento           14.0
# 2         3    Marcos         Monterrey                    NaN            NaN
# 3         4    Felipe           Tijuana                 Rayuela           10.0
# 4         5  Catalina           Merida                    NaN            NaN
```

### `right`

Conserva todas las filas de la tabla derecha.

```python
resultado = df_socios.merge(df_prestamos, on="socio_id", how="right")
print(resultado)
# Output:
#    socio_id nombre             ciudad                  libro  dias_prestamo
# 0         1   Hugo  Ciudad de Mexico  Cien anios de soledad              7
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
# 0         1      Hugo  Ciudad de Mexico  Cien anios de soledad            7.0
# 1         2     Karen       Guadalajara   La sombra del viento           14.0
# 2         3    Marcos         Monterrey                    NaN            NaN
# 3         4    Felipe           Tijuana                 Rayuela           10.0
# 4         5  Catalina           Merida                    NaN            NaN
# 5         6       NaN               NaN          El principito            5.0
```

---

## 3. Cuando usar cada uno

- Usa `inner` cuando solo te interesan coincidencias completas.
- Usa `left` cuando tu tabla principal es la primera.
- Usa `right` cuando tu tabla principal es la segunda.
- Usa `outer` cuando no quieres perder ninguna fila.

Si tu objetivo es analizar socios y no perder ninguno aunque no tenga prestamo, `left` suele ser la mejor opcion.

---

## 4. Error comun

Si las columnas no tienen el mismo nombre, `on` no alcanza. En ese caso necesitas otro capitulo para `left_on` y `right_on`.

Tambien hay que cuidar que la llave no repita demasiadas veces, porque eso puede multiplicar filas.

---
