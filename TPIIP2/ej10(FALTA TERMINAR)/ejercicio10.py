##10. Un empleado tiene una oficina asignada o trabaja de forma remota. Los empleados pueden ser
##trasladados a otra oficina.
##(agregacion)
from empleado import Empleado
from oficina import Oficina


oficina1 = Oficina("oficina centro", 1)
oficina2 = Oficina("oficina Zona Norte", 3)

 
empleado1 = Empleado("lucia", "romero", "ingeniera", oficina=oficina1)
empleado2 = Empleado("ramiro", "perez", "contador", trabajaremoto=True)
empleado3 = Empleado("leonel", "messi", "portero", oficina=oficina2)

print("inicial")
print(empleado1)
print(empleado2)
print(empleado3)

print("translado")
empleado2.trasladar(oficina1)
empleado3.trasladar(oficina2)

print(empleado1)
print(empleado2)
print(empleado3)
                    