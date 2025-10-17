from lineaFactura import LineaFactura
class Factura():
    def __init__(self, numero: int, tipofactura: str):
        self.numero = numero
        self.tipofactura = tipofactura
        self.lineas = []

    def agregarlineas(self, linea : "LineaFactura"):
        self.lineas.append(linea)
    
    def mostrarinfo(self):
        print(f"numero factura:{self.numero}, tipo:{self.tipofactura}")
        for linea in self.lineas:
            linea.mostrarinfo()