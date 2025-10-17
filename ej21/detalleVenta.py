from producto import Producto
class DetalleVenta():
    def __init__(self, producto: "Producto", cantidad: int, metodopago: str):
        self.producto = producto
        self.cantidad = cantidad
        self.metodopago = metodopago

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"producto:{self.producto.nombre}, cantdad:{self.cantidad}, metodo de pago:{self.metodopago}, subtotal:{self.subtotal()}"