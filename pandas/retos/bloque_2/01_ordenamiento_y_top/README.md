# 01 - Ordenamiento y Top

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Practicaremos **ordenar datos y extraer los mejores (o peores)** usando un DataFrame de estudiantes:

- **¿Cómo ordeno a los estudiantes por su promedio?** → `sort_values(ascending=False)`
- **¿Cómo obtengo a los primeros N estudiantes ordenados?** → `sort_values()` + `head()`
- **¿Cómo ordeno por ciudad y semestre a la vez?** → `sort_values(['col1', 'col2'])`
- **¿Cómo descarto los últimos N registros rápidamente?** → `tail()`

> [!IMPORTANT]
> `sort_values()` devuelve una copia; el DataFrame original no cambia a menos que uses `inplace=True`.

---

## ¿Qué vas a aprender?

- Por qué `sort_values()` es más eficiente que ordenar con bucles.
- Cuándo usar `head()` vs `tail()` vs `nlargest()` / `nsmallest()`.
- Cómo preservar o resetear el índice tras ordenar.
- Cuándo ordenar por múltiples criterios es esencial.

**Documentación:** [sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html), [head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html) y [nlargest](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nlargest.html)

---

## 1. Ordenamiento simple

Ordenar datos es el primer paso para responder muchas preguntas: "¿quién tiene el promedio más alto?", "¿qué estudiante va más avanzado?".

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "carrera": ["Ingeniería de Sistemas", "Economía", "Psicología", "Arquitectura", "Medicina", "Derecho"],
    "promedio": [4.8, 4.1, 4.5, 3.9, 4.9, 4.0],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "semestre": [8, 6, 5, 7, 9, 4]
})

# Ordenar de menor a mayor por promedio (default)
print(df.sort_values("promedio"))
# Output:
#   nombre                 carrera  promedio            ciudad  semestre
# 3  Erwin             Arquitectura       3.9           Medellín         7
# 5  Catalina                Derecho       4.0            Caracas         4
# 1  Karen                Economía       4.1  Ciudad de México         6
# 2  Marcos              Psicología       4.5           Santiago         5
# 0  Hugo  Ingeniería de Sistemas       4.8            Bogotá         8
# 4  Felipe                Medicina       4.9             La Paz         9

# Ordenar de mayor a menor
print(df.sort_values("promedio", ascending=False))
# Output: Felipe primero, luego Hugo y Marcos
```

### ¿Cuándo usarlo?

- Ranking de promedios académicos.
- Estudiantes por semestre o ciudad.
- Cualquier pregunta tipo "top" o "bottom".

---

## 2. Top N y Bottom N

Muchas veces solo te importan los extremos. En lugar de ordenar y luego tomar filas, usa `head()`, `tail()`, `nlargest()` o `nsmallest()`.

```python
# Las 3 personas con mayor promedio
print(df.nlargest(3, "promedio"))
# Output:
#    nombre                 carrera  promedio    ciudad  semestre
# 4   Felipe                Medicina       4.9  Medellín         9
# 0   Hugo  Ingeniería de Sistemas       4.8   Bogotá         8
# 2  Marcos               Psicología       4.5  Santiago         5

# Las 2 personas con menor promedio
print(df.nsmallest(2, "promedio"))
# Output:
#   nombre      carrera  promedio    ciudad  semestre
# 3  Erwin  Arquitectura       3.9  Medellín         7
# 5  Catalina      Derecho       4.0  Caracas         4
```

### Diferencia entre `head()` / `tail()` y `nlargest()` / `nsmallest()`

- `head(n)`: devuelve las primeras N filas tal como están (sin ordenar).
- `nlargest(n, col)`: devuelve las N mayores por esa columna (más eficiente que sort + head).

---

## 3. Ordenamiento múltiple

A veces necesitas ordenar por varias columnas a la vez. Por ejemplo: "ordena por ciudad, y dentro de cada ciudad por salario descendente".

```python
# Ordena por ciudad (A→Z) y luego por promedio (mayor a menor)
print(df.sort_values(["ciudad", "promedio"], ascending=[True, False]))
# Output:
#   nombre                 carrera  promedio              ciudad  semestre
# 0  Hugo  Ingeniería de Sistemas       4.8             Bogotá         8
# 1  Karen                Economía       4.1   Ciudad de México         6
# 3  Erwin             Arquitectura       3.9           Medellín         7
# 4  Felipe                Medicina       4.9             La Paz         9
# 2 Marcos               Psicología       4.5            Santiago         5
# 5  Catalina                 Derecho       4.0            Caracas         4
```

### Regla importante

- `ascending=[True, False]` aplica a cada columna en orden.
- Primera columna: True (A→Z).
- Segunda columna: False (mayor→menor).

---

## 4. ¿Preservar o resetear índice?

Cuando ordenas, los índices se mantienen. A veces es útil limpiar esto.

```python
# Con reset_index, el índice se renumera 0,1,2...
print(df.sort_values("promedio", ascending=False).reset_index(drop=True))
# Output: Felipe (índice 0), Hugo (1), Marcos (2), etc.
```

---

## Errores comunes

- Confundir `head(n)` (primeras filas sin ordenar) con `nlargest(n)` (mayores de verdad).
- Olvidar `ascending=False` y obtener el orden opuesto al esperado.
- No usar `reset_index(drop=True)` cuando necesitas índices limpios para merges posteriores.
