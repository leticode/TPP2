class LineaFactura():
    def __init__(self, cantidad: int):
        self.cantidad = cantidad
        self.productos = []

    def agregarproducto(self, producto: "Producto"):
        self.productos.append(producto)

    def mostrarinfo(self):
        for producto in self.productos:
            producto.mostrarinfo()
            print(f"cantidad:{self.cantidad}")