# Bloque 2 de NumPy

Este bloque sube un poco la dificultad. Aqui ya no solo vas a crear arreglos, sino que vas a usarlos para resolver tareas mas cercanas a la practica real: operaciones vectorizadas, condiciones y resúmenes simples.

## Enfoque

1. Trabajar sin bucles cuando NumPy puede resolverlo directo.
2. Entender por que las operaciones vectorizadas son mas limpias.
3. Usar condiciones para filtrar valores concretos.
4. Reconocer cuando conviene convertir una idea de Python puro a NumPy.

## Recordatorio de Operadores Logicos

En este bloque vas a usar operadores logicos aplicados a arreglos:

1. `np.logical_and(...)` para combinar dos condiciones que deben cumplirse al mismo tiempo.
2. `np.logical_or(...)` para aceptar valores que cumplen al menos una condicion.
3. `np.logical_not(...)` para invertir una condicion booleana.

Nota importante:
Con arreglos de NumPy no se recomienda usar `and`, `or` y `not` de Python directo para comparar elemento por elemento; por eso se usan las funciones logicas de NumPy.

## Orden Sugerido de Retos

1. `reto_1_operaciones_vectorizadas.py`
2. `reto_2_filtrado_booleano.py`
3. `reto_3_resumen_simple.py`
4. `reto_4_logical_and.py`
5. `reto_5_logical_or.py`
6. `reto_6_logical_not.py`

## Siguiente Paso

Resuelve los ejercicios en orden. Si no recuerdas una operacion, vuelve al bloque 1 y prueba de nuevo con ejemplos pequenos.
