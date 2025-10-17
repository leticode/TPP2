from autor import Autor
from editorial import Editorial
from capitulo import Capitulo

class Libro:
    def __init__(self, titulo, autores_info, editorial_info, fecha_public = None):
        self.titulo = titulo
        self.fecha_public = fecha_public

        self.autores = [Autor(a["nombre"], a["apellido"], a.get("nacionalidad", "")) for a in autores_info]

        self.editorial = Editorial(editorial_info.get("nombre"), editorial_info.get("ciudad"))

        self.capitulos = []
        self.prox_num = 1

    def capitulo_agregar(self, nombre_cap):
        capitulo = Capitulo(self.prox_num, nombre_cap)
        self.capitulos.append(capitulo)
        self.prox_num += 1

    def lista_caps(self):
        if not self.capitulos:
            return "No hay capitulos"
        return "\n".join(str(i) for i in self.capitulos)
        
    def info(self):
        autores_str = ", ".join(str(a) for a in self.autores)
        fecha = f", {self.fecha_public}" if self.fecha_public else ""
        return f"---{self.titulo}{fecha}---\nAutores: {autores_str}\nEditorial: {self.editorial}"

    def obtener_capitulo(self, numero):
        for i in self.capitulos:
            if i.numero == numero:
                return i
        return None

    def __str__(self):
        return f"{self.titulo} - {len(self.capitulos)} capitulos"