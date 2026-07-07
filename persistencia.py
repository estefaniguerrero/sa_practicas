"""Módulo para el manejo del almacenamiento persistente de datos."""

import os
from dataclasses import dataclass
from config import ARCHIVO_INVENTARIO
from calculos import calcular_precio_final

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int
    categoria: str


def validar_producto(producto: Producto) -> bool:
    """Verifica que el producto cumpla con los requisitos mínimos de negocio."""
    return (
        producto.nombre.strip() != ""
        and producto.precio > 0
        and producto.stock >= 0
    )


def guardar_producto(producto: Producto):
    """Escribe un nuevo registro de producto en el archivo de inventario."""
    precio_final = calcular_precio_final(producto.precio, producto.categoria)

    with open(ARCHIVO_INVENTARIO, "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{producto.nombre},"
            f"{producto.precio},"
            f"{producto.stock},"
            f"{producto.categoria},"
            f"{precio_final}\n"
        )


def leer_productos() -> list:
    """Lee el archivo físico y mapea cada línea."""
    if not os.path.exists(ARCHIVO_INVENTARIO):
        return []

    productos = []
    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
            
            nombre, precio, stock, categoria, precio_final = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "stock": int(stock),
                "categoria": categoria,
                "precio_final": float(precio_final)
            })
            
    return productos