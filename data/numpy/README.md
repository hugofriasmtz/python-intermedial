# Datos para NumPy

Esta carpeta contiene arreglos y tablas pequenas para practicar con NumPy.

## Archivos disponibles

- `numeros_base.csv` - serie corta para crear arreglos basicos.
- `secuencia_6.csv` - secuencia numerica para indexado.
- `matriz_2x3.csv` - matriz de ejemplo para forma y dimensiones.
- `precios.csv` - precios base para operaciones vectorizadas.
- `temperaturas.csv` - datos para filtrado booleano.
- `puntajes.csv` - valores para resumen simple.
- `edades.csv` - edades para condiciones compuestas.
- `puntajes_extremos.csv` - puntajes para filtros con logical_or.

## Uso rapido

```python
from pathlib import Path
import numpy as np

data_dir = Path(__file__).resolve().parents[2] / "data" / "numpy"
values = np.loadtxt(data_dir / "numeros_base.csv", delimiter=",", skiprows=1, dtype=int)
```

Estos datos estan pensados para ejercicios cortos y progresivos.
