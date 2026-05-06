# Bloque 1 - Fundamentos de NumPy

![NumPy logo](https://numpy.org/images/logo.svg)

> Empieza con arreglos simples, revisa su forma y aprende a seleccionar datos paso a paso.

---

## Objetivo del bloque

Al terminar este bloque deberias poder:

1. Crear arreglos con `np.array()`.
2. Leer `shape`, `ndim` y `dtype`.
3. Seleccionar elementos con indices y slices.
4. Aplicar operaciones vectorizadas simples.
5. Filtrar datos con mascaras booleanas.
6. Obtener resumenes basicos de un arreglo.

---

## Metodos clave

- `np.array()` - Convierte listas en arreglos.
  - Para qué: trabajar con datos numericos de forma consistente.
- `shape` - Muestra filas y columnas.
  - Para qué: entender la estructura del arreglo.
- `ndim` - Indica cuantas dimensiones tiene.
  - Para qué: saber si estas trabajando con vector o matriz.
- `dtype` - Indica el tipo interno de dato.
  - Para qué: revisar si el arreglo guarda enteros, floats o textos.
- Indexado y slices - Permiten seleccionar posiciones concretas.
  - Para qué: tomar solo la parte que te interesa.
- Operaciones vectorizadas - Aplican una operación a todo el arreglo.
  - Para qué: evitar bucles innecesarios.
- Mascaras booleanas - Filtran elementos por condicion.
  - Para qué: quedarse solo con los datos relevantes.

---

## Ruta recomendada

Completa los retos en este orden:

1. `reto_1_arreglos_basicos.py` - crear tu primer arreglo.
2. `reto_2_dimension_y_forma.py` - leer forma y dimensiones.
3. `reto_3_indexado_basico.py` - seleccionar posiciones.
4. `reto_4_operaciones_vectorizadas.py` - aplicar una operacion a todo el arreglo.
5. `reto_5_filtrado_booleano.py` - filtrar con condiciones.
6. `reto_6_resumen_simple.py` - calcular maximo, minimo y promedio.

---

## Que haras en cada reto

### Reto 1

Vas a convertir una lista en un arreglo de NumPy y revisar cuántos elementos tiene.

### Reto 2

Vas a crear una matriz simple y leer su forma, dimensiones y tipo de dato.

### Reto 3

Vas a practicar indices positivos, negativos y slices.

### Reto 4

Vas a aplicar una operacion numerica a todos los elementos a la vez.

### Reto 5

Vas a usar una mascara booleana para quedarte solo con los valores que cumplen una condicion.

### Reto 6

Vas a calcular resumenes rapidos para entender mejor una serie de numeros.

---

## Estrategia de estudio

### Antes de cada reto

1. Mira el arreglo y piensa que representa.
2. Identifica si estas trabajando con vector o matriz.
3. Decide que resultado quieres obtener.

### Después de cada reto

1. Cambia un valor y revisa que pasa.
2. Imprime el arreglo original y el resultado.
3. Explica por que NumPy resuelve ese caso mejor que listas puras.

---

## Datos del bloque

Los ejercicios usan archivos pequenos guardados en `data/numpy/`.

- `numeros_base.csv`
- `secuencia_6.csv`
- `matriz_2x3.csv`
- `precios.csv`
- `temperaturas.csv`
- `puntajes.csv`

---

## Errores comunes

- Confundir indexado con slice.
- Olvidar que el indice negativo cuenta desde el final.
- Usar `and` u `or` de Python con arreglos en lugar de funciones de NumPy.
- No revisar el tipo de dato antes de operar.

---

## Checklist de finalizacion

- [ ] Entiendo para que sirve `np.array()`.
- [ ] Puedo leer `shape`, `ndim` y `dtype`.
- [ ] Puedo seleccionar elementos con indices y slices.
- [ ] Puedo aplicar una operacion vectorizada.
- [ ] Puedo filtrar con una mascara booleana.
- [ ] Puedo calcular resumenes basicos sin ayuda.
