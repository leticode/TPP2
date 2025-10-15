class Vuelo:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.reservas = []
    
    def agregar_reservas(self, pasajero):
        if len(self.reservas) < self.capacidad:
            self.reservas.append(pasajero)
            print("Asiento reservado exitosamente :)")
        else:
            print("No hay asientos disponibles")

    def mostrar_reservar(self):
        print(f"Vuelo: {self.numero}, Capacidad: {self.capacidad}")