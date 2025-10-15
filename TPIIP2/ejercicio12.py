
class Decano:
    def __init__(self, nombre, dni, email):
        self.nombre = nombre
        self.dni = dni
        self.email = email

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
class Facultad:
    def __init__(self, nombre, decano):
        self.nombreFacultad = nombre
        self.decano = decano

decano1 = Decano("Julio", 44556673, "juliochucho@blbl.com")
decano2 = Decano("Soledad", 22233008, "Soledadposta@gmail.com")
facultad1 = Facultad("Ingenieria", decano1)
facultad2 = Facultad("Medicina", decano2)
universidad = Universidad("Tecnologica Nacional")

universidad.agregarFacultad(facultad1)
universidad.mostrarFcultad()
universidad.agregarFacultad(facultad2)
universidad.mostrarFcultad()
        

