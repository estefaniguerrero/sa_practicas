"""Módulo encargado de las operaciones y reglas de negocio fiscales."""

from config import IVA, CATEGORIA_DESCUENTO, DESCUENTO_TECNOLOGIA

def calcular_iva(precio: float) -> float:
    """Calcula el valor del IVA para un precio base."""
    return precio * IVA


def calcular_precio_final(precio_base: float, categoria: str) -> float:
    """Calcula el precio final aplicando el IVA y los descuentos correspondientes."""
    precio_con_iva = precio_base + calcular_iva(precio_base)

    if categoria == CATEGORIA_DESCUENTO:
        return precio_con_iva * (1 - DESCUENTO_TECNOLOGIA)

    return precio_con_iva