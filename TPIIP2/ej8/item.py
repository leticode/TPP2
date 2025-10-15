class Item():

    def __init__(self, producto: str, cantidad: int):
        if not producto:
            raise ValueError("tiene que poner algo")
        elif cantidad < 0:
            raise ValueError("la cantidad no puede ser negativa")

        self.producto = producto
        self.cantidad = cantidad

    def mostrarinfo(self):
        return f"producto:{self.producto}, cantidad:{self.cantidad}" 