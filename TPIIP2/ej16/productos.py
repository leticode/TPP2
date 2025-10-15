class Producto():
    def __init__(self, nombreProduc,  precio, ):
        self.nombreProduc = nombreProduc
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombreProduc}, Precio: {self.precio}"