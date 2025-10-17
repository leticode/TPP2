#22-Una flota agrupa a múltiples vehículos. Los vehículos pueden ser camiones o furgonetas. Cada vehículo en la flota transporta un envío. Un envío puede estar compuesto por varios paquetes (uno o más productos) cuya vida depende totalmente de dicho envío. Si un paquete no se entrega, el paquete se “destruye” pero no así los productos.

from camion import Camion
from envio import Envio
from flota import Flota
from vehiculo import Vehiculo
from paquete import Paquete
from producto import Producto
from furgoneta import Furgoneta






p1 = Producto("Laptop")
p2 = Producto("Telefono")
p3 = Producto("Monitor")
paquete1 = Paquete([p1, p2])
paquete2 = Paquete([p3])
envio1 = Envio([paquete1, paquete2])
camion = Camion(envio1)
flota = Flota()
flota.agregar(camion)
flota.mostrar()
camion.fallar_entrega()
print("\nNuevo envío:")
p4 = Producto("Tablet")
paquete3 = Paquete([p4])
envio2 = Envio([paquete3])
ligero = Furgoneta(envio2)
flota.agregar(ligero)
ligero.entregar()