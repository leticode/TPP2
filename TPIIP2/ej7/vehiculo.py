class Vehiculo:
    def __init__(self, marca, pasajeros):
        self.marca = marca
        self.pasajeros = pasajeros
    def mostrarInfo(self):
        print(f"La marca: {self.marca} tiene {self.pasajeros} cantidad de pasajeros")