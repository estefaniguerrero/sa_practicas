import os
from dataclasses import dataclass

ARCHIVO_INVENTARIO = "datos_inv.txt"
IVA_ECUADOR = 0.15  # Constante semántica más descriptiva
CATEGORIA_DESCUENTO = "Tecnología"
DESCUENTO_TECNOLOGIA = 0.10

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int
    categoria: str
    precio_final: float = 0.0


def validar_producto(producto: Producto) -> bool:
    """Verifica que el producto cumpla con las condiciones mínimas comerciales."""
    return (
        producto.nombre.strip() != ""
        and producto.precio > 0
        and producto.stock >= 0
    )


def calcular_iva(precio: float) -> float:
    """Calcula el valor del IVA sobre un precio base."""
    return precio * IVA_ECUADOR


def calcular_precio_final(producto: Producto) -> float:
    """Calcula el precio final aplicando el IVA y los descuentos correspondientes."""
    precio_con_iva = producto.precio + calcular_iva(producto.precio)

    if producto.categoria == CATEGORIA_DESCUENTO:
        return precio_con_iva * (1 - DESCUENTO_TECNOLOGIA)

    return precio_con_iva


def guardar_producto(producto: Producto) -> None:
    """Persiste el registro del producto en el archivo de inventario."""
    producto.precio_final = calcular_precio_final(producto)

    # Añadido encoding='utf-8' para soportar tildes de forma segura
    with open(ARCHIVO_INVENTARIO, "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{producto.nombre},"
            f"{producto.precio},"
            f"{producto.stock},"
            f"{producto.categoria},"
            f"{producto.precio_final}\n"
        )


def registrar_producto(producto: Producto) -> None:
    """Valida y procesa el ingreso de un nuevo producto al sistema."""
    if not validar_producto(producto):
        print("Datos inválidos.")
        return

    guardar_producto(producto)
    print("Producto registrado.")


def existe_archivo() -> bool:
    """Comprueba la existencia física del archivo de persistencia."""
    return os.path.exists(ARCHIVO_INVENTARIO)


def leer_productos() -> list[Producto]:
    """Lee el archivo de inventario y reconstruye la lista de objetos Producto."""
    # Cláusula de guarda para evitar que el programa falle si el archivo no existe
    if not existe_archivo():
        return []

    productos = []
    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Validación simple para ignorar líneas vacías accidentales
            if not linea.strip():
                continue
                
            nombre, precio, stock, categoria, precio_final = linea.strip().split(",")

            productos.append(
                Producto(
                    nombre=nombre,
                    precio=float(precio),
                    stock=int(stock),
                    categoria=categoria,
                    precio_final=float(precio_final)
                )
            )    
    return productos


def mostrar_producto(producto: Producto) -> None:
    """Formatea la salida visual de un producto en consola."""
    print(
        f"{producto.nombre} | "
        f"${producto.precio:.2f} | "  # Formateado a 2 decimales para consistencia visual
        f"{producto.stock} | "
        f"{producto.categoria} | "
        f"${producto.precio_final:.2f}"
    )


def listar_productos() -> None:
    """Despliega en pantalla el catálogo completo de productos registrados."""
    productos = leer_productos()

    if not productos:
        print("No existen productos.")
        return

    print("-" * 60)
    for producto in productos:
        mostrar_producto(producto)        


def reporte_iva() -> None:
    """Calcula y muestra el valor total acumulado por concepto de IVA."""
    productos = leer_productos()
    
    total_iva = sum(calcular_iva(producto.precio) for producto in productos)
    print(f"IVA acumulado: ${total_iva:.2f}")


def main() -> None:
    # Casos de prueba iniciales obligatorios de la práctica
    registrar_producto(Producto("Laptop", 800.0, 5, "Tecnología"))
    registrar_producto(Producto("Cuaderno", 2.5, 50, "Útiles"))

    listar_productos()
    reporte_iva()


if __name__ == "__main__":
    main()