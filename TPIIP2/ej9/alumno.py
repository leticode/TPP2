class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
    def mostrarInfo(self):
        print(f"Alumno: {self.nombre} | Legajo: {self.legajo}")