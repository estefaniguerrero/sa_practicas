import os
import json

# Archivo JSON para persistencia de datos (Actividad 3)
A_JSON = "datos_inv.json"

def p_pro(codigo_barras, op, x="", p=0.0, c=0, t=""):
    """
    Función de inventario modificada para subsanar todas las actividades del taller.
    """
    # Cargar datos existentes si el archivo JSON ya existe
    inventario = []
    if os.path.exists(A_JSON):
        with open(A_JSON, "r") as f:
            try:
                inventario = json.load(f)
            except json.JSONDecodeError:
                inventario = []

    if op == 1:
        # ACTIVIDAD 4: Validación de campo obligatorio codigo_barras al inicio
        if codigo_barras == "" or x == "" or p <= 0 or c < 0:
            print("Error: Datos inválidos o falta el código de barras obligatorio.")
            return False
        
        # ACTIVIDAD 2: Categoría "Tecnología" paga el 12% de IVA en lugar del 15%
        tasa_iva = 0.12 if t == "Tecnología" else 0.15
        iva = p * tasa_iva
        total_con_iva = p + iva
        
        if t == "Tecnología":
            p_final = total_con_iva - (total_con_iva * 0.10)
        else:
            p_final = total_con_iva
            
        # ACTIVIDAD 3: Estructurar la información para guardarla en JSON
        nuevo_producto = {
            "codigo_barras": codigo_barras,
            "producto": x,
            "precio": p,
            "stock": c,
            "categoria": t,
            "precio_final": round(p_final, 2)
        }
        
        inventario.append(nuevo_producto)
        
        # Guardar en archivo estructurado .json
        with open(A_JSON, "w") as f:
            json.dump(inventario, f, indent=4)
        print(f"Producto '{x}' guardado con éxito en formato JSON.")
        return True

    elif op == 2:
        # LECTURA Y DESPLIEGUE DESDE JSON (Actividad 3)
        if not inventario:
            print("No hay datos registrados en el inventario.")
            return
            
        print("--------------------------------------------------------------------------------")
        print("COD. BARRAS | PROD | PRECIO BASE | STOCK | CAT | PRECIO FINAL")
        print("--------------------------------------------------------------------------------")
        for prod in inventario:
            print(f"{prod['codigo_barras']} | {prod['producto']} | ${prod['precio']} | {prod['stock']} u. | {prod['categoria']} | ${prod['precio_final']}")
            
            # ACTIVIDAD 1: Imprimir mensaje de alerta en consola si el stock es menor a 5 unidades
            if int(prod['stock']) < 5:
                print(f"   ⚠️ [ALERTA CALIDAD] ¡Stock crítico! Solo quedan {prod['stock']} unidades de '{prod['producto']}'.")
        print("--------------------------------------------------------------------------------")

    elif op == 3:
        # SIMULACIÓN DE REPORTES RECALCULANDO EL IVA ACUMULADO
        if not inventario:
            print("No hay datos para generar reportes.")
            return
            
        sumatoria = 0
        for prod in inventario:
            precio_base = float(prod['precio'])
            # ACTIVIDAD 2: Aplicar el 12% a Tecnología y 15% general en el reporte
            tasa_iva_rep = 0.12 if prod['categoria'] == "Tecnología" else 0.15
            iva_repetido = precio_base * tasa_iva_rep
            sumatoria += iva_repetido
            
        print(f"Total de IVA acumulado en inventario: ${round(sumatoria, 2)}")

# Simulación completa del programa ejecutando todas las pruebas del documento
if __name__ == "__main__":
    print("--- SISTEMA DE INVENTARIO ACTUALIZADO V2.0 (TODO EN UNO) ---")
    
    # Limpiar archivo previo si existe para una simulación limpia
    if os.path.exists(A_JSON):
        os.remove(A_JSON)
        
    # 1. Registrar productos de prueba (Estefani)
    p_pro("78610012", 1, "Laptop", 800.0, 3, "Tecnología")  # Stock < 5 (Alerta) e IVA 12%
    p_pro("78610055", 1, "Cuaderno", 2.50, 50, "Útiles")     # Stock Normal e IVA 15%
    
    # =========================================================================
    # MODIFICACIÓN DE COMPAÑERO: PRUEBAS DE INTEGRACIÓN ADICIONALES
    # =========================================================================
    print("\n--- EJECUTANDO REGISTROS ADICIONALES (APORTE COMPAÑERO) ---")
    p_pro("78620022", 1, "Smartphone", 350.0, 2, "Tecnología") # Validando Alerta e IVA 12%
    p_pro("78630033", 1, "Impresora", 150.0, 10, "Tecnología") # Validando Stock Ok e IVA 12%
    p_pro("78640044", 1, "Escritorio", 85.0, 4, "Muebles")     # Validando Alerta e IVA 15%
    # =========================================================================
    
    # 2. Listar productos (Para verificar formato visual y alertas de stock)
    print("\n--- DESPLIEGUE GENERAL DEL INVENTARIO ---")
    p_pro("", 2)
    
    # 3. Ver reporte acumulado de IVA
    print("\n--- REPORTE IMPOSITIVO FINAL ---")
    p_pro("", 3)