from item import Item
        

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