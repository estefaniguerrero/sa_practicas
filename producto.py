from config import IVA_GENERAL, IVA_TECNOLOGIA, DESCUENTO_TECNOLOGIA


class Producto:

    def __init__(self, codigo_barras, nombre, precio, stock, categoria):
        self.codigo_barras = codigo_barras
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def calcular_precio_final(self):

        if self.categoria == "Tecnología":
            iva = self.precio * IVA_TECNOLOGIA
            total = self.precio + iva
            total -= total * DESCUENTO_TECNOLOGIA
        else:
            iva = self.precio * IVA_GENERAL
            total = self.precio + iva

        return round(total, 2)

    def to_dict(self):

        return {
            "codigo_barras": self.codigo_barras,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria,
            "precio_final": self.calcular_precio_final()
        }