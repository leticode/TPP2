
class Item():

    def __init__(self, producto: str, cantidad: int):
        if not producto:
            raise ValueError("tiene que poner algo")
        elif cantidad < 0:
            raise ValueError("la cantidad no puede ser negativa")

        self.producto = producto
        self.cantidad = cantidad

    def mostrarinfo(self):
        return f"producto:{self.producto}, cantidad:{self.cantidad}" 
        

class Pedidos():
    
    def __init__(self):
        self.items = []

    def agregarproducto(self, producto, cantidad):
        
        item = Item(producto, cantidad) 
        self.items.append(item)

    def mostrarinfo(self):
        if not self.items:
            raise ValueError("el pedido esta vacio")
        print("PEDIDO")
        for item in self.items:
            print(item.mostrarinfo())


pedido1 = Pedidos()
pedido2 = Pedidos()

pedido1.agregarproducto("mayonesa", 1)
pedido1.agregarproducto("limón", 4)
pedido2.agregarproducto("lavandina", 2)

pedido1.mostrarinfo()
pedido2.mostrarinfo()