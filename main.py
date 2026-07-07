from persistencia import registrar_producto, listar_productos, generar_reporte_iva

if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO MODULAR v3.0 ---")
    
    # Ejecución limpia
    registrar_producto("Laptop", 800.0, 5, "Tecnología")
    registrar_producto("Cuaderno", 2.50, 50, "Útiles")
    
    listar_productos()
    generar_reporte_iva()