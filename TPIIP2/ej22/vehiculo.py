from envio import Envio
class Vehiculo:
    def __init__(self, envio: Envio):
        self.envio = envio
    def entregar(self):
        self.envio.entregar()
    def fallar_entrega(self):
        self.envio.fallar()