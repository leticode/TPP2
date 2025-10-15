
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