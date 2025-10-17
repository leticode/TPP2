class Producto():
    def __init__(self, nombre: str, precio: float, descripcion: str):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre}, precio:{self.precio}, descripcion:{self.descripcion}"