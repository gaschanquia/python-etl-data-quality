# Python ETL & Data Quality Pipeline

Mini proyecto de Data Engineering desarrollado en Python para practicar la construcción de un pipeline ETL con controles de calidad, transformación de registros y trazabilidad de errores.

## Objetivo

Implementar un flujo ETL reproducible que permita extraer datos desde un archivo CSV, validar su calidad, transformar los registros correctos y separar aquellos que incumplen las reglas establecidas.

## Flujo del pipeline

```text
CSV RAW → Extract → Validate → Transform → Load
```

El proceso realiza las siguientes etapas:

1. Extrae los registros desde un archivo CSV.
2. Valida la calidad de los datos.
3. Separa los registros válidos y rechazados.
4. Registra el motivo de rechazo de cada dato inválido.
5. Convierte los campos numéricos a tipos enteros.
6. Calcula el subtotal de cada venta.
7. Identifica las ventas no canceladas mediante una regla de negocio.
8. Genera archivos CSV separados para los datos procesados y rechazados.

## Reglas de calidad

Cada registro es evaluado mediante los siguientes controles:

- El producto no puede estar vacío.
- El precio debe contener un número entero válido.
- La cantidad debe contener un número entero válido.
- La cantidad debe ser mayor que cero.

Los registros que incumplen alguna regla se almacenan en el archivo de rechazados junto con el motivo correspondiente.

## Transformaciones

Sobre los registros válidos, el pipeline:

- Convierte `id`, `precio` y `cantidad` a valores enteros.
- Calcula el campo `subtotal` multiplicando el precio por la cantidad.
- Genera el campo booleano `validado`.
- Marca como no validadas las ventas cuyo estado sea `Cancelado`.

## Resultados

El pipeline procesó 13 registros:

- 8 registros válidos y transformados.
- 5 registros rechazados con motivo documentado.
- 4 reglas de calidad implementadas.
- 7 ventas no canceladas y 1 venta cancelada.

Los archivos generados se encuentran disponibles en:

- `data/ventas_procesadas.csv`
- `data/ventas_rechazadas.csv`

Estos archivos permiten verificar los resultados del proceso y el motivo de rechazo de cada registro inválido.

## Motivos de rechazo detectados

| Motivo | Cantidad |
|---|---:|
| Precio inválido | 2 |
| Producto vacío | 1 |
| Cantidad no positiva | 2 |
| **Total** | **5** |

## Estructura del repositorio

```text
python-etl-data-quality/
├── data/
│   ├── ventas_raw.csv
│   ├── ventas_procesadas.csv
│   └── ventas_rechazadas.csv
├── src/
│   └── etl.py
└── README.md
```

- `data/ventas_raw.csv`: datos originales de entrada.
- `data/ventas_procesadas.csv`: registros válidos y transformados.
- `data/ventas_rechazadas.csv`: registros rechazados con trazabilidad del error.
- `src/etl.py`: lógica principal del pipeline ETL.

## Ejecución

El proyecto utiliza únicamente módulos incluidos en la biblioteca estándar de Python, por lo que no requiere instalar dependencias externas.

Desde la carpeta principal del proyecto, ejecutar:

```bash
python src/etl.py
```

Al finalizar correctamente, el programa muestra:

```text
Pipeline finalizado correctamente
```

También genera o actualiza los siguientes archivos:

- `data/ventas_procesadas.csv`
- `data/ventas_rechazadas.csv`

## Tecnologías

- Python
- Módulo CSV
- Git
- GitHub

## Conceptos aplicados

- ETL
- Validación de datos
- Transformación de tipos
- Reglas de negocio
- Data Quality
- Separación de registros válidos y rechazados
- Trazabilidad de errores
- Generación de archivos procesados