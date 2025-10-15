class Pasajero:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
    
    def __str__(self):
        return f"Nombre del pasajero: {self.nombre}, DNI: {self.dni}"