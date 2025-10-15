from archivo import Archivo
class Carpeta():
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = []

    def agregararchivos(self, nombre, tamano, contenido):
        archivo = Archivo(nombre, tamano, contenido)
        self.archivos.append(archivo)
        
    def mostrarinfo(self):
        print(f"Carpeta:", {self.nombre})
        for archivo in self.archivos:
            print(f"{archivo.mostrarinfo()}")