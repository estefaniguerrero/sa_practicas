from config import PORCENTAJE_IVA, DESCUENTO_TECNOLOGIA

def calcular_iva(precio_base):
    return precio_base * PORCENTAJE_IVA

def calcular_descuento(precio_con_iva, categoria):
    if categoria == "Tecnología":
        return precio_con_iva * DESCUENTO_TECNOLOGIA
    return 0.0