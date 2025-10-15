class Vehiculo:
    def __init__(self, marca, pasajeros):
        self.marca = marca
        self.pasajeros = pasajeros
    def mostrarInfo(self):
        print(f"La marca: {self.marca} tiene {self.pasajeros} cantidad de pasajeros")
class Auto(Vehiculo):
    def __init__(self, marca, pasajeros, puertas):
        super().__init__(marca, pasajeros)
        self.puertas = puertas
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"y {self.puertas} puertas")   
class Moto(Vehiculo):
    def __init__(self, marca, pasajeros, tipo):
        super().__init__(marca, pasajeros)
        self.tipo = tipo
    def mostrarInfo(self):
        super().mostrarInfo()  
        print(f"y es de tipo {self.tipo}")  
auto1 = Auto("Toyota", 4, 4)
moto1 = Moto("Yamaha", 2, "Enduro")    
auto1.mostrarInfo()
moto1.mostrarInfo()                  