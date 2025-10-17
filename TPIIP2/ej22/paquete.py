from producto import Producto
class Paquete:
    def __init__(self, productos):
        self.productos = productos

    def entregar(self):
        print("Paquete entregado.")

    def destruir(self):
        print("Paquete destruido. Productos no destruidos:")
        for producto in self.productos:
            print(f"  - {producto}")
