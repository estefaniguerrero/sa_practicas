import os

# --- CONSTANTES ---
ARCHIVO_INVENTARIO = "datos_inv.txt"
PORCENTAJE_IVA = 0.15
DESCUENTO_TECNOLOGIA = 0.10

def calcular_iva(precio_base):
    """Calcula el IVA basado en el porcentaje establecido."""
    return precio_base * PORCENTAJE_IVA

def calcular_descuento(precio_con_iva, categoria):
    """Aplica descuento del 10% si el producto es de Tecnología."""
    if categoria == "Tecnología":
        return precio_con_iva * DESCUENTO_TECNOLOGIA
    return 0.0

def registrar_producto(nombre, precio, stock, categoria):
    """Valida, calcula el precio final y guarda el producto en el archivo."""
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
    """Lee el archivo plano y despliega los datos en un formato de tabla limpio."""
    if not os.path.exists(ARCHIVO_INVENTARIO):
        print("No hay datos registrados.")
        return

    print("-" * 60)
    print(f"{'PRODUCTO':<15} | {'PRECIO':<8} | {'STOCK':<8} | {'CATEGORÍA':<12} | {'PRECIO FINAL':<10}")
    print("-" * 60)
    
    with open(ARCHIVO_INVENTARIO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            nombre = datos[0]
            precio = float(datos[1])
            stock = int(datos[2])
            categoria = datos[3]
            precio_final = float(datos[4])
            
            print(f"{nombre:<15} | ${precio:<7.2f} | {stock:<8} | {categoria:<12} | ${precio_final:<10.2f}")
    print("-" * 60)

def generar_reporte_iva():
    """Calcula y muestra la sumatoria total del IVA acumulado."""
    if not os.path.exists(ARCHIVO_INVENTARIO):
        print("No hay productos para generar reportes.")
        return
        
    total_iva_acumulado = 0.0
    with open(ARCHIVO_INVENTARIO, "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            precio_base = float(datos[1])
            total_iva_acumulado += calcular_iva(precio_base)
            
    print(f"Total de IVA acumulado en inventario: ${total_iva_acumulado:.2f}")

if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO LIMPIO V2.0 ---")
    # Registro de pruebas
    registrar_producto("Laptop", 800.0, 5, "Tecnología")
    registrar_producto("Cuaderno", 2.50, 50, "Útiles")
    
    # Listado de productos
    listar_productos()
    
    # Reporte de IVA
    generar_reporte_iva()