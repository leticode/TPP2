from persona import Persona
class Proveedor(Persona):
    def __init__(self, nombre, dni, telefono, email, direccion, marca):
        super().__init__(nombre, dni, telefono, email, direccion)
        self.marca = marca
    def mostrarInfo(self):
        print(super().mostrarInfo() + f" Marca: {self.marca}")    