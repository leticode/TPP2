from transaccion import Transaccion

class Retiro(Transaccion):
    def aplicar(self, cuenta):
        if self.monto <= cuenta.saldo:
            cuenta.saldo = cuenta.saldo - self.monto
            print(f"${self.monto} retirado correctamente de la cuenta :)")
        else:
            print("Error! Intente con un monto mas pequeño")