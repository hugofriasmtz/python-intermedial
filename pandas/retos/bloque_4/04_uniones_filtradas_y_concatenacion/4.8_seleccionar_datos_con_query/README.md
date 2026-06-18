# 4.8 - Selecting data with .query()

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La practica consistente transforma lo dificil en dominio. Cada linea de codigo es un paso adelante."

El metodo `.query()` permite filtrar filas usando una expresion en texto. Es similar a una clausula `WHERE` de SQL, pero no necesitas experiencia previa en SQL para usarla.

---

## ¿Que haremos?

Aplicaremos `.query()` en condiciones simples, condiciones multiples (`and` y `or`) y filtros por texto.

> [!TIP]
> `.query()` vuelve mas legibles filtros largos cuando comparas varias columnas.

- **¿Que recibe `query()`?** -> una cadena con la condicion
- **¿Como filtro por una sola condicion?** -> `df.query('columna >= valor')`
- **¿Como combino condiciones?** -> `and`, `or` y parentesis
- **¿Como filtro texto?** -> comparaciones como `stock == "disney"`

> [!IMPORTANT]
> Si hay espacios en nombres de columna, usa comillas invertidas en la expresion.

---

## ¿Que vas a aprender?

- Filtros simples con `.query()`.
- Combinaciones con `and` y `or`.
- Filtros por texto con parentesis para prioridad logica.

**Documentacion:** [pandas.DataFrame.query](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html)

---

## 1. Condicion simple

Empezamos con una tabla de acciones y una sola condicion.

```python
import pandas as pd

stocks = pd.DataFrame({
    "date": [
        "2019-07-01", "2019-08-01", "2019-09-01", "2019-10-01", "2019-11-01",
        "2019-12-01", "2020-01-01", "2020-02-01", "2020-03-01", "2020-04-01",
    ],
    "disney": [143.009995, 137.259995, 130.320007, 129.919998, 151.580002, 144.630005, 138.309998, 117.650002, 96.599998, 99.580002],
    "nike": [86.029999, 84.5, 93.919998, 89.550003, 93.489998, 101.309998, 96.300003, 89.379997, 82.739998, 84.629997],
})

print(stocks.query("nike >= 90"))
# Output:
#          date      disney        nike
# 2  2019-09-01  130.320007   93.919998
# 4  2019-11-01  151.580002   93.489998
# 5  2019-12-01  144.630005  101.309998
# 6  2020-01-01  138.309998   96.300003
```

### ¿Por que sirve esto?

- Porque deja claro que quieres solo filas que cumplan una expresion.
- Porque la sintaxis es compacta y legible.
- Porque se parece a filtrar por `WHERE` en SQL.

---

## 2. Multiples condiciones

Cuando necesitas mas de una regla, `.query()` permite usar `and` y `or`.

```python
print(stocks.query("nike > 90 and disney < 140"))
# Output:
#          date      disney       nike
# 2  2019-09-01  130.320007  93.919998
# 6  2020-01-01  138.309998  96.300003

print(stocks.query("nike > 96 or disney < 98"))
# Output:
#          date      disney        nike
# 5  2019-12-01  144.630005  101.309998
# 6  2020-01-01  138.309998   96.300003
# 8  2020-03-01   96.599998   82.739998
```

Si la logica mezcla varias condiciones, usa parentesis para que la expresion quede bien definida.

---

## 3. Seleccion por texto

Tambien puedes filtrar texto dentro de `.query()`.

```python
stocks_long = pd.DataFrame({
    "date": ["2019-07-01", "2019-08-01", "2019-09-01", "2019-10-01", "2019-11-01", "2019-07-01", "2019-08-01", "2019-09-01", "2019-10-01", "2019-11-01"],
    "stock": ["disney", "disney", "disney", "disney", "disney", "nike", "nike", "nike", "nike", "nike"],
    "close": [143.009995, 137.259995, 130.320007, 129.919998, 151.580002, 86.029999, 84.5, 93.919998, 89.550003, 93.489998],
})

print(stocks_long.query('stock == "disney" or (stock == "nike" and close < 90)'))
# Output:
#          date   stock       close
# 0  2019-07-01  disney  143.009995
# 1  2019-08-01  disney  137.259995
# 2  2019-09-01  disney  130.320007
# 3  2019-10-01  disney  129.919998
# 4  2019-11-01  disney  151.580002
# 5  2019-07-01    nike   86.029999
# 6  2019-08-01    nike   84.500000
# 8  2019-10-01    nike   89.550003
```

Este ejemplo muestra como conservar todas las filas de `disney` y solo algunas filas de `nike`.

---

## 4. ¿Cuando usar `.query()`?

- Cuando quieres filtros legibles en una sola linea.
- Cuando combinas varias condiciones logicas.
- Cuando prefieres expresiones de texto en lugar de mascaras largas.

Como regla practica, preguntate esto antes de filtrar:

- ¿La expresion es mas clara que una mascara booleana?
- ¿Necesito combinar `and` y `or`?
- ¿Estoy filtrando texto o numeros?

---

## Errores comunes

1. Confundir `=` con `==` dentro de la expresion.
2. Olvidar comillas para comparar texto.
3. No usar parentesis cuando la logica es compuesta.
4. Escribir nombres de columna incorrectos en la cadena.
