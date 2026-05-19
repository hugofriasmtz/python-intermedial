# 02 - Filtros Combinados

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **crear filtros más complejos** respondiendo preguntas del mundo académico:

- **¿Cómo encuentro estudiantes en dos ciudades específicas?** → `isin()`
- **¿Cómo filtro estudiantes cuyo nombre contenga cierta letra?** → `.str.contains()`
- **¿Cómo combino filtros con lógica "Y" y "O"?** → `&` e `|` con paréntesis
- **¿Cómo niego un filtro (lo opuesto)?** → `~mask`

> [!WARNING]
> Los operadores `and`, `or`, `not` de Python **no funcionan** con DataFrames. Usa `&`, `|`, `~` en su lugar.

---

## Que vas a aprender

- Por qué `isin()` es más legible que múltiples condiciones OR.
- Cuándo usar `.str.contains()` para filtros de texto.
- Cómo combinar filtros sin caer en errores de precedencia.
- La negación (`~`) para obtener lo opuesto a un filtro.

---

## 1. Filtro con isin()

En lugar de escribir `(df['ciudad'] == 'Bogotá') | (df['ciudad'] == 'Santiago')`, usa `isin()`.

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "carrera": ["Ingeniería de Sistemas", "Economía", "Psicología", "Arquitectura", "Medicina", "Derecho"],
    "promedio": [4.8, 4.1, 4.5, 3.9, 4.9, 4.0],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "semestre": [8, 6, 5, 7, 9, 4]
})

# Estudiantes en Bogotá o Santiago
print(df[df["ciudad"].isin(["Bogotá", "Santiago"])])
# Output:
#   nombre                carrera  promedio     ciudad  semestre
# 0   Hugo  Ingeniería de Sistemas       4.8     Bogotá         8
# 2 Marcos              Psicología       4.5    Santiago         5
```

### Cuándo usarlo

- Cuando necesitas verificar si un valor está en una lista.
- Mucho más legible que múltiples OR.

---

## 2. Filtro de texto con .str.contains()

Para buscar patrones o substrings en columnas de texto.

```python
# Estudiantes cuya carrera contiene "Ingeniería" o "Psicología"
print(df[df["carrera"].str.contains("Ingeniería|Psicología")])
# Output:
#   nombre                carrera  promedio      ciudad  semestre
# 0   Hugo  Ingeniería de Sistemas       4.8      Bogotá         8
# 2 Marcos              Psicología       4.5     Santiago         5

# Estudiantes cuyo nombre empieza con "C"
print(df[df["nombre"].str.contains("^C")])  # regex: ^C significa "empieza con C"
# Output:
#   nombre      carrera  promedio    ciudad  semestre
# 5 Catalina  Derecho       4.0   Caracas         4
```

### Opciones útiles

- `case=False`: ignore mayúsculas/minúsculas.
- `regex=True` (default): interpreta patrones regex.
- `regex=False`: búsqueda literal.

---

## 3. Combinación de filtros

Combina múltiples condiciones con `&` (Y) e `|` (O), siempre con paréntesis alrededor de cada condición.

```python
# Estudiantes de Ingeniería en Bogotá con promedio > 4.5
mask = (df["carrera"] == "Ingeniería de Sistemas") & (df["ciudad"] == "Bogotá") & (df["promedio"] > 4.5)
print(df[mask])
# Output:
#   nombre                carrera  promedio   ciudad  semestre
# 0   Hugo  Ingeniería de Sistemas       4.8   Bogotá         8

# Estudiantes en Medellín O con semestre >= 8
mask = (df["ciudad"] == "Medellín") | (df["semestre"] >= 8)
print(df[mask])
# Output:
#   nombre                carrera  promedio    ciudad  semestre
# 0   Hugo  Ingeniería de Sistemas       4.8    Bogotá         8
# 3  Erwin           Arquitectura       3.9  Medellín         7
```

### Reglas importantes

- Cada condición en paréntesis: `(condición1) & (condición2)`.
- `&` = Y (ambas verdaderas).
- `|` = O (al menos una verdadera).

---

## 4. Negación con ~

Para obtener lo opuesto a un filtro.

```python
# Estudiantes que NO están en Bogotá
mask = ~(df["ciudad"] == "Bogotá")
print(df[mask])
# Output: todos excepto Hugo

# Estudiantes que NO están en Ingeniería de Sistemas ni Medicina
mask = ~(df["carrera"].isin(["Ingeniería de Sistemas", "Medicina"]))
print(df[mask])
# Output: Karen, Marcos, Erwin, Catalina
```

---

## Errores comunes

- Olvidar paréntesis: `df[df['a'] > 5 & df['b'] < 10]` falla; debe ser `df[(df['a'] > 5) & (df['b'] < 10)]`.
- Usar `and`/`or` en lugar de `&`/`|`: genera error o comportamiento inesperado.
- Confundir `|` (O) con `&` (Y) en la lógica.
