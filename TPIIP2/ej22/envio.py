from  paquete import Paquete
class Envio:
    def __init__(self, paquetes):
        self.paquetes = paquetes
        self.entregado = False

    def entregar(self):
        self.entregado = True
        for paquete in self.paquetes:
            paquete.entregar()

    def fallar(self):
        for paquete in self.paquetes:
            paquete.destruir()
