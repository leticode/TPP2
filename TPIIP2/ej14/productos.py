class Producto():
    def __init__(self, nombre: str, descripcion: str, precio: float):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def mostrarinfo(self):
        print(f"producto:{self.nombre}, descripcion:{self.descripcion}, precio:{self.precio}")