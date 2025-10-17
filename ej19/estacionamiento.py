class Estacionamiento:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.plazas = []

    def agregar_plaza(self, plaza):
        if len(self.plazas) < self.capacidad:
            self.plazas.append(plaza)
            print(f"Auto agregado a la plaza {plaza.num_plaza} de {self.nombre}")
        else:
            print("No hay lugar para estacionarse :(")

    def mostrar_plazas(self):
        print(f"Estacionamiento: {self.nombre} - Capacidad: {self.capacidad}, Plazas agregadas: {len(self.plazas)}")
        if not self.plazas:
            print("No hay plazas")
        else:
            for i in self.plazas:
                print(f" - {i}")
        
    def __str__(self):
        return f"Estacionamiento: {self.nombre}, Capacidad: {self.capacidad}"