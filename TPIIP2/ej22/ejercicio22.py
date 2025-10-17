'''22. Una flota agrupa a múltiples vehículos. Los vehículos pueden ser camiones o furgonetas. Cada
vehículo en la flota transporta un envío. Un envío puede estar compuesto por varios paquetes
(uno o más productos) cuya vida depende totalmente de dicho envío. Si un paquete no se
entrega, el paquete se “destruye” pero no así los productos.'''

class Producto:
    def __init__(self, nombre, precio):
        self.nom = nombre
        self.precio = precio  
    def __str__(self, nombre, precio):
        return self.nom + self.precio
class Paquete:
    def __init__(self, productos):
        self.productos = productos

    def __str__(self):
        return f"Paquete con productos: {[p.nombre for p in self.productos]}" 
                
class Vehiculo:
    def __init__(self, patente, envio):
        self.patente = patente
        self.envio = envio
    def __str__(self):
        return    
class Camiones(Vehiculo):   
    def __init__(self, patente, modelo, marca, conductor):
        super().__init__(patente, modelo, marca, conductor) 
class Furgoneta(Vehiculo):
    def __init__(self, patente, modelo, marca, conductor):
        super().__init__(patente, modelo, marca, conductor)               


class Flota:
    def __init__(self):
