'''16. Un almacén está dividido en estanterías. Cada estantería puede contener diferentes productos, 
los cuales son compartidos entre varios almacenes. '''
from almacen import Almacen
from estanterias import Estanterias
from productos import Producto

producto1 = Producto("Mayonesa",  1400)
producto2 = Producto("Leche", 1200)
producto3 = Producto("Huevo", 70)
producto4 = Producto("Atun", 900)

estanteria1 = Estanterias("A1")
estanteria2 = Estanterias("B1")

estanteria1.agregar_productos(producto1)
estanteria1.agregar_productos(producto3)
estanteria2.agregar_productos(producto2)
estanteria2.agregar_productos(producto4)

almacen1 = Almacen("Pepito")
almacen2 = Almacen("Oreo")

almacen1.agregar_estanterias(estanteria1)
almacen2.agregar_estanterias(estanteria2)

almacen1.mostra_estanterias_almacen()
almacen2.mostra_estanterias_almacen()