class Usuario:
    todosLosNombres = []
    
    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.todosLosNombres.append(nombre)

    def mostrarNombre(self):
        print("mi nombre es "+self.nombre)

    @classmethod
    def nombreValido(cls, nombre):
        if len(nombre) < 3 or len(nombre) > 15:
            return False
        elif nombre in cls.todosLosNombres:
            return False
        return True
    
    @classmethod
    def mostrarTodos(cls):
        print("Todos los nombres guardados:")
        for nombre in cls.todosLosNombres:
            print("-", nombre)        


if Usuario.nombreValido("Leticia"):     
    usuario1 = Usuario("Leticia")
    usuario1.mostrarNombre()

if Usuario.nombreValido("ab"):     
    usuario2 = Usuario("ab")

Usuario.mostrarTodos()