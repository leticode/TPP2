
class Examen():
    def __init__(self, tema: str, numero: int ):
        self.tema = tema
        self.numero = numero
        self.preguntas = []

    def agregarpreguntas(self, interrogante, puntaje):
        pregunta = Preguntas(interrogante, puntaje)
        if pregunta not in self.preguntas:
            self.preguntas.append(pregunta)

    def mostrarinfo(self): 
        print(f"examen {self.numero}, tema: {self.tema}")
        for pregunta in self.preguntas:
            return(f"  {pregunta.mostrarinfo()}")

class Preguntas():
    def __init__(self, interrogante: str, puntaje: int):
        self.interrogante = interrogante 
        self.puntaje = puntaje

    def mostrarinfo(self):
        return f"pregunta: {self.interrogante}, puntaje: {self.puntaje}"

class Materia():
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.examenes = []

    def agregarexamenes(self, examen):
        if examen not in self.examenes:
            self.examenes.append(examen)
            examen.materia = self

    def mostrarinfo(self):
        print(f"Materia:{self.nombre}")
        for examen in self.examenes:
            examen.mostrarinfo()

examen1 = Examen("cultura general", 1)
examen2 = Examen("colores", 3)

materia1 = Materia("Biologia")
materia2 = Materia("geografia")

materia1.agregarexamenes(examen1)
materia1.agregarexamenes(examen2)

examen1.agregarpreguntas("donde nacio messi?", 5)
examen1.agregarpreguntas("de que color es el cielo?", 10)

materia1.mostrarinfo()