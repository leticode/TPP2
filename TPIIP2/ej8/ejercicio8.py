from item import Item
from pedidos import Pedidos


pedido1 = Pedidos()
pedido2 = Pedidos()

pedido1.agregarproducto("mayonesa", 1)
pedido1.agregarproducto("limón", 4)
pedido2.agregarproducto("lavandina", 2)

pedido1.mostrarinfo()
pedido2.mostrarinfo()