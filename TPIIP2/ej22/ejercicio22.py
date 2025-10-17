'''22. Una flota agrupa a múltiples vehículos. Los vehículos pueden ser camiones o furgonetas. Cada
vehículo en la flota transporta un envío. Un envío puede estar compuesto por varios paquetes
(uno o más productos) cuya vida depende totalmente de dicho envío. Si un paquete no se
entrega, el paquete se “destruye” pero no así los productos.'''

        
class Vehiculo:
    def __init__(self, patente, modelo, marca, conductor):
        self.patente = patente
        self.modelo = modelo
        self.marca = marca  
        self.conductor = conductor 
class Camiones(Vehiculo):   
    def __init__(self, patente, modelo, marca, conductor):
        super().__init__(patente, modelo, marca, conductor) 
class Furgoneta(Vehiculo):
    def __init__(self, patente, modelo, marca, conductor):
        super().__init__(patente, modelo, marca, conductor)               


class Flota:
    def __init__(self):
