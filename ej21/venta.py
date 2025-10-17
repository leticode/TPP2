from cajero import Cajero
from detalleVenta import DetalleVenta

class Venta():
    def __init__(self, cajero: "Cajero"):
        self.cajero = cajero
        self.detalles = []

    def agregarDetalleVenta(self, detalleventa: "DetalleVenta"):
        self.detalles.append(detalleventa)

    def total(self):
        total = 0
        for detalle in self.detalles:
            total+= detalle.subtotal()
        return total
    
    def __str__(self):
        resultado = f"venta de:{self.cajero.nombre} {self.cajero.apellido}\n"
        resultado += f"detalles venta:\n"
        for detalle in self.detalles:
            resultado += str(detalle) 
            
        resultado += f"total:{self.total()}"
        return resultado