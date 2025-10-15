

class Universidad:
    def __init__(self, nombre):
        self.nombreUniversidad = nombre
        self.facultades = []
    def agregarFacultad(self, facultad):
        self.facultades.append(facultad)
    def mostrarFcultad(self):
        print(f"Facultades de la universidad {self.nombreUniversidad}:")
        for facul in self.facultades:
            print(f"Facultad: {facul.nombreFacultad} | Decano: {facul.decano.nombre}")