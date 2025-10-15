from estanterias import Estanterias
class Almacen():
    def __init__(self, nombre):
        self.nombre = nombre
        self.estanterias = []

    def agregar_estanterias(self, estantaria):
        self.estanterias.append(estantaria)

    def mostra_estanterias_almacen(self):
        print(f"Almacen: {self.nombre}")
        for a in self.estanterias:
            a.mostrar_productos()