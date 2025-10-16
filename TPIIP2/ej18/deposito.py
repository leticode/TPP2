from transaccion import Transaccion

class Deposito(Transaccion):
    def aplicar(self, cuenta):
        self.cuenta =  cuenta
        cuenta.saldo = cuenta.saldo + self.monto
        print(f"Se han depositado ${self.monto} de manera correcta :)")