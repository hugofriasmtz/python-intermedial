# NumPy: arreglos y operaciones vectorizadas

![NumPy logo](https://numpy.org/images/logo.svg)

> Convierte listas en arreglos eficientes y aprende a trabajar con operaciones numéricas de forma clara y rápida.

---

## Tabla de contenido

1. [Que es NumPy](#que-es-numpy)
2. [Que puedes lograr con NumPy](#que-puedes-lograr-con-numpy)
3. [Ruta de aprendizaje de este modulo](#ruta-de-aprendizaje-de-este-modulo)
4. [Como ejecutar los retos](#como-ejecutar-los-retos)
5. [Convencion de nombres](#convencion-de-nombres)
6. [Datos del modulo](#datos-del-modulo)
7. [Recursos oficiales](#recursos-oficiales)
8. [Estado del modulo](#estado-del-modulo)

---

## Que es NumPy

NumPy es la libreria base para trabajar con datos numericos en Python.

Con NumPy puedes:

- Crear arreglos eficientes.
- Trabajar con matrices y dimensiones.
- Hacer operaciones vectorizadas sin bucles.
- Filtrar valores con condiciones booleanas.
- Preparar la base para Pandas, Matplotlib y analisis numerico.

En palabras simples: NumPy te ayuda a pensar en datos numericos como arreglos, no como listas sueltas.

---

## Que puedes lograr con NumPy

### Analisis numerico

- Revisar forma, tipo y dimensiones de un arreglo.
- Seleccionar posiciones concretas con slicing.
- Calcular resumenes rapidos.

### Operaciones sobre datos

- Sumar, restar o multiplicar todos los elementos a la vez.
- Aplicar condiciones para filtrar datos.
- Combinar mascaras booleanas.

### Base para otros modulos

- Pandas usa arreglos numericos bajo el capot.
- Matplotlib puede graficar los resultados que prepares aqui.

---

## Ruta de aprendizaje de este modulo

Este modulo esta dividido en dos bloques:

1. `retos/bloque_1` - fundamentos de arreglos y seleccion.
2. `retos/bloque_2` - operaciones vectorizadas y condiciones.

### Bloque 1: fundamentos

- Reto 1: crear arreglos basicos.
- Reto 2: leer forma, dimensiones y tipo.
- Reto 3: indexado y slices.
- Reto 4: operaciones vectorizadas.
- Reto 5: filtrado booleano.
- Reto 6: resumen simple de datos.

### Bloque 2: intermedio

- Reto 1: operaciones vectorizadas.
- Reto 2: filtrado booleano.
- Reto 3: resumen simple.
- Reto 4: logical_and.
- Reto 5: logical_or.
- Reto 6: logical_not.

---

## Como ejecutar los retos

Desde la raiz del modulo:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r numpy/requirements.txt
python numpy/retos/bloque_1/reto_1_arreglos_basicos.py
```

Puedes cambiar el ultimo archivo por cualquiera de los demas retos.

---

## Convencion de nombres

Los ejercicios usan este formato:

- `reto_1_...py`
- `reto_2_...py`
- `reto_3_...py`

La idea es resolverlos en orden porque cada uno agrega un concepto nuevo.

---

## Datos del modulo

Los archivos de apoyo estan en:

- `data/numpy/`

Archivos disponibles:

- `numeros_base.csv` - arreglos basicos.
- `secuencia_6.csv` - valores para indexado.
- `matriz_2x3.csv` - matriz simple para forma y dimensiones.
- `precios.csv` - precios para operaciones vectorizadas.
- `temperaturas.csv` - datos para filtrado booleano.
- `puntajes.csv` - datos para resumen simple.
- `edades.csv` - datos para filtros con condiciones compuestas.
- `puntajes_extremos.csv` - datos para logical_or.

---

## Recursos oficiales

- [Sitio oficial de NumPy](https://numpy.org/)
- [Documentacion de NumPy](https://numpy.org/doc/)
- [Guia rapida](https://numpy.org/doc/stable/user/quickstart.html)
- [Referencia de API](https://numpy.org/doc/stable/reference/)

---

## Estado del modulo

- Los README de cada bloque explican que vas a aprender en cada parte.
- Los archivos `.py` contienen solo lo necesario para resolver cada ejercicio.
- Los datos de apoyo viven en `data/numpy/` para reutilizarlos en los retos.# Guía de NumPy

NumPy es la base del trabajo numerico en Python. Sirve para crear arreglos eficientes, hacer operaciones vectorizadas y construir una base solida antes de pasar a Pandas o visualizacion.

La ruta de aprendizaje de esta carpeta va de lo simple a lo util: primero crear arreglos, despues indexarlos y finalmente aplicar operaciones y filtros basicos. Cada archivo busca que recuerdes el por que de la sintaxis, no solo el resultado.

## Qué Vas a Practicar

1. Crear arreglos con `array()` y entender la diferencia con una lista.
2. Revisar forma, tipo de dato y dimensiones.
3. Indexar, cortar y seleccionar elementos.
4. Aplicar operaciones vectorizadas sin usar bucles.
5. Usar mascaras booleanas para filtrar datos.

## Preparar el Entorno

Si quieres trabajar solo con NumPy, crea un entorno virtual y luego instala la dependencia minima:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Verifica la instalacion asi:

```bash
python -c "import numpy as np; print(np.__version__)"
```

## Cómo Están Hechos los Retos

Los ejercicios de `retos/` estan escritos para que puedas leerlos como ejemplos guiados. Cada uno tiene comentarios que explican que significa cada paso y por que conviene escribirlo de esa forma.

## Operadores Logicos en NumPy

Cuando trabajas con arreglos, usa estas funciones para combinar condiciones elemento por elemento:

1. `np.logical_and(cond1, cond2)` equivale a `and`.
2. `np.logical_or(cond1, cond2)` equivale a `or`.
3. `np.logical_not(cond)` equivale a `not`.

Ejemplo rapido:

```python
import numpy as np

values = np.array([5, 12, 18, 25, 30])

between_10_and_25 = np.logical_and(values >= 10, values <= 25)
less_than_10_or_greater_25 = np.logical_or(values < 10, values > 25)
not_between_10_and_25 = np.logical_not(between_10_and_25)

print(values[between_10_and_25])
print(values[less_than_10_or_greater_25])
print(values[not_between_10_and_25])
```

## Qué Sigue Después

Cuando domines esta carpeta, el siguiente paso natural es combinar NumPy con Pandas para limpiar datos y con Matplotlib para graficarlos.
