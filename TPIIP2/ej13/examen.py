from preguntas import Preguntas
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