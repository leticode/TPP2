class Persona:
    def __init__(self, nombre, dni, telefono, email, direccion):
        self.nom = nombre
        self.dni = dni
        self.tel = telefono
        self.email = email
        self.direc = direccion
    def mostrarInfo(self):
        return f"Nombre: {self.nom} | DNI: {self.dni} | Telefono: {self.tel} | Email: {self.email} | Direccion: {self.direc}"     