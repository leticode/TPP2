from vehiculo import Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, pasajeros, puertas):
        super().__init__(marca, pasajeros)
        self.puertas = puertas
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"y {self.puertas} puertas") 