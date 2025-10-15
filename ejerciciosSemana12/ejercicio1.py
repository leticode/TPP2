class Factura:
    ultimoNumero = 0
    def __init__(self, cliente, monto):
            Factura.ultimoNumero+= 1 #Toma valor actual y le suma 1
            self.nro = Factura.ultimoNumero
            self.cliente = cliente
            self.monto = monto
    def mostrar(self):
          print(f"Factura numero {self.nro} | Cliente: {self.cliente} | Monto: ${self.monto}")

f1 = Factura("Leticia", 1000)
f2 = Factura("Lucia", 8000)
f3 = Factura("Valentina", 90000)
f1.mostrar()
f2.mostrar()
f3.mostrar()
