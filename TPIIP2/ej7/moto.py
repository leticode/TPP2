from vehiculo import Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, pasajeros, tipo):
        super().__init__(marca, pasajeros)
        self.tipo = tipo
    def mostrarInfo(self):
        super().mostrarInfo()  
        print(f"y es de tipo {self.tipo}")  