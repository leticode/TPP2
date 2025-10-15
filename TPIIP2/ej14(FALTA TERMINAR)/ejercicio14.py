'''14. Una factura contiene líneas de factura. Cada línea hace referencia a un producto
 (con precio y descripción) que está en el inventario preexistente y una cantidad vendida.'''
from productos import Producto
from factura import Factura
from lineaFactura import LineaDeFactura

producto1 = Producto(500, "Limpia mucho" )
producto2 = Producto( 700 ,"Dientes radiantes")
linea1 = LineaDeFactura("Detergente", 6)
linea2= LineaDeFactura("Pasta dental", 5)
             
