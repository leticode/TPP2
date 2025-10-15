
class Preguntas():
    def __init__(self, interrogante: str, puntaje: int):
        self.interrogante = interrogante 
        self.puntaje = puntaje

    def mostrarinfo(self):
        return f"pregunta: {self.interrogante}, puntaje: {self.puntaje}"
