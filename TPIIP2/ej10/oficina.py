class Oficina():
    def __init__(self, nombre: str, numerooficina: int):
        self.nombre = nombre
        self.numerooficina = numerooficina

    def __str__(self):
        return f"{self.nombre} numero:{self.numerooficina})"