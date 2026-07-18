import os

# Constantes
ARCHIVO_DATOS = "datos_inv.txt"
IVA = 0.15
DESCUENTO_TECNOLOGIA = 0.10


def calcular_precio_final(precio, categoria):
    """Calcula el precio final incluyendo IVA y descuento si aplica."""
    total_con_iva = precio + (precio * IVA)

    if categoria == "Tecnología":
        total_con_iva -= total_con_iva * DESCUENTO_TECNOLOGIA

    return total_con_iva


def registrar_producto(nombre, precio, stock, categoria):
    """Registra un producto en el archivo."""

    if nombre == "" or precio <= 0 or stock < 0:
        print("Error: Datos inválidos.")
        return

    precio_final = calcular_precio_final(precio, categoria)

    linea = f"{nombre},{precio},{stock},{categoria},{precio_final}\n"

    with open(ARCHIVO_DATOS, "a") as archivo:
        archivo.write(linea)

    print("Producto guardado con éxito.")


def listar_productos():
    """Muestra todos los productos registrados."""

    if not os.path.exists(ARCHIVO_DATOS):
        print("No hay datos registrados.")
        return

    print("--------------------------------------------------")
    print("PROD | PRECIO | STOCK | CAT | PRECIO FINAL")
    print("--------------------------------------------------")

    with open(ARCHIVO_DATOS, "r") as archivo:

        for linea in archivo:
            datos = linea.strip().split(",")

            nombre = datos[0]
            precio = float(datos[1])
            stock = int(datos[2])
            categoria = datos[3]
            precio_final = float(datos[4])

            print(
                f"{nombre} | ${precio} | {stock} unidades | "
                f"{categoria} | ${precio_final}"
            )

    print("--------------------------------------------------")


def reporte_iva():
    """Calcula el IVA total del inventario."""

    if not os.path.exists(ARCHIVO_DATOS):
        return

    total_iva = 0

    with open(ARCHIVO_DATOS, "r") as archivo:

        for linea in archivo:
            datos = linea.strip().split(",")
            precio = float(datos[1])
            total_iva += precio * IVA

    print(f"Total de IVA acumulado en inventario: ${total_iva}")


def gestionar_inventario(opcion, nombre="", precio=0, stock=0, categoria=""):
    """Controla las operaciones del sistema."""

    if opcion == 1:
        registrar_producto(nombre, precio, stock, categoria)

    elif opcion == 2:
        listar_productos()

    elif opcion == 3:
        reporte_iva()

    else:
        print("Opción inválida.")


if __name__ == "__main__":

    print("--- SISTEMA DE INVENTARIO VIEJO V1.0 ---")

    gestionar_inventario(
        1,
        "Laptop",
        800.0,
        5,
        "Tecnología"
    )

    gestionar_inventario(
        1,
        "Cuaderno",
        2.50,
        50,
        "Útiles"
    )

    gestionar_inventario(2)

    gestionar_inventario(3)