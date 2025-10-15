class Alumno:
    contadores = {}  # Diccionario: clave=carrera, valor=número de alumno

    def __init__(self, carrera, nombre):
        # Inicializar el contador de la carrera si no existe
        if carrera not in Alumno.contadores:
            Alumno.contadores[carrera] = 1000
        
        self.legajo = f"{carrera}-{Alumno.contadores[carrera]}"
        
        Alumno.contadores[carrera] += 1

        self.nombre = nombre

# --- Ejemplo ---
a1 = Alumno("ISI", "Ana")
a2 = Alumno("ISI", "Juan")
a3 = Alumno("Mat", "Luis")
a4 = Alumno("ISI", "Marta")
a5 = Alumno("Mat", "Clara")

print(a1.legajo)  # CS-1000
print(a2.legajo)  # CS-1001
print(a3.legajo)  # Math-1000
print(a4.legajo)  # CS-1002
print(a5.legajo)  # Math-1001



