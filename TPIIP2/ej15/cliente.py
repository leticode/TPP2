from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, dni, telefono, email, direccion, idCliente):
        super().__init__(nombre, dni, telefono, email, direccion)
        self.idCliente = idCliente
    def  mostrarInfo(self):
        print (super().mostrarInfo() + f"Id cliente: {self.idCliente}")  