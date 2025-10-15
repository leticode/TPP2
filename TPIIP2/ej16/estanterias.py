class Estanterias():
    def __init__(self, numeroE):
        self.numeroE = numeroE
        self.productos = []

    def agregar_productos(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Estanteria {self.numeroE}")
        for i in self.productos:
            print(f" | {i}")