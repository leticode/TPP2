##14. Una factura contiene líneas de factura. Cada línea hace referencia a un producto (con precio y
##descripción) que está en el inventario preexistente y una cantidad vendida.
##(agregacion)
from productos import Producto
from lineaFactura import LineaFactura
from factura import Factura
        




producto1 = Producto("mayonesa", "aderezo", 3400)
producto2 = Producto("arroz", "pasta", 2000)

linea1 = LineaFactura(2)
linea2 = LineaFactura(3)

linea1.agregarproducto(producto1)
linea2.agregarproducto(producto2)

factura1 = Factura(15, "A")
factura2 = Factura(2, "B")

factura1.agregarlineas(linea1)
factura1.agregarlineas(linea2)

factura1.mostrarinfo()
             
