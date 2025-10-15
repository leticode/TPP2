'''17. Un vuelo tiene una capacidad fija de asientos. 
Un pasajero reserva uno de esos asientos en su 
vuelo. '''
from pasajero import Pasajero
from vuelo import Vuelo

pasajero1 = ("Danisa", 4848488)
pasajero2 = ("Leticia", 4855667)
pasajero3 = ("Lucia", 48747484)
pasajero4 = ("Valentina", 4855962)

vuelo1 = Vuelo("BR1234", 3)

vuelo1.agregar_reservas(pasajero1)
vuelo1.agregar_reservas(pasajero2)
vuelo1.agregar_reservas(pasajero3)
vuelo1.agregar_reservas(pasajero4)

vuelo1.mostrar_reservar()