
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
    def agregarAlumnos(self, alumno):
        self.alumnos.append(alumno)
    def mostrarAlumno(self): 
        print(f"Profesor: {self.nombre}") 
        for alumno in self.alumnos:
            alumno.mostrarInfo()