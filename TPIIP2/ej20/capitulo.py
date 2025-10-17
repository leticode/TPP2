class Capitulo:
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre

    def __str__(self):
        return f"Capitulo {self.numero}: {self.nombre}"