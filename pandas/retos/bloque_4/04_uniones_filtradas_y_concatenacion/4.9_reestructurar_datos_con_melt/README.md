# 4.9 - Reshaping data with `.melt()`

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La practica consistente transforma lo dificil en dominio. Cada linea de codigo es un paso adelante."

`.melt()` transforma datos de formato ancho (wide) a formato largo (long). Este proceso tambien se conoce como unpivot, porque convierte columnas en filas.

---

## ¿Que haremos?

Partiremos de una tabla financiera en formato ancho y la convertiremos a formato largo con `.melt()`. Luego veremos como conservar columnas fijas, limitar columnas a despivotar y renombrar la salida.

> [!TIP]
> El formato long es ideal para graficos, agrupaciones y modelos que esperan una sola columna de valores.

- **¿Para que sirve `.melt()`?** -> convertir wide a long
- **¿Que columnas permanecen fijas?** -> `id_vars`
- **¿Que columnas se despivotan?** -> `value_vars`
- **¿Como renombro las columnas resultantes?** -> `var_name` y `value_name`

> [!IMPORTANT]
> Si no defines `value_vars`, pandas usa todas las columnas que no esten en `id_vars`.

---

## ¿Que vas a aprender?

- Diferencia entre formato wide y long.
- Uso basico de `.melt()`.
- Uso de `id_vars`, `value_vars`, `var_name` y `value_name`.
- Como controlar la forma final del dataset.

**Documentacion:** [pandas.DataFrame.melt](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.melt.html)

---

## 1. Dataset en formato wide

La tabla de partida tiene una columna por ano.

```python
import pandas as pd

social_fin = pd.DataFrame({
    "financial": ["total_revenue", "gross_profit", "net_income", "total_revenue", "gross_profit", "net_income"],
    "company": ["twitter", "twitter", "twitter", "facebook", "facebook", "facebook"],
    "2019": [3459329, 2322288, 1465659, 70697000, 57927000, 18485000],
    "2018": [3042359, 2077362, 1205596, 55838000, 46483000, 22112000],
    "2017": [2443299, 1582057, -108063, 40653000, 35199000, 15934000],
    "2016": [2529619, 1597379, -456873, 27638000, 23849000, 10217000],
})

print(social_fin)
# Output:
#       financial   company      2019      2018      2017      2016
# 0  total_revenue   twitter   3459329   3042359   2443299   2529619
# 1   gross_profit   twitter   2322288   2077362   1582057   1597379
# 2     net_income   twitter   1465659   1205596   -108063   -456873
# 3  total_revenue  facebook  70697000  55838000  40653000  27638000
# 4   gross_profit  facebook  57927000  46483000  35199000  23849000
# 5     net_income  facebook  18485000  22112000  15934000  10217000
```

---

## 2. Ejemplo base de `.melt()`

Al convertir la tabla a formato long, los anos pasan a una columna de variables.

```python
social_fin_tall = social_fin.melt(id_vars=["financial", "company"])
print(social_fin_tall.head(10))
# Output:
#       financial   company variable     value
# 0  total_revenue   twitter     2019   3459329
# 1   gross_profit   twitter     2019   2322288
# 2     net_income   twitter     2019   1465659
# 3  total_revenue  facebook     2019  70697000
# 4   gross_profit  facebook     2019  57927000
# 5     net_income  facebook     2019  18485000
# 6  total_revenue   twitter     2018   3042359
# 7   gross_profit   twitter     2018   2077362
# 8     net_income   twitter     2018   1205596
# 9  total_revenue  facebook     2018  55838000
```

Este formato es mas facil de agrupar y graficar.

---

## 3. Melting con `value_vars`

Si solo te interesan algunos anos, puedes limitar las columnas a despivotar.

```python
social_fin_tall = social_fin.melt(
    id_vars=["financial", "company"],
    value_vars=["2018", "2017"],
)
print(social_fin_tall.head(9))
# Output:
#       financial   company variable     value
# 0  total_revenue   twitter     2018   3042359
# 1   gross_profit   twitter     2018   2077362
# 2     net_income   twitter     2018   1205596
# 3  total_revenue  facebook     2018  55838000
# 4   gross_profit  facebook     2018  46483000
# 5     net_income  facebook     2018  22112000
# 6  total_revenue   twitter     2017   2443299
# 7   gross_profit   twitter     2017   1582057
# 8     net_income   twitter     2017   -108063
```

---

## 4. Renombrar columnas de salida

Para que el resultado sea mas descriptivo, puedes cambiar `variable` y `value`.

```python
social_fin_tall = social_fin.melt(
    id_vars=["financial", "company"],
    value_vars=["2018", "2017"],
    var_name="year",
    value_name="dollars",
)
print(social_fin_tall.head(8))
# Output:
#       financial   company  year   dollars
# 0  total_revenue   twitter  2018   3042359
# 1   gross_profit   twitter  2018   2077362
# 2     net_income   twitter  2018   1205596
# 3  total_revenue  facebook  2018  55838000
# 4   gross_profit  facebook  2018  46483000
# 5     net_income  facebook  2018  22112000
# 6  total_revenue   twitter  2017   2443299
# 7   gross_profit   twitter  2017   1582057
```

---

## 5. ¿Cuándo usar `.melt()`?

- Cuando tus variables estan en columnas y quieres analizarlas por fila.
- Cuando necesitas normalizar un dataset wide para visualizacion o modelado.
- Cuando quieres combinar facilmente con otras tablas en formato long.

---

## Errores comunes

1. Olvidar `id_vars` y perder columnas clave.
2. Elegir `value_vars` incorrectas.
3. No renombrar `variable` y `value` cuando el contexto lo pide.
4. Suponer que `.melt()` modifica el DataFrame original en sitio.
