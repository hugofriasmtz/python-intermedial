# Python Intermedio - Prácticas y Apuntes

Este repositorio reúne mis prácticas de Python con enfoque aplicado: visualización, análisis de datos y uso de librerías comunes en entornos profesionales.

## Objetivo

- Consolidar fundamentos de Python intermedio.
- Practicar librerías del ecosistema de datos.
- Documentar aprendizajes con ejemplos claros y progresivos.

## Estructura del Repositorio

Actualmente el repositorio está organizado por librería o tema:

```text
python_intermedio/
├── numpy/
│   ├── README.md
│   ├── requirements.txt
│   └── retos/
│       ├── bloque_1/
│       └── bloque_2/
├── matplotlib/
│   ├── README.md
│   ├── requirements.txt
│   └── retos/
│       ├── bloque_1/
│       └── bloque_2/
├── pandas/
│   └── README.md
└── README.md
```

## Contenido Actual

### Matplotlib

Incluye:

- Guía base de conceptos y tipos de gráficos.
- Preparación de entorno virtual para trabajar de forma aislada.
- Retos progresivos por bloques.
- Buenas prácticas de presentación de gráficos.

### Pandas

Incluye:

- Guía inicial sobre qué es Pandas y para qué sirve.
- Conceptos básicos para comenzar a trabajar con datos tabulares.
- Base para futuros ejemplos, apuntes y ejercicios.

### NumPy

Incluye:

- Guía base para entender arreglos, tipos de datos y operaciones vectorizadas.
- Retos simples para practicar creacion, indexado y operaciones con `ndarray`.
- Ejercicios progresivos con comentarios para recordar por que se escribe cada linea.

## Cómo Empezar

1. Clona el repositorio.
2. Entra a la carpeta del módulo que quieras practicar (por ejemplo, `matplotlib/`).
3. Crea y activa un entorno virtual.
4. Instala dependencias del módulo.
5. Resuelve retos y documenta mejoras.

Comandos base:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r numpy/requirements.txt
```

Si quieres empezar con Pandas o Matplotlib, entra a sus carpetas y sigue una estructura similar.

## Convenciones del Repo

- Organización por módulos (una carpeta por librería o tema).
- Retos en orden progresivo (`bloque_1`, `bloque_2`, etc.).
- Archivos de dependencias por módulo.
- Entorno virtual fuera de control de versiones (`.venv/` en `.gitignore`).

## Próximos Módulos

- Limpieza y transformación de datos.
- Mini casos integrando varias librerías.

## Estado del Proyecto

En construcción. Este repositorio se irá actualizando de forma continua con nuevas prácticas y mejoras.
