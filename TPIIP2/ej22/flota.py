class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar(self):
        for i, v in enumerate(self.vehiculos, 1):
            print(f"{i}. {v}")

