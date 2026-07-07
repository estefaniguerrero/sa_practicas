import os
from config import ARCHIVO_INVENTARIO
from calculos import calcular_iva, calcular_descuento

def registrar_producto(nombre, precio, stock, categoria):
    if not nombre or precio <= 0 or stock < 0:
        print("Error: Datos del producto inválidos.")
        return False
        
    precio_con_iva = precio + calcular_iva(precio)
    descuento = calcular_descuento(precio_con_iva, categoria)
    precio_final = precio_con_iva - descuento
    
    linea = f"{nombre},{precio},{stock},{categoria},{precio_final}\n"
    
    with open(ARCHIVO_INVENTARIO, "a") as archivo:
        archivo.write(linea)
    print(f"Producto '{nombre}' guardado con éxito.")
    return True

def listar_productos():
    if not os.path.exists(ARCHIVO_INVENTARIO):
        print("No hay datos registrados.")
        return

    print("-" * 60)
    print(f"{'PRODUCTO':<15} | {'PRECIO':<8} | {'STOCK':<8} | {'CATEGORÍA':<12} | {'PRECIO FINAL':<10}")
    print("-" * 60)
    
    with open(ARCHIVO_INVENTARIO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            print(f"{datos[0]:<15} | ${float(datos[1]):<7.2f} | {datos[2]:<8} | {datos[3]:<12} | ${float(datos[4]):<10.2f}")
    print("-" * 60)

def generar_reporte_iva():
    if not os.path.exists(ARCHIVO_INVENTARIO):
        print("No hay productos para generar reportes.")
        return
        
    total_iva_acumulado = 0.0
    with open(ARCHIVO_INVENTARIO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            total_iva_acumulado += calcular_iva(float(datos[1]))
            
    print(f"Total de IVA acumulado en inventario: ${total_iva_acumulado:.2f}")