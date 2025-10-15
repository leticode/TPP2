class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
    def mostrarInfo(self):
        print(f"Alumno: {self.nombre} | Legajo: {self.legajo}")
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
            
alumno1 = Alumno("Leticia", 9000443)
alumno2 = Alumno("Sofia", 70009444)
profesor1 = Profesor("Patricia")
profesor1.agregarAlumnos(alumno1)
profesor1.agregarAlumnos(alumno2)
profesor1.mostrarAlumno()            
