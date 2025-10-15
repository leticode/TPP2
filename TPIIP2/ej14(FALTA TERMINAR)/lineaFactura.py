class LineaDeFactura:
    def __init__(self, producto, cantidad):
        self.cant = cantidad
        self.producto = producto
    def subtotal(self):
        return self.producto.precio * self.cant