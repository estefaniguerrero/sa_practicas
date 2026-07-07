"""Módulo para el manejo del almacenamiento persistente de datos."""

import os
from dataclasses import dataclass, field
from config import ARCHIVO_INVENTARIO
from calculos import calcular_precio_final

@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int
    categoria: str
    # Campo opcional para almacenar el cálculo al leer desde la persistencia
    precio_final: float = field(default=0.0)


def validar_producto(producto: Producto) -> bool:
    """Verifica que el producto cumpla con los requisitos mínimos de negocio."""
    return (
        producto.nombre.strip() != ""
        and producto.precio > 0
        and producto.stock >= 0
    )


def guardar_producto(producto: Producto):
    """Escribe un nuevo registro de producto en el archivo de inventario."""
    precio_calculado = calcular_precio_final(producto.precio, producto.categoria)

    with open(ARCHIVO_INVENTARIO, "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{producto.nombre.strip()},"
            f"{producto.precio},"
            f"{producto.stock},"
            f"{producto.categoria.strip()},"
            f"{precio_calculado}\n"
        )


def leer_productos() -> list[Producto]:
    """Lee el archivo físico y mapea cada línea a objetos de la clase Producto."""
    if not os.path.exists(ARCHIVO_INVENTARIO):
        return []

    productos: list[Producto] = []
    
    with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as archivo:
        for num_linea, linea in enumerate(archivo, start=1):
            linea_limpia = linea.strip()
            if not linea_limpia:
                continue
            
            try:
                nombre, precio, stock, categoria, precio_final = linea_limpia.split(",")
                
                # Creamos el objeto Producto directamente con su precio_final guardado
                producto = Producto(
                    nombre=nombre,
                    precio=float(precio),
                    stock=int(stock),
                    categoria=categoria,
                    precio_final=float(precio_final)
                )
                productos.append(producto)
                
            except ValueError:
                print(f"⚠️ Alerta: Línea {num_linea} corrupta u omitida en el archivo de datos.")
                continue
            
    return productos