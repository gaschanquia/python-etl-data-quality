import csv


def extraer_ventas(ruta_archivo):
    lista_completa = []
    
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            lista_completa.append(fila)
    return lista_completa


def convertir_entero_seguro(valor):
    try:
        return int(valor)
    except (ValueError, TypeError):
        return None
   
    
def diagnosticar_registro(venta):
    if venta["producto"] == "":
        return "producto_vacio"

    if convertir_entero_seguro(venta["precio"]) is None:
        return "precio_invalido"

    cantidad = convertir_entero_seguro(venta["cantidad"])

    if cantidad is None:
        return "cantidad_invalida"

    if cantidad <= 0:
        return "cantidad_no_positiva"

    return "OK"

def separar_por_calidad(ventas):
    validos= []
    rechazados = []
    
    for venta in ventas:
        diagnostico = diagnosticar_registro(venta)
        if diagnostico == "OK":
            validos.append(venta)
        else:
            copia_venta = venta.copy()
            copia_venta["motivo_rechazo"] = diagnostico
            rechazados.append(copia_venta)

    return validos, rechazados


def transformar_fila(venta):
    fila_transformada = venta.copy()
    
    fila_transformada["id"] = int(fila_transformada["id"])
    fila_transformada["precio"] = int(fila_transformada["precio"])
    fila_transformada["cantidad"] = int(fila_transformada["cantidad"])
    
    fila_transformada["subtotal"] = fila_transformada["precio"] * fila_transformada["cantidad"]
    
    validado = fila_transformada["estado"] != "Cancelado"    
    
    fila_transformada["validado"] = validado
    
    return fila_transformada
    
    
def transformar_ventas(ventas):
    lista_transformada = []
    for venta in ventas:
        lista_transformada.append(transformar_fila(venta))
    return lista_transformada


def cargar_procesadas(ruta_salida, ventas):
    columnas = [
        "id",
        "producto",
        "precio",
        "cantidad",
        "estado",
        "subtotal",
        "validado"
    ]

    with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()

        for venta in ventas:
            escritor.writerow(venta)
            

def cargar_rechazadas(ruta_salida, ventas):
    columnas = [
        "id",
        "producto",
        "precio",
        "cantidad",
        "estado",
        "motivo_rechazo"
    ]

    with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()

        for venta in ventas:
            escritor.writerow(venta)
    
    
            
def ejecutar_pipeline(ruta_entrada, ruta_procesadas, ruta_rechazadas):
    
    #Extraccion
    ventas_extraidas = extraer_ventas(ruta_entrada)
    
    #Validacion
    ventas_validas, ventas_rechazadas = separar_por_calidad(ventas_extraidas)
    
    #Transformación
    ventas_transformadas = transformar_ventas(ventas_validas)
    
    #Carga
    cargar_procesadas(ruta_procesadas, ventas_transformadas)
    cargar_rechazadas(ruta_rechazadas, ventas_rechazadas)
    
    print("Pipeline finalizado correctamente")
    
    
ejecutar_pipeline(
    "data/ventas_raw.csv",
    "data/ventas_procesadas.csv",
    "data/ventas_rechazadas.csv"
)