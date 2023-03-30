class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno {self.nombre} se ha creado con éxito.")
    
    def calificacion(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}.")
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nNota: {self.nota}"

# Ejemplo de uso
alumno1 = Alumno("Juan", 7)
print(alumno1)

alumno2 = Alumno("María", 3)
print(alumno2)

alumno1.calificacion()  # imprimirá "El alumno Juan ha aprobado con una nota de 7"
alumno2.calificacion() # imprimirá "El alumno María ha suspendido con una nota de 3"
