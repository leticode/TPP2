class Vehiculo:
    def __init__(self, titular, patente, tipo):
        self.titular = titular
        self.patente = patente
        self.tipo = tipo
    
    def __str__(self):
        return f"Titular: {self.titular}, Patente: {self.patente}, Tipo: {self.tipo}"