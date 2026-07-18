import os

# ==========================
# CONFIGURACIÓN DEL SISTEMA
# ==========================

ARCHIVO_DATOS = "datos_inv.txt"
IVA = 0.15
DESCUENTO_TECNOLOGIA = 0.10


# ==========================
# FUNCIONES AUXILIARES
# ==========================

def calcular_precio_final(precio, categoria):
    """
    Calcula el precio final del producto
    aplicando IVA y descuento si corresponde.
    """
    precio_con_iva = precio * (1 + IVA)

    if categoria == "Tecnología":
        precio_con_iva *= (1 - DESCUENTO_TECNOLOGIA)

    return round(precio_con_iva, 3)


def validar_producto(nombre, precio, stock):
    """
    Verifica que los datos del producto sean válidos.
    """
    return nombre != "" and precio > 0 and stock >= 0


# ==========================
# GESTIÓN DE PRODUCTOS
# ==========================

def registrar_producto(nombre, precio, stock, categoria):
    """
    Registra un producto en el archivo.
    """

    if not validar_producto(nombre, precio, stock):
        print("Error: Datos inválidos.")
        return

    precio_final = calcular_precio_final(precio, categoria)

    with open(ARCHIVO_DATOS, "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{nombre},{precio},{stock},{categoria},{precio_final}\n"
        )

    print("Producto guardado con éxito.")


def listar_productos():
    """
    Muestra todos los productos almacenados.
    """

    if not os.path.exists(ARCHIVO_DATOS):
        print("No hay datos registrados.")
        return

    print("--------------------------------------------------")
    print("PROD | PRECIO | STOCK | CAT | PRECIO FINAL")
    print("--------------------------------------------------")

    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:
            nombre, precio, stock, categoria, precio_final = (
                linea.strip().split(",")
            )

            print(
                f"{nombre} | "
                f"${float(precio)} | "
                f"{int(stock)} unidades | "
                f"{categoria} | "
                f"${float(precio_final)}"
            )

    print("--------------------------------------------------")


def reporte_iva():
    """
    Calcula el IVA total acumulado.
    """

    if not os.path.exists(ARCHIVO_DATOS):
        print("No hay datos registrados.")
        return

    total_iva = 0

    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:
            datos = linea.strip().split(",")
            precio = float(datos[1])
            total_iva += precio * IVA

    print(f"Total de IVA acumulado en inventario: ${round(total_iva, 3)}")


# ==========================
# MENÚ PRINCIPAL
# ==========================

def gestionar_inventario(opcion, nombre="", precio=0, stock=0, categoria=""):
    """
    Controla las operaciones del sistema.
    """

    if opcion == 1:
        registrar_producto(nombre, precio, stock, categoria)

    elif opcion == 2:
        listar_productos()

    elif opcion == 3:
        reporte_iva()

    else:
        print("Opción inválida.")


# ==========================
# EJECUCIÓN DEL PROGRAMA
# ==========================

if __name__ == "__main__":

    print("--- SISTEMA DE INVENTARIO VIEJO V1.0 ---")

    registrar_producto("Laptop", 800.0, 5, "Tecnología")
    registrar_producto("Cuaderno", 2.50, 50, "Útiles")

    listar_productos()

    reporte_iva()