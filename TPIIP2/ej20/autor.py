class Autor:
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    def __str__(self):
        info_autor = f"Nombre: {self.nombre} {self.apellido} - Nacionalidad: {self.nacionalidad}"
        return info_autor