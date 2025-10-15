from universidad import Universidad
from decano import Decano
from facultad import Facultad

decano1 = Decano("Julio", 44556673, "juliochucho@blbl.com")
decano2 = Decano("Soledad", 22233008, "Soledadposta@gmail.com")
facultad1 = Facultad("Ingenieria", decano1)
facultad2 = Facultad("Medicina", decano2)
universidad = Universidad("Tecnologica Nacional")

universidad.agregarFacultad(facultad1)
universidad.mostrarFcultad()
universidad.agregarFacultad(facultad2)
universidad.mostrarFcultad()
        

