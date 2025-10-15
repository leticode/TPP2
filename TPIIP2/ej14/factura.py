
class Factura:
    def __init__(self, numero):
        self.nro = numero
        self.lineas = []
    def agregarLinea(self, linea):
        self.lineas.append(linea)