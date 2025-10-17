class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
    
    def __str__(self):
        return f"{self.nombre} - Lugar: {self.ciudad}"