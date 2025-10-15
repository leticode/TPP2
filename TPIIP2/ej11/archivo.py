class Archivo():
    def __init__(self, nombre: str, tamano: int, contenido: str):
        self.nombre = nombre
        self.tamano = tamano
        self.contenido = contenido

    def mostrarinfo(self):
        return f"nombre archivo:{self.nombre}, tamano:{self.tamano}, contenido:{self.contenido}"