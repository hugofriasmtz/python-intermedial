# 4.6 - Using merge_ordered()

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La practica consistente transforma lo dificil en dominio. Cada linea de codigo es un paso adelante."

`merge_ordered()` esta pensado para datos ordenados, especialmente series de tiempo. A diferencia de `merge()`, su enfoque natural es preservar el orden y permitir relleno de valores faltantes.

---

## ¿Que haremos?

Vamos a comparar `merge()` con `merge_ordered()` y luego veremos como completar vacios con `fill_method='ffill'`.

> [!TIP]
> Si el eje temporal importa, `merge_ordered()` suele ser mejor que un merge normal.

- **¿Cuando conviene `merge_ordered()`?** -> datos ordenados por fecha o secuencia
- **¿Cual es su `how` por defecto?** -> `outer`
- **¿Como rellenar faltantes?** -> `fill_method='ffill'`

> [!IMPORTANT]
> Ordena la columna temporal antes de usar este metodo.

---

## ¿Que vas a aprender?

- Unir datos ordenados con `pd.merge_ordered()`.
- Usar `suffixes` para columnas repetidas.
- Rellenar faltantes con `fill_method='ffill'`.
- Reconocer cuando este metodo supera a `merge()`.

**Documentacion:** [pandas.merge_ordered](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge_ordered.html)

---

## 1. Merge ordered basico

La forma mas directa de verlo es con dos tablas de precios ordenadas por fecha.

```python
import pandas as pd

aapl = pd.DataFrame({
    "date": ["2007-02-01", "2007-03-01", "2007-04-01", "2007-05-01", "2007-06-01"],
    "close": [12.087143, 13.272857, 14.257143, 17.312857, 17.434286],
})

mcd = pd.DataFrame({
    "date": ["2007-01-01", "2007-02-01", "2007-03-01", "2007-04-01", "2007-05-01"],
    "close": [44.349998, 43.689999, 45.049999, 48.279999, 50.549999],
})

stocks = pd.merge_ordered(aapl, mcd, on="date", suffixes=("_aapl", "_mcd"))
print(stocks)
# Output:
#          date  close_aapl  close_mcd
# 0  2007-01-01         NaN  44.349998
# 1  2007-02-01   12.087143  43.689999
# 2  2007-03-01   13.272857  45.049999
# 3  2007-04-01   14.257143  48.279999
# 4  2007-05-01   17.312857  50.549999
# 5  2007-06-01   17.434286        NaN
```

### ¿Por que sirve esto?

- Porque conserva el orden temporal.
- Porque permite ver vacios en ambos lados.
- Porque ayuda a unir series que no tienen exactamente las mismas fechas.

---

## 2. Completar valores faltantes

Si quieres arrastrar el ultimo valor conocido hacia adelante, usa `ffill`.

```python
stocks_ffill = pd.merge_ordered(
    aapl,
    mcd,
    on="date",
    suffixes=("_aapl", "_mcd"),
    fill_method="ffill",
)
print(stocks_ffill)
# Output:
#          date  close_aapl  close_mcd
# 0  2007-01-01         NaN  44.349998
# 1  2007-02-01   12.087143  43.689999
# 2  2007-03-01   13.272857  45.049999
# 3  2007-04-01   14.257143  48.279999
# 4  2007-05-01   17.312857  50.549999
# 5  2007-06-01   17.434286  50.549999
```

Este patron es util cuando el ultimo valor conocido sigue siendo valido para el siguiente registro.

---

## 3. ¿Cuándo usar `merge_ordered()`?

- En series de tiempo.
- Cuando tus datos ya siguen un orden natural.
- Cuando necesitas completar huecos con `ffill`.

Como regla practica, preguntate esto antes de unir:

- ¿El orden temporal importa?
- ¿Quiero mantener todos los valores aunque falten fechas?
- ¿Tiene sentido arrastrar el ultimo dato conocido?

---

## Errores comunes

1. Usarlo con datos no ordenados sin revisar la salida.
2. Aplicar `ffill` donde no tiene sentido.
3. Olvidar `suffixes` en columnas repetidas.
4. Esperar una union exacta en lugar de una union ordenada.
