# 06 - Filtros Basicos

![pandas secondary logo](https://pandas.pydata.org/static/img/pandas_secondary.svg)

> [!NOTE]
> "La práctica consistente transforma lo difícil en dominio. Cada línea de código es un paso adelante."

---

## ¿Qué haremos?

Responderemos preguntas usando filtros:

1. **¿Cómo encuentro todas las filas que cumplen UNA condición?** → Filtro simple
2. **¿Cómo encuentro filas que cumplen VARIAS condiciones a la vez?** → Filtro combinado con `&` y `|`
3. **¿Cómo muestro mis resultados ordenados por prioridad?** → Combinar filtro + sort

> [!WARNING]
> Los operadores `and` y `or` de Python NO funcionan con DataFrames. Usa `&` e `|` en su lugar.

---

## Que vas a aprender

- Por qué `&` (AND) requiere TODAS las condiciones verdaderas y `|` (OR) requiere al menos UNA.
- Cuándo los paréntesis alrededor de cada condición son obligatorios (precedencia de operadores).
- Cómo depurar filtros complejos dividiéndolos en variables intermedias.

---

## 1. Filtro simple

```python
import pandas as pd

df = pd.DataFrame({
    "nombre": ["Hugo", "Karen", "Marcos", "Erwin", "Felipe", "Catalina"],
    "puesto": ["Programador", "Administradora", "Backend", "Frontend", "Constructor", "Ama de casa"],
    "salario": [4500, 3200, 3800, 3500, 2800, 3100],
    "ciudad": ["Bogotá", "Ciudad de México", "Santiago", "Medellín", "La Paz", "Caracas"],
    "años_experiencia": [8, 5, 3, 6, 4, 7]
})

# Filtro simple: empleados con salario mayor a 3500
print(df[df["salario"] > 3500])
# Output:
#    nombre         puesto          salario      ciudad       años_experiencia
# 0   Hugo           Programador     4500         Bogotá        8
# 2   Marcos         Backend         3800         Santiago      3
```

### Cuándo usarlo

- Cuando quieres solo filas que cumplen una condición.
- Para responder preguntas como "¿quién gana más de...?"

---

## 2. Filtro combinado

```python
# Filtro combinado: empleados de Bogotá con experiencia > 5 años
print(df[(df["ciudad"] == "Bogotá") & (df["años_experiencia"] > 5)])
# Output:
#   nombre     puesto          salario   ciudad     años_experiencia
# 0   Hugo      Programador     4500      Bogotá      8
```

> [!TIP]
> Para depurar filtros complejos, divide la máscara en variables intermedias y comprueba el tamaño con `mask.sum()` o `df[mask].shape`.

### Regla importante

- Cada condición va entre paréntesis.
- `&` significa Y (ambas condiciones deben ser verdaderas).
- `|` significa O (al menos una condición debe ser verdadera).

**Documentación:** [Indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)

---

## 3. Mini practica

Filtra jugadores titulares con valor alto y ordénalos por `valor_millones`.
