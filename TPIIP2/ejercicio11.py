
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

        
class Archivo():
    def __init__(self, nombre: str, tamano: int, contenido: str):
        self.nombre = nombre
        self.tamano = tamano
        self.contenido = contenido

    def mostrarinfo(self):
        return f"nombre archivo:{self.nombre}, tamano:{self.tamano}, contenido:{self.contenido}"
    
carpeta1 = Carpeta("libros")

carpeta1.agregararchivos("piojo.txt", 40, "contenido libro")
carpeta1.agregararchivos("caperucita", 50, "libro")

carpeta1.mostrarinfo()