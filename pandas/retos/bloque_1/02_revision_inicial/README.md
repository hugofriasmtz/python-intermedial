# 02 - Revision Inicial

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Responderemos estas preguntas sobre el DataFrame recién cargado:

- **¿Qué tamaño tiene?** → `shape` (filas, columnas)
- **¿Cuáles son los nombres de las columnas?** → `columns`
- **¿Cómo se identifica cada fila?** → `index`
- **¿Qué tipo de dato tiene cada columna?** → `dtypes`
- **¿Hay datos faltantes (nulos)?** → `isna().sum()`

> [!WARNING]
> Los tipos inferidos por `pandas` pueden no ser óptimos; define `dtype` al leer CSVs si conoces los tipos.

---

## Que vas a aprender

- Por qué revisar estructura ANTES de analizar evita errores.
- Cómo identificar columnas problemáticas (tipo incorrecto, muchos nulos).
- La diferencia entre `index` (etiqueta) y posición numérica.

---

## 1. Estructura básica

Primero, creamos nuestro DataFrame de empleados:

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "puesto": ["Programador", "Administradora", "Backend", "Frontend", "Constructor", "Ama de casa"],
    "salario": [4500, 3200, 3800, 3500, 2800, 3100],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "años_experiencia": [8, 5, 3, 6, 4, 7]
})

# Ahora revisamos la estructura
print(df.shape)
# Output: (6, 5)  → 6 filas, 5 columnas

print(df.columns)
# Output: Index(['nombre', 'puesto', 'salario', 'ciudad', 'años_experiencia'], dtype='object')

print(df.index)
# Output: RangeIndex(start=0, stop=6, step=1)

print(df.dtypes)
# Output:
# nombre                object
# puesto                object
# salario               int64
# ciudad                object
# años_experiencia      int64
```

### Para qué sirve revisar estructura

- Saber cuántas filas y columnas hay (`shape`).
- Ver los nombres de las columnas (`columns`).
- Revisar tipos de dato (`dtypes`) - esencial antes de hacer cálculos.
- Entender cómo están etiquetadas las filas (`index`).

> [!TIP]
> Si `df.shape` no coincide con lo esperado, revisa la primera fila del CSV o DataFrame: un separador incorrecto suele colocar todo en una sola columna.

---

## 2. Nulos

```python
# Contar nulos por columna
print(df.isna().sum())
# Output:
# nombre              0
# puesto              0
# salario             0
# ciudad              0
# años_experiencia    0

# Ver porcentaje de nulos
print((df.isna().mean() * 100).round(2))
# Output:
# nombre              0.0
# puesto              0.0
# salario             0.0
# ciudad              0.0
# años_experiencia    0.0
```

### Para qué sirve contar nulos

- Detectar columnas incompletas.
- Saber si hace falta limpieza.
- Identificar dónde hay datos faltantes (`NaN`) que pueden afectar cálculos.

**Documentación:** [Missing data](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html)

---

## 3. Mini practica

Carga el CSV y responde:

- Cuantas filas y columnas tiene?
- Que columnas son numericas?
- Hay nulos?

---

## Errores comunes

- No revisar tipos de datos.
- Confundir `index` con `columns`.
- No detectar valores faltantes antes de seguir.
