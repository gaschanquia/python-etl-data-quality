# Python ETL & Data Quality Pipeline

Mini proyecto de Data Engineering desarrollado en Python para practicar la construcción de un pipeline ETL con controles de calidad de datos.

## Flujo del pipeline

CSV RAW → Extract → Validate → Transform → Load

El proceso:

- Extrae registros desde un archivo CSV.
- Valida la calidad de los datos.
- Separa registros válidos y rechazados.
- Registra el motivo de rechazo de los datos inválidos.
- Convierte tipos de datos.
- Calcula el subtotal de cada venta.
- Aplica una regla de negocio para identificar ventas no canceladas.
- Genera archivos CSV separados para datos procesados y rechazados.

## Tecnologías

- Python
- CSV
- Git
- GitHub

## Estructura

- `data/ventas_raw.csv`: datos de entrada.
- `data/ventas_procesadas.csv`: registros válidos y transformados.
- `data/ventas_rechazadas.csv`: registros rechazados con trazabilidad del error.
- `src/etl.py`: lógica del pipeline.

## Objetivo

Proyecto práctico orientado al aprendizaje de conceptos fundamentales de Data Engineering: ETL, validación, transformación, calidad de datos y trazabilidad.

## Resultados

El pipeline procesó 13 registros:

- 8 registros válidos y transformados.
- 5 registros rechazados con motivo documentado.
- 4 reglas de calidad implementadas.
- 7 ventas no canceladas y 1 cancelada.

Los archivos generados se encuentran disponibles en `data/ventas_procesadas.csv` y `data/ventas_rechazadas.csv`, permitiendo verificar los resultados y el motivo de rechazo de cada registro inválido.
