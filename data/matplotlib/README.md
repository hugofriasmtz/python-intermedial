# Datos para Matplotlib

Esta carpeta contiene los datasets utilizados en los retos de matplotlib.

## Archivos disponibles

### `ventas_cafeteria.csv`

- **Descripción**: Datos de ventas mensuales de una cafetería por tipo de producto
- **Periodo**: Enero a Diciembre (12 meses)
- **Categorías**: Café, Té, Postres, Sándwiches, Helados
- **Uso**: Gráficos de líneas, barras, comparaciones y tendencias

## Cómo usar los datos

```python
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parents[3] / "data" / "matplotlib" / "ventas_cafeteria.csv"
df = pd.read_csv(csv_path)
```

Estos datos permiten practicar:

- Gráficos de líneas simples y múltiples
- Gráficos de barras y barras agrupadas
- Subplots para comparaciones
- Escalas y anotaciones
- Visualización de tendencias
