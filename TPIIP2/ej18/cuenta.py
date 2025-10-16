from deposito import Deposito
from retiro import Retiro

class Cuenta:
    def __init__(self, nombre, saldo_og=0):
        self.nombre = nombre
        self.saldo = saldo_og
        self.transacciones = []

    def hacer_transaccion(self, clase, monto):
        self.clase = clase
        self.monto = monto
        if self.clase == "deposito":
            transaccion = Deposito(monto)
            self.transacciones.append(transaccion)
            transaccion.aplicar(self)
        elif self.clase == "retiro":
            transaccion = Retiro(monto)
            self.transacciones.append(transaccion)
            transaccion.aplicar(self)
        else:
            print("Accion no reconocida")
        return
    
    def transacciones_mostrar(self):
        print(f"Titular: {self.nombre}, Saldo: ${self.saldo}")
        print(f"Historial: ")
        if not self.transacciones:
            print("No se han realizado movimientos")
        else:
            for i, j in enumerate(self.transacciones, 1):
                print(f"{i}. Clase: {self.clase} - Monto: ${j.monto}")