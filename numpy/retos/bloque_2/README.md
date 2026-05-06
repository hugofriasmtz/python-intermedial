# Bloque 2 - Operaciones y condiciones en NumPy

![NumPy logo](https://numpy.org/images/logo.svg)

> Lleva los arreglos un paso mas alla: transforma, filtra y resume datos de forma vectorizada.

---

## Objetivo del bloque

Al completar este bloque deberias poder:

1. Aplicar operaciones vectorizadas sobre un arreglo completo.
2. Filtrar datos con mascaras booleanas.
3. Calcular resumenes rapidos de una serie numerica.

- `np.logical_and()` - Combina dos condiciones que deben cumplirse al mismo tiempo.
  - Para qué: filtrar rangos, por ejemplo entre 18 y 30.
- `np.logical_or()` - Acepta valores que cumplen al menos una condicion.
  - Para qué: quedarte con extremos o categorias alternativas.
- `np.logical_not()` - Inverte una condicion booleana.
  - Para qué: obtener el complemento de un filtro.
- Operaciones vectorizadas - Ejecutan una operacion sobre todo el arreglo.
  - Para qué: evitar bucles y hacer el codigo mas claro.
- `mean()`, `max()`, `min()` y `np.sum()` - Resumenes basicos.
  - Para qué: entender rapido la distribucion de valores.

---

## Ruta recomendada

Completa los retos en este orden:

1. `reto_1_operaciones_vectorizadas.py` - sumar un impuesto a todos los precios.
2. `reto_2_filtrado_booleano.py` - seleccionar temperaturas altas.
3. `reto_3_resumen_simple.py` - revisar maximo, minimo y promedio.
4. `reto_4_logical_and.py` - combinar dos condiciones a la vez.
5. `reto_5_logical_or.py` - seleccionar valores extremos.
6. `reto_6_logical_not.py` - invertir una condicion.

---

## Que haras en cada reto

### Reto 1

Aplicaras un impuesto a un arreglo de precios usando una sola operacion.

### Reto 2

Crearás una mascara booleana para quedarte solo con las temperaturas altas.

### Reto 3

Calcularas maximo, minimo, promedio y cuantos valores quedan por encima del promedio.

### Reto 4

Filtraras edades que esten dentro de un rango concreto.

### Reto 5

Seleccionaras puntajes muy bajos o muy altos con una condicion compuesta.

### Reto 6

Invertiras una mascara para obtener el grupo contrario.

---

## Datos del bloque

Los ejercicios usan archivos guardados en `data/numpy/`.

- `precios.csv`
- `temperaturas.csv`
- `puntajes.csv`
- `edades.csv`
- `puntajes_extremos.csv`

---

## Errores comunes

- Usar `and`, `or` o `not` de Python con arreglos.
- Olvidar que NumPy filtra con arreglos booleanos.
- No revisar el arreglo original antes de aplicar el filtro.
- Mezclar arreglos y listas sin necesidad.

---

## Checklist de finalizacion

- [ ] Puedo aplicar una operacion vectorizada a todo el arreglo.
- [ ] Puedo crear y usar una mascara booleana.
- [ ] Puedo calcular maximo, minimo y promedio.
- [ ] Puedo usar `np.logical_and()` correctamente.
- [ ] Puedo usar `np.logical_or()` correctamente.
- [ ] Puedo usar `np.logical_not()` correctamente.
- [ ] Puedo terminar el bloque sin problemas de formato.

Fin del bloque.
