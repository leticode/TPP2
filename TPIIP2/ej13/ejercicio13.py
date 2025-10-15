from examen import Examen
from materia import Materia
from preguntas import Preguntas

examen1 = Examen("cultura general", 1)
examen2 = Examen("colores", 3)

materia1 = Materia("Biologia")
materia2 = Materia("geografia")

materia1.agregarexamenes(examen1)
materia1.agregarexamenes(examen2)

examen1.agregarpreguntas("donde nacio messi?", 5)
examen1.agregarpreguntas("de que color es el cielo?", 10)

materia1.mostrarinfo()