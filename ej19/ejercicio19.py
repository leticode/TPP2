'''19. El estacionamiento consiste en muchas plazas. Un vehículo ocupando una plaza genera un ticket 
que está vinculado a esa ocupación temporal.'''
from estacionamiento import Estacionamiento
from plaza import Plaza
from vehiculo import Vehiculo

vehiculo1 = Vehiculo("Lucia Bide", "AA 000 AA", "auto")
vehiculo2 = Vehiculo("Leticia Soulos", "AB 001 AB", "moto")
vehiculo3 = Vehiculo("LValentina Calderone", "AC 010 AC", "triciclo")

plaza1 = Plaza(1)
plaza2 = Plaza(2)
plaza3 = Plaza(3)

estacionamiento1 = Estacionamiento("Rosario Sur", 20)

estacionamiento1.agregar_plaza(plaza1)
estacionamiento1.agregar_plaza(plaza2)
estacionamiento1.agregar_plaza(plaza3)

estacionamiento1.mostrar_plazas()

plaza1.plaza_ocupar(vehiculo1)

plaza1.plaza_ocupar(vehiculo2)

estacionamiento1.mostrar_plazas()

plaza1.plaza_liberar()

estacionamiento1.mostrar_plazas()

plaza2.plaza_ocupar(vehiculo3)

estacionamiento1.mostrar_plazas()