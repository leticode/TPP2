'''20. Un libro tiene una estructura interna definida por sus capítulos. El libro fue escrito por uno o más 
autores, y es publicado por una editorial. '''
from libro import Libro
autores = [
    {"nombre": "Lucia", "apellido": "Bide", "nacionalidad": "Argentina"},
    {"nombre": "Leticia", "apellido": "Soulos", "nacionalidad": "Uruguaya"}
]

editorial = {"nombre": "La Anonima", "ciudad": "Rosario"}

libro = Libro("Guia para aprobar ingles", autores, editorial, fecha_public=2025)

libro.capitulo_agregar("Verbo to be")
libro.capitulo_agregar("Voz pasiva y activa")
libro.capitulo_agregar("Aprende a hablar como un nativo")

print(libro.info())

print("\nCapitulos:")
print(libro.lista_caps())

cap2 = libro.obtener_capitulo(2)
if cap2:
    print("\nCapitulo encontrado!")
    print("Titulo:", cap2.nombre)