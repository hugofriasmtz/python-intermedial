# Guía de NumPy

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

## Qué Sigue Después

Cuando domines esta carpeta, el siguiente paso natural es combinar NumPy con Pandas para limpiar datos y con Matplotlib para graficarlos.
