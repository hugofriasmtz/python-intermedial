# 01 - Cargar Datos Basicos

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Antes de analizar datos, necesitas:

1. **Cargar el archivo** (`pd.read_csv()`): lee un CSV y lo convierte en DataFrame
2. **Inspeccionar las primeras filas** (`head()`): ve qué datos hay sin abrumaarte
3. **Revisar el tamaño** (`shape`): cuántas filas y columnas tiene
4. **Entender tipos de dato** (`dtypes`): qué tipo es cada columna (números, texto, fechas, etc.)

Estos pasos son **esenciales** antes de cualquier análisis.

> [!TIP]
> `head()` es tu amigo: siempre revisa las primeras filas después de cargar un archivo.

---

## Que vas a aprender

- Usar `pd.read_csv()`.
- Revisar las primeras filas con `head()`.
- Entender por que un DataFrame es la base del analisis.

---

## 1. Cargar un CSV

```python
import pandas as pd

df = pd.read_csv("data/pandas/jugadores_futbol.csv")
```

### Por que importa

- Sin DataFrame no hay analisis.
- Cargar bien el archivo evita errores posteriores.

---

## 2. Revisar rapidamente

```python
print(df.head())
print(df.shape)
```

### Que te dice

- `head()`: como se ve la tabla.
- `shape`: cuantas filas y columnas hay.

---

## 3. Mini practica

Carga el CSV, imprime `head()` y `shape`, y verifica que las columnas esperadas existan.

---

## Errores comunes

- Escribir mal la ruta del archivo.
- Olvidar importar pandas.
- No revisar si el CSV tiene separador o encoding distinto.
