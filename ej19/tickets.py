class Ticket:
    def __init__(self,  vehiculo, plaza):
        self.vehiculo = vehiculo
        self.plaza = plaza
    
    def mostrar_ticket(self):
        return f"Ticket - Vehiculo: {self.vehiculo} - Plaza: {self.plaza.num_plaza}"