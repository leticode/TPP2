from tickets import Ticket

class Plaza:
    def __init__(self, num_plaza):
        self.num_plaza = num_plaza
        self.ocupada = False
        self.ticket = None

    def plaza_ocupar(self, vehiculo):
        if not self.ocupada:
            self.ocupada = True
            self.ticket = Ticket(vehiculo, self)
            print(f"Plaza {self.num_plaza} libre, se genero un ticket:")
            print("   ", self.ticket.mostrar_ticket())
        else:
            print(f"La plaza {self.num_plaza} esta ocupada.")
    
    def plaza_liberar(self):
        if self.ocupada:
            print("Plaza liberada!")
            self.ocupada = False
            self.ticket = None
        else:
            print("Esta plaza ya esta libre :)")
    
    def __str__(self):
        estado = "ocupada" if self.ocupada else "libre"
        return f"Plaza {self.num_plaza} esta {estado}"