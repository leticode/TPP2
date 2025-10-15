from carpeta import Carpeta 
from archivo import Archivo   
carpeta1 = Carpeta("libros")

carpeta1.agregararchivos("piojo.txt", 40, "contenido libro")
carpeta1.agregararchivos("caperucita", 50, "libro")

carpeta1.mostrarinfo()