from empleado import Empleado
class Cajero(Empleado):
    def __init__(self, nombre: str, apellido: str, cargo: str, turno: str, sucursal: str):
        super().__init__(nombre, apellido, cargo)
        self.turno = turno
        self.sucursal = sucursal