import os
import json

# Archivo de persistencia de datos actualizado a formato estructurado JSON
A = "datos_inv.json"

def p_pro(op, x, p, c, t, codigo_barras=""):
    """
    Función de gestión de inventario optimizada con almacenamiento JSON.
    Incluye las reglas de negocio de la Fase 2.
    """
    # Intentar cargar los datos existentes si el archivo JSON ya existe
    inventario = []
    if os.path.exists(A):
        try:
            with open(A, "r", encoding="utf-8") as f:
                inventario = json.load(f)
        except json.JSONDecodeError:
            inventario = []

    if op == 1:
        # VALIDACIÓN Y REGISTRO DE PRODUCTO
        if x == "" or p <= 0 or c < 0 or codigo_barras == "":
            print("Error: Datos inválidos o falta el código de barras obligatorio.")
            return False
        
        # Financiero: Categoría "Tecnología" paga el 12% de IVA en lugar del 15% general
        if t == "Tecnología":
            iva = p * 0.12
        else:
            iva = p * 0.15
            
        total_con_iva = p + iva
        
        # Lógica de descuento para Tecnología (10%)
        if t == "Tecnología":
            p_final = total_con_iva - (total_con_iva * 0.10)
        else:
            p_final = total_con_iva
            
        # Estructura del nuevo producto en formato de diccionario para JSON
        nuevo_producto = {
            "codigo_barras": codigo_barras,
            "producto": x,
            "precio_base": p,
            "stock": c,
            "categoria": t,
            "precio_final": round(p_final, 2)
        }
        
        inventario.append(nuevo_producto)
        
        # Escritura estructurada en formato JSON
        with open(A, "w", encoding="utf-8") as f:
            json.dump(inventario, f, indent=4, ensure_ascii=False)
            
        print(f"Producto '{x}' guardado con éxito en formato JSON.")
        return True
        
    elif op == 2:
        # LECTURA Y DESPLIEGUE EN TABLA
        if not inventario:
            print("No hay datos registrados.")
            return
        
        print("---------------------------------------------------------------------------")
        print("CÓDIGO    | PROD | PRECIO | STOCK | CAT | PRECIO FINAL")
        print("---------------------------------------------------------------------------")
        for prod in inventario:
            cb = prod["codigo_barras"]
            x1 = prod["producto"]
            p1 = prod["precio_base"]
            c1 = prod["stock"]
            t1 = prod["categoria"]
            pf1 = prod["precio_final"]
            
            print(f"{cb} | {x1} | ${p1} | {c1} unidades | {t1} | ${pf1}")
            
            # Control de calidad: Alerta si el stock es menor a 5 unidades
            if c1 < 5:
                print(f"   ⚠️ ALERTA: ¡Stock crítico para '{x1}'! Apenas quedan {c1} unidades.")
                
        print("---------------------------------------------------------------------------")

    elif op == 3:
        # REPORTES: Recálculo acumulado basado en las reglas de IVA vigentes
        if not inventario:
            print("No hay datos para generar reportes de IVA.")
            return
        
        sumatoria = 0
        for prod in inventario:
            precio_base = prod["precio_base"]
            # Aplicar la misma regla de IVA asignada
            if prod["categoria"] == "Tecnología":
                iva_item = precio_base * 0.12
            else:
                iva_item = precio_base * 0.15
            sumatoria += iva_item
            
        print(f"Total de IVA acumulado en inventario: ${round(sumatoria, 2)}")

# Simulación de ejecución del programa
if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO MEJORADO V2.0 (JSON) ---")
    
    # Registrar productos de prueba con el campo obligatorio 'codigo_barras' al inicio
    p_pro(1, "Laptop", 800.0, 4, "Tecnología", "789101")  # Generará alerta por stock < 5
    p_pro(1, "Cuaderno", 2.50, 50, "Útiles", "789102")
    
    # Listar productos (Desplegará la tabla y la alerta)
    p_pro(2, "", 0, 0, "")
    
    # Ver reporte de IVA acumulado
    p_pro(3, "", 0, 0, "")