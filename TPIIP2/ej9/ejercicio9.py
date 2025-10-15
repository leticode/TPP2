from alumno import Alumno
from profesor import Profesor
            
alumno1 = Alumno("Leticia", 9000443)
alumno2 = Alumno("Sofia", 70009444)
profesor1 = Profesor("Patricia")
profesor1.agregarAlumnos(alumno1)
profesor1.agregarAlumnos(alumno2)
profesor1.mostrarAlumno()            
