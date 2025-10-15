from cliente import Cliente
from proveedor import Proveedor
from persona import Persona

cliente1 = Cliente("Pipi", 4456789, 33400665, "pipitu@gamil.com", "Rosas al 30", 1)
provedor1 = Proveedor("Toti", 4456223, 3364523, "totilon@gmail.com", "Pacman al 400", "Don satur")

print("-----INFORMACION-----")
cliente1.mostrarInfo()
provedor1.mostrarInfo()