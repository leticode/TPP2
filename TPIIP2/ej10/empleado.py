from oficina import Oficina
class Empleado():
    def __init__(self, nombre: str, apellido: str, cargo: str, trabajaremoto = False, oficina = None):
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.trabajaremoto = trabajaremoto
        self.oficina = oficina

    def trasladar(self, nuevaoficina: "Oficina"):
        self.oficina = nuevaoficina
        self.trabajaremoto = False

    def __str__(self):
        return f"Empleado:{self.nombre}{self.apellido}, Cargo:{self.cargo}, trabaja remoto: {self.trabajaremoto}, oficina: {self.oficina}"