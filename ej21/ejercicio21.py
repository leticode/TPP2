##21. Una venta se compone de detalles (ítems vendidos). Cada detalle apunta a un producto
##preexistente. La venta es ejecutada por un cajero de la tienda que es un tipo de empleado. (agregacion)
from producto import Producto
from cajero import Cajero
from venta import Venta
from detalleVenta import DetalleVenta



producto1 = Producto("manzana", 1200, "proteica")
producto2 = Producto("pera", 300, "fruta")

cajero1 = Cajero("roberta", "romero", "cajera", "noche","centro")

venta1 = Venta(cajero1)
venta1.agregarDetalleVenta(DetalleVenta(producto1, 3, "efectivo")) 
venta1.agregarDetalleVenta(DetalleVenta(producto2, 2, "transferencia")) 

print(venta1)