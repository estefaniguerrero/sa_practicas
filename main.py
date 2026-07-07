"""Punto de entrada principal de la aplicación."""

# 1. ESTOS IMPORTS FALTABAN ARRIBA:
from persistencia import Producto, validar_producto, guardar_producto, leer_productos
from calculos import calcular_iva

def registrar_producto(producto: Producto):
    """Controlador para registrar un producto validando sus campos."""
    if not validar_producto(producto):
        print("❌ Error: Datos del producto inválidos.")
        return

    guardar_producto(producto)
    print(f"✅ Producto '{producto.nombre}' registrado con éxito.")


def listar_productos():
    """Muestra el inventario actual en pantalla de manera formateada."""
    productos = leer_productos()

    # Encabezados limpios y alineados para la tabla
    print("\n" + "=" * 65)
    print(f"{'PRODUCTO':<15} | {'PRECIO':<8} | {'STOCK':<6} | {'CATEGORÍA':<12} | {'P. FINAL':<8}")
    print("-" * 65)

    for prod in productos:
        print(
            f"{prod.nombre:<15} | "
            f"${prod.precio:<7.2f} | "
            f"{prod.stock:<6} | "
            f"{prod.categoria:<12} | "
            f"${prod.precio_final:<7.2f}"
        )
    print("=" * 65 + "\n")


def generar_reporte_iva():
    """Calcula y muestra el total consolidado de IVA recaudado."""
    productos = leer_productos()
    total_iva = sum(calcular_iva(prod.precio) for prod in productos)
    print(f"📊 IVA acumulado en inventario: ${total_iva:.2f}")


if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO MODULAR v3.0 ---")
    
    # Flujo de prueba obligatorio
    registrar_producto(Producto("Laptop", 800.0, 5, "Tecnología"))
    registrar_producto(Producto("Cuaderno", 2.5, 50, "Útiles"))

    listar_productos()
    generar_reporte_iva()